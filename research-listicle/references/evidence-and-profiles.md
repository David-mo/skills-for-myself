# Evidence and output contract

## Sources and agency cards

Maintain `evidence.json` with `brief`, `sources`, and `agencies`. Source IDs and claim IDs are unique. Paths are relative to the evidence file. Store full extracted text in each source file before a worker sees it; preserve URL and retrieval metadata separately.

```json
{
  "brief": {"topic": "Top UGC agencies in Miami", "geography_policy": "local_office", "as_of": "YYYY-MM-DD"},
  "sources": [{"id": "s1", "url": "https://agency.example/contact", "kind": "official", "checked_at": "YYYY-MM-DD", "path": "sources/s1.md"}],
  "agencies": [{
    "name": "Example", "website": "https://agency.example", "selected": true,
    "geography_class": "local_office",
    "claims": [{"id": "a1-location", "field": "location", "text": "Operates a Miami office.", "status": "verified", "evidence": [{"source_id": "s1", "excerpt": "Our Miami office"}]}],
    "eligibility": {"identity": ["a1-identity"], "category": ["a1-category"], "geography": ["a1-location"]},
    "best_for": {"text": "A specific buyer/use case", "claim_ids": ["a1-category"]},
    "selection_reason": "Why this agency merits inclusion under the shared criteria.",
    "unknowns": ["pricing"], "conflicts": [], "exclusion_reason": null
  }]
}
```

This shape illustrates fields, not a passing fixture: create real identity/category claims and evidence. Allowed source kinds: `official`, `client`, `independent`, `directory`, `search_snippet`. Only the first four can support a verified claim; snippets/AI summaries are discovery only. Eligibility requires official evidence for identity and category. Geography requires an official source or strong independent reporting, plus human verification of actual office vs. mere coverage. Do not treat a directory as proof of local presence.

Claims use `verified`, `unverified`, or `conflicted`. Only verified claims may enter the article. A verified self-reported outcome remains attributed, e.g. “The agency reports …”; verified means the source supports the statement, not independent validation. `conflicts` must be empty for selected entries; keep resolution notes in QA. Record fields searched but unconfirmed in `unknowns`. Do not infer “quote-based pricing” from missing prices: write “Pricing: not publicly listed on the pages reviewed” or “Request a proposal” without inventing a pricing model.

For every published detail capture exact original evidence: name/domain, office, service, deliverables, industry focus, platform, clients, results, pricing, review score. Prefer official service/contact pages and client or agency case studies. Find independent corroboration for consequential quantitative performance claims where practical; otherwise attribute and state relevant limits. A client logo is not proof of a UGC engagement or a result. Record result metric, baseline, period, scope, and who reported it; omit a number if its meaning is unclear. Ratings need source, count, date, and exact entity; omit by default.

For UGC, distinguish content production from influencer distribution. Research creator sourcing, briefs, filming, editing, paid-ad variations, testing, rights/usage duration, and whitelisting/partnership ads where evidenced. Don't attribute all of these services to every agency. For other categories replace these with the actual buyer's decision criteria; retain evidence discipline.

## Reader-facing article

1. **SEO pack:** proposed title, slug, and natural meta description (roughly 140–160 characters; don't damage clarity to hit a count). Include the actual research date. A year in the title must match the evidence refresh. Keep metadata visually separate from article body.
2. **H1 + short opening:** explain who the list is for and what qualifies, then get to the agencies. No generic market history or unsourced market-size statistics.
3. **Quick comparison:** name linked to its profile/site, best for, precise location status, core service/deliverable, published starting price or honest unknown. Put shared pricing unknowns in one note rather than adding a repetitive column. Keep numeric scores in QA unless requested. Add a column only when it helps compare. Table values must agree with profiles.
4. **How we selected (after profiles by default):** explain category/geography screening, sources and check date, ranking vs. numbered shortlist, and known publisher affiliation. Avoid “we tested,” objective “best overall,” or numerical scoring without actual support.
5. **Numbered profiles:** use the same core structure below, while writing distinct paragraphs.
6. **How to choose:** a short buyer checklist specific to the topic; for UGC cover production scope, creator fit, rights/duration, revision limits, paid usage, delivery cadence, testing, and what a quote includes. Frame unverified contract terms as questions to ask, not agency facts.
7. **FAQ only when useful:** usually 3–4 questions that resolve buyer intent without repeating profiles. Never manufacture market-wide price averages.
8. **Closing:** a short next step tied to the reader's needs. Promotional CTA/internal links only with supplied publisher context and verified destinations. No default inBeat sales pitch.

### Each agency profile

`## 1. Agency name — specific best-fit label`

A short editorial paragraph explains what it does, why it made the list, and the buyer it suits. This is a synthesis of sourced capabilities, not agency marketing copied into third person.

- **Location:** actual headquarters/office or accurately disclosed coverage; cite office evidence.
- **Best for:** concrete buyer, campaign, or operating need; explain the reasoning from evidence, not a fabricated award.
- **UGC services / deliverables:** 3–5 verified, specific capabilities when available; fewer beats invention.
- **Why consider it:** a distinctive operating model, relevant specialization, or demonstrated work with a direct citation.
- **Relevant work / clients:** strongest verified example with scope, attribution, and limits; do not add logo names to pad the entry. If missing, say a relevant public case study was not found on reviewed pages.
- **Pricing:** published amount, currency, pricing basis/minimum, date and source; otherwise an honest unknown. A directory project minimum is not a UGC package price.
- **Before signing:** a relevant question/gap to confirm, or a sourced limitation. No invented negative review or stock “cons.”
- **Website:** direct official link.

Omit optional founded date, headcount, awards, ratings, imagery, and arbitrary pros/cons unless they materially help the decision and have evidence. Material profile claims need nearby links to the pages that support them; a homepage link at the bottom is not universal support. Quote sparingly and paraphrase originals without copying competitors' profile structure or phrasing.
