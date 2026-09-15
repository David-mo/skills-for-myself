# Editorial and brand contract

## Select and freeze the brand

Use the selected project's current site profile, voice, POV, audience files, and approved examples. When using the engine's files, resolve `config/sites/<id>.json` and `config/sites/<id>/{voice,pov,audience}.md`; an article's pinned editorial settings may supersede today's defaults. Store the editorial snapshot and its provenance with the article. Do not send CMS credentials, operational config, or unrelated brand records to models.

User instructions take precedence. The current engine's authoritative editorial policy supersedes inherited presentation quotas. Explicitly approved verbatim passages stay exact; POV beliefs normally should be expressed freshly. A quota from an old skill must not reappear as a different review failure.

Fallback brand facts below are a snapshot from September 15, 2026, not permission to ignore newer supplied brand settings.

| | Growth Partner Index | inBeat |
| --- | --- | --- |
| Reader and role | Marketing leaders evaluating agencies and advertising decisions; GPI is a publication | Growth/brand/creator/paid-media leaders; inBeat is a creator and performance marketing agency |
| Voice | Clear, experienced, evidence-led; explain mechanisms and tradeoffs | Opinionated practitioner; second person for guidance; first-person plural only for supported agency experience |
| Proof | Verified GPI methodology, directory criteria, named external research; never claim it ran an inBeat campaign | Published inBeat case studies and approved master case-study deck; use exact published results, never extrapolate |
| POV | Match measurement to a decision; evaluate partner claims against methods and limitations; distinguish attribution from causation | Creative, creators, media, and measurement form one operating system; creative tests produce learning that informs the next brief |
| CTA | Relevant related GPI guidance; no invented offers or inBeat promotion | Relevant verified service/strategy-call destinations; zero to three useful CTAs, not three mandatory placements |
| Length guidance | Profile range 1,800–4,800 words | Profile range 3,500–4,800 words |
| Graphic tokens | Ink `#111828`, accent `#fe5c33`, white, surface `#f6f8fa`, muted `#626976`, rule `#e3e5e8`, Arial | Ink `#1c2436`, accent `#bfe03e`, white, surface `#f6f6f9`, muted `#586174`, rule `#e8e7ee`, Inter with Helvetica Neue/Arial fallback |

For inBeat, a short topic-specific worldview paragraph after the introduction can make the integrated POV explicit. Pick relevant beliefs; do not paste canonical wording or label the section mechanically. The POV must change recommendations later in the article, not merely advertise the brand.

Prefer no em dashes, negative parallelism ("it's not X, it's Y"), `leverage` as a verb, hype, mechanical transitions, generic scene-setting, or reader insults. Treat minor style deviations as editorial fixes; factual support, useful reasoning, and materially clear prose determine readiness. Never invent first-hand specificity to make writing sound human.

## Evidence ledger

Every used evidence record carries:

```text
id; claim; source_url; original_url; publisher; title;
published_date; retrieved_at; captured_file; exact_support_excerpt;
claim_type (observed/surveyed/modeled/forecast/methodological);
value/unit/denominator/period/geography/population where applicable;
method; limitations; intended_section; verified_status
```

Keep source excerpts only as long as verification needs. Final articles paraphrase and cite; do not exceed applicable quotation limits. For web-derived non-lyrical sources, the engine's normal cap is 25 verbatim words per source in the article.

- Prefer original research, official documentation, transparent studies, regulators, and first-party datasets. Competitor pages reveal reader expectations, not proof for copied claims.
- Chase statistics to the original source. Verify numbers and their period, unit, denominator, sample, geography, method, and source publication date. A retrieval date is not a publication date.
- If a numerical claim lacks an adequate original source or verified date, drop it or research the gap. Do not disguise it as qualitative evidence.
- Foundational or older findings can be useful when honestly dated and qualified. Verify current product behavior or current recommendations separately.
- Preserve distinctions between percent and percentage points, association and causation, attributed and incremental results, reported benchmarks and universal targets.
- Label illustrative calculations and hypothetical examples. Do not present them as research or agency outcomes.
- Maintain source exclusions from the selected brand. Assess actual URL provenance, not just a company name.
- Keep an internal-link inventory with URL, page purpose, existence check, and intended anchor/section. Use relevant destinations naturally, without padding to meet a link count.

## Consolidated review brief

Give the review worker the final draft, compact brand contract, evidence/links actually used, and the brief's reader decisions. Request a short finding list:

```text
check; severity (material/advisory); paragraph_or_asset_id;
exact_affected_passage; evidence_id; reason; requested_change
```

The review must cover thesis support, intent/coverage, examples, counterarguments, numerical accuracy, claim/citation alignment, brand truth, voice/utility, duplication, internal links, and changed-claim integrity. No rewriting, no unsupported "looks good," and no failure based only on length/CTA/source-count targets. The supervising agent adjudicates disputed findings from the originals before paying Fable to repair them.
