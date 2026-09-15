#!/usr/bin/env python3
"""Check locked evidence structure; semantic review is still required."""
from datetime import date, datetime
import json
from pathlib import Path
import sys
from urllib.parse import urlparse


def validate(data, root):
    errors = []
    def need(ok, message):
        if not ok:
            errors.append(message)
    def url_ok(value):
        try:
            return urlparse(value).scheme in ('https', 'http') and bool(urlparse(value).hostname)
        except (ValueError, TypeError):
            return False
    sources = {}
    texts = {}
    brief = data.get('brief', {})
    policy = brief.get('geography_policy')
    need(policy in ('local_office', 'metro_office', 'serves_market', 'not_applicable'), 'Invalid geography policy')
    need(bool(brief.get('topic')), 'Missing topic')
    try:
        as_of = date.fromisoformat(brief['as_of'])
        need(as_of <= date.today(), 'Research date is in the future')
    except (KeyError, ValueError, TypeError):
        as_of = None
        need(False, 'Missing/invalid research date')
    for s in data.get('sources', []):
        sid = s.get('id')
        need(bool(sid) and sid not in sources, 'Missing/duplicate source ID: ' + str(sid))
        sources[sid] = s
        need(url_ok(s.get('url')), 'Invalid source URL: ' + str(sid))
        need(s.get('kind') in ('official', 'client', 'independent', 'directory', 'search_snippet'), 'Unclassified source: ' + str(sid))
        try:
            checked = datetime.fromisoformat(s['checked_at'].replace('Z', '+00:00')).date()
            need(checked <= date.today(), 'Future source check: ' + str(sid))
            need(as_of is None or checked >= as_of, 'Source predates research session: ' + str(sid))
            path = (root / s['path']).resolve()
            need(path.is_relative_to(root.resolve()), 'Source path escapes research directory: ' + str(sid))
            if path.is_relative_to(root.resolve()):
                texts[sid] = path.read_text()
        except (ValueError, KeyError, OSError, TypeError):
            need(False, 'Missing/invalid source date or file: ' + str(sid))
    selected = [a for a in data.get('agencies', []) if a.get('selected') is True]
    need(bool(selected), 'No selected agencies')
    names, domains, all_claims = set(), set(), set()
    for a in selected:
        name = a.get('name', '')
        need(bool(name) and name.casefold() not in names, 'Missing/duplicate agency: ' + name)
        names.add(name.casefold())
        site = a.get('website')
        need(url_ok(site), 'Invalid official website: ' + name)
        domain = (urlparse(site or '').hostname or '').lower().removeprefix('www.')
        need(domain not in domains, 'Duplicate agency domain: ' + name)
        domains.add(domain)
        need(not a.get('conflicts'), 'Unresolved conflicts: ' + name)
        need(bool(a.get('selection_reason')), 'Missing selection reason: ' + name)
        claims = {}
        for c in a.get('claims', []):
            cid = c.get('id')
            need(bool(cid) and cid not in all_claims, 'Missing/duplicate claim ID: ' + str(cid))
            all_claims.add(cid)
            claims[cid] = c
            need(bool(c.get('text')) and bool(c.get('field')), 'Empty claim: ' + str(cid))
            need(c.get('status') in ('verified', 'unverified', 'conflicted'), 'Invalid claim status: ' + str(cid))
            if c.get('status') != 'verified':
                continue
            need(bool(c.get('evidence')), 'Verified claim lacks evidence: ' + str(cid))
            for ev in c.get('evidence', []):
                sid, excerpt = ev.get('source_id'), ev.get('excerpt')
                need(sid in sources, 'Unknown evidence source: ' + str(cid))
                need(sources.get(sid, {}).get('kind') != 'search_snippet', 'Snippet used as proof: ' + str(cid))
                need(isinstance(excerpt, str) and bool(excerpt.strip()) and excerpt in texts.get(sid, ''), 'Excerpt missing from saved source: ' + str(cid))
        eligibility = a.get('eligibility', {})
        required = ['identity', 'category'] + ([] if policy == 'not_applicable' else ['geography'])
        for field in required:
            ids = eligibility.get(field, [])
            need(bool(ids), 'Missing ' + field + ' eligibility: ' + name)
            for cid in ids:
                c = claims.get(cid, {})
                need(c.get('status') == 'verified', 'Unverified eligibility: ' + str(cid))
                kinds = [sources.get(e.get('source_id'), {}).get('kind') for e in c.get('evidence', [])]
                allowed = ('official',) if field != 'geography' else ('official', 'independent')
                need(any(k in allowed for k in kinds), 'Weak eligibility source: ' + str(cid))
        allowed_geo = {'local_office': ('local_office',), 'metro_office': ('local_office', 'metro_office'), 'serves_market': ('local_office', 'metro_office', 'serves_market', 'remote'), 'not_applicable': ('not_applicable',)}
        need(a.get('geography_class') in allowed_geo.get(policy, ()), 'Geography outside scope: ' + name)
        best = a.get('best_for', {})
        need(bool(best.get('text')) and bool(best.get('claim_ids')), 'Missing grounded best-for: ' + name)
        for cid in best.get('claim_ids', []):
            need(claims.get(cid, {}).get('status') == 'verified', 'Unsupported best-for claim: ' + str(cid))
    return {'passed': not errors, 'errors': errors, 'selected_count': len(selected), 'scope': 'Structural evidence only; Astra semantic/editorial acceptance still required'}


if __name__ == '__main__':
    try:
        path = Path(sys.argv[1]).resolve()
        result = validate(json.loads(path.read_text()), path.parent)
        print(json.dumps(result, indent=2))
        sys.exit(0 if result['passed'] else 1)
    except (ValueError, KeyError, TypeError, OSError, IndexError, AttributeError) as exc:
        print(json.dumps({'passed': False, 'error': 'Invalid evidence input: ' + type(exc).__name__}))
        sys.exit(1)
