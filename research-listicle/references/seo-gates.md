# SEO gates for researched listicles

Read before discovery for articles intended for organic search. SEO is a layer on the evidence workflow, not permission to add unsupported claims or promise rankings. Use the existing Tavily/OpenRouter budgets; reserve roughly two discovery queries and one compact analysis call for this work instead of duplicating the full research pass.

## S1: search intent and positioning, before drafting

Save `seo-brief.json` with the primary query, close variants, reader's buying decision, geography, sampled results with URLs/date/provider, chosen page type, competing formats, and the useful difference this article will offer. Inspect two or three relevant result pages, not just their snippets. Competing articles inform search intent and coverage gaps, never agency facts, inherited rankings, or copied outlines. Search-provider order is not a verified Google rank; record locale/device uncertainty and never invent search volume or difficulty. Use a connected SEO dataset only when it materially helps.

Choose a descriptive title matching both the query and the actual shortlist. When national providers qualify, “UGC agencies for Miami brands” can be more accurate than implying all are based in Miami. Exact-match phrasing is not a quota. Keep a useful slug stable on revisions; an existing live URL needs a migration reason before changing it.

When a publisher domain is known, inspect its relevant existing articles and services. Decide whether to update an existing page, create a distinct page, or report unclear overlap. Record actual internal-link candidates and their role. Distinguish a service page's hiring intent from a comparison guide; overlap is a question to investigate, not automatic cannibalization. Without the domain, finish the content and mark site-specific work pending.

Pass when the format, audience, geography and distinctive contribution are supported by the sampled results and brief. Do not claim a full SERP audit from a handful of provider results.

## S2: useful original analysis and reader experience

Before drafting, identify a defensible contribution beyond rephrasing service pages. Suitable examples: compare what named case studies demonstrate; explain a consequential difference in delivery models; assess linked creative that was actually inspected; normalize verified proposal scopes; analyze primary interview responses supplied or explicitly authorized by the user. Do not require paid outreach or invent hands-on experience. Clearly distinguish observed creative, agency-reported case narratives, and editorial interpretation.

For city pages, include supported differences that affect the buying decision: language capabilities, local shoots, creator availability, relevant local work, or logistics. A provider advertising a capability is evidence of its offer, not independently proven delivery. Where details are missing, turn them into specific questions. Keep office/coverage labels accurate. Do not manufacture local relevance by swapping the city name through a national article.

Show recommendations early: short opening, concise relationship/placement disclosure, useful table, then profiles. Keep the full scoring matrix and operational gate details in QA by default. Maintain the underlying weighted rubric and user priority policy. Public numeric scores require a user preference and an explanation of what they measure; never emit those editorial scores as `aggregateRating` or star-review markup. Put a short methodology after the profiles and retain qualifications beside the claims they limit.

Keep each profile useful on its own: buying fit, concrete services, a supported distinction, relevant work with limits, location/coverage, pricing or honest unknown, and a specific hiring question. Add only decision-relevant FAQs. No target word-count padding or claimed FAQ rich-result benefit. Use descriptive links and a heading/anchor structure the destination renderer supports. Preserve preferred-brand ordering with a clear affiliation disclosure.

Pass when the article adds specific source-supported analysis, answers the buying decision, and reads as a comparison guide rather than a research log. Another model should review new claims against frozen sources; Astra decides final acceptance. Missing firsthand testing is disclosed, not disguised.

## S3: publishing readiness, separate from content acceptance

Deliver a compact publishing handoff with actual values where known and explicit pending items elsewhere. Never put fake author names, placeholder URLs, or unverified internal links into the clean article or structured data.

For a known destination, verify:

- Actual HTML title, H1, meta description, stable intended URL, canonical, and date semantics. Research date is not publication date. Changing the year alone is not a substantive update.
- Real author/reviewer identity and relevant profile; truthful publisher and relationship disclosure. Do not invent expertise or treat a byline as a ranking guarantee.
- Relevant internal links from the article and existing pages pointing to it; confirm target relevance and reachability.
- Public status, crawl access, robots/noindex, canonical consistency, and indexable main content. These are prerequisites, not an indexing guarantee. Respect intentional staging noindex until authorized publication.
- Mobile readability of tables, headings, links and media in the actual CMS output; check page performance if a live page exists. A local draft is not a production check.
- If structured data is useful, use truthful `Article`/`BlogPosting` and applicable breadcrumbs consistent with visible content. Verify current official guidance before implementing. Do not invent publication timestamps, images, reviewers, or ratings, and do not promise rich results from markup.
- If Search Console access exists after publication, inspect actual indexing status and record it separately from a successful fetch. Set up measurement only within authorized scope; no silent recurring monitoring.

Use statuses `pass`, `fail`, `pending`, or `not_applicable`, with evidence for each. Without a destination URL/CMS, mark the technical gate pending and deliver the article plus handoff. Ask for the missing domain/author while continuing independent work; do not hold the entire draft hostage to site details. Never mark all SEO gates passed merely because the Markdown checks passed. Publishing remains subject to the user's actual authorization.

## Economical execution and reporting

Use Tavily discovery/extraction and one small Gemini packet for competitor structure and new factual evidence. Keep source roles separate: competitor observations cannot become agency claim evidence. Reuse same-session verified agency cards; send only changed material plus necessary context to reviewers when possible. Astra makes positioning decisions and final edits; use bounded economical workers for bulk reading and routine checks. Report new calls and costs alongside cumulative receipts on revisions.

QA should record S1/S2/S3 separately from G1–G6, the original contribution actually delivered, unavailable data, site checks still pending, and evidence refresh date. Never promise rankings, a traffic lift, AI citations, or that a checklist equals SEO performance.

Official references (verify current guidance when applying technical recommendations): [review quality](https://developers.google.com/search/docs/specialty/ecommerce/write-high-quality-reviews), [helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content), [SEO starter guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide), [technical requirements](https://developers.google.com/search/docs/essentials/technical), [Article structured data](https://developers.google.com/search/docs/appearance/structured-data/article).
