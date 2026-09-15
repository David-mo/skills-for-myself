---
name: gpi-thought-leadership
description: Create evidence-led, brand-specific thought-leadership articles using the GPI content engine's editorial and visual methods, with Fable 5.1 writing through OpenRouter and measured cost controls. Use for the GPI-derived article workflow, including research, source-image discovery, original graphics, brand voice, and article revisions. Not for ranked listicles or statistics roundups.
---

# GPI thought leadership

Produce a defensible argument that helps a particular reader make a decision. Preserve the engine's strengths: traceable evidence, a brand-specific point of view, concrete examples, useful sourced images, accurate original graphics, and inspection of the delivered article.

This is a standalone personal authoring workflow distilled from `content-pipeline-gpi`, not a command to run, change, or publish through that application. The name identifies the method; it does not force every article to use the Growth Partner Index brand.

## Roles and scope

- **Fable 5.1 through OpenRouter owns the thesis/brief, article prose, substantive revisions, voice edits, final captions, and reader-facing metadata.** Use the exact model `anthropic/claude-fable-5.1`. Do not substitute another writer silently.
- Use `google/gemini-3.8-flash` through OpenRouter for source extraction, inventories, coverage mapping, visual planning, and evidence-linked review findings. It proposes changes, not replacement article prose.
- The supervising agent decides scope, checks original evidence, resolves ambiguous findings, and verifies delivery. Its usage is separate from OpenRouter spend.
- Use deterministic tools for link inventories, arithmetic, file hashes, charts, and packaging. Use an available image-generation tool for admitted illustrations; follow its current instructions. Track its cost separately if it does not bill through OpenRouter.
- Read [OpenRouter and cost control](references/openrouter-costs.md) before paid calls, [editorial and brand rules](references/editorial-brand.md) before research, and [visual production](references/visuals.md) before selecting or generating images. [Source map](references/source-map.md) documents the inspected engine revision and intentional changes.

When the request explicitly uses this skill, these current GPI-derived rules govern instead of the older `write-inbeat-thought-leadership` skill's fixed link, length, CTA, and visual quotas. Do not automatically chain both workflows.

## 1. Set the article contract

Use the topic, brand, reader, market, language, desired outcome, and destination supplied by the user. Infer unambiguous details from project context. Ask about a missing brand when it cannot be inferred; selecting the wrong brand changes the whole article.

Create `articles/<slug>/` with these persistent artifacts, adding each when its stage runs:

| Artifact | Purpose |
| --- | --- |
| `brand.json` | Resolved brand identity, voice, POV, proof restrictions, visual tokens, byline, CTA destinations, source exclusions, and source/version of this snapshot |
| `brief.md` | Reader decision, thesis, search intent, section IDs and budgets, evidence mapping, useful comparisons, required explanations |
| `sources.json` + `sources/` | Evidence ledger, captures, verified internal destinations, search date/method and coverage gaps |
| `article.md` | Fable's article, metadata, stable paragraph/figure IDs, linked citations |
| `visuals.json` + `assets/` | Candidate decisions, search attempts, selected/delivered assets, provenance, placement, and inspection results |
| `qa.md` | Findings with exact locations, fixes, exceptions, and final delivery readback |
| `calls.jsonl` + `costs.json` | Call-level usage, reservations, external costs, estimates, and unresolved charges |

Set a topic-appropriate word target, normally 2,000–4,500 words, considering brand guidance and the user's request. Budget sections by what must be explained. Longer is warranted by additional substance, never filler. Use the destination's heading conventions: a standalone article can have an H1; engine/CMS imports may store the title separately.

Default planning target: **US$3 of provider/API spend per completed article**, inherited as an aspiration from the engine, not a guarantee or permission to spend indefinitely. Forecast text, research, visuals, and revision reserve before starting. Record a bounded run ceiling consistent with the user's existing budget; if none exists, initially use $3 and surface a forecast that cannot fit before dependent paid work. Do not inherit the engine's $20 hard ceiling automatically.

## 2. Research once and retain the evidence

1. Check the brand's live sitemap/content inventory for overlap and useful internal links. Identify whether the task is a new article or an update.
2. Inspect current search results for the intended keyword/market. Start with 5–7 useful competitor pages when SEO is in scope. Name the actual search provider; do not label another engine's results as Google or invent volume/KD metrics.
3. Fetch original sources and give the extraction worker only those captures. Retain full captures locally, send relevant sections for bounded jobs, and expand when surrounding context is needed. Do not treat search snippets as evidence.
4. Build the ledger described in the editorial reference. Start with roughly 10–12 useful evidence entries across six independent domains when the topic supports it; support and diversity matter more than counts. Find counterevidence and limitations.
5. Collect source-image opportunities during these same page reads. Reuse the inventory later rather than repeating research.
6. Stop researching when the central argument, decision-critical sections, examples, and material factual claims have adequate support. Conduct one focused gap batch for specific missing evidence; further research needs a named unresolved claim and remaining budget.

Do not give Fable raw search dumps or the full crawl. Give it the resolved brand contract, verified evidence with exact excerpts and limitations, internal-link inventory, intent/coverage summary, and explicit gaps.

## 3. Let Fable build the argument and draft

Make one Fable brief call: a debatable thesis, the reader decision, why now, ordered sections, tradeoffs/counterargument, practical framework, evidence IDs, and provisional visual opportunities. Review this compact brief against the evidence before funding a full draft. Correct structural gaps here.

Make one Fable drafting call from the accepted brief and evidence packet. Ask it to:

- Establish the consequence quickly; explain mechanisms and where advice stops applying.
- Carry the selected brand's POV through actual recommendations, with no invented experience.
- Use concrete, supported examples and inline citations beside the relevant claims.
- Write natural transitions, useful comparisons, a substantive close, and FAQs only if they answer real reader questions.
- Apply the brand's voice and humanization rules during drafting, including varied rhythm and cutting generic filler.
- Include accurate metadata and provisional captions in the same response to avoid separate premium calls for small fields.

Do not require an unconditional second full-draft voice pass. After the draft, run local integrity checks and one consolidated evidence/voice/utility review with the cheap worker. It must cite exact passages and source IDs, distinguish material failures from suggestions, and assess the actual article rather than private planning notes.

Send only actionable findings, affected blocks, relevant adjacent prose, evidence, and the accepted brief to Fable. Prefer one targeted revision call. Allow at most two substantive repair rounds without a new plan; if the same central failure survives, stop the loop and report the precise gap. Never sacrifice evidence or silently accept a failed article to meet the budget.

## 4. Identify, produce, and inspect the images

Follow the visual reference. Plan source discovery and original graphics together, but generate only admitted assets after the argument is stable.

For the current GPI/inBeat defaults, aim for `max(2, min(8, round(body_words / 700)))` inline visuals and two useful externally sourced examples. These guide search effort. Weak visuals do not become acceptable to meet the target. Preserve the five-strategy search process and explicit coverage exceptions described in the reference.

Reuse unchanged, inspected source bytes and successful original graphics. Fix captions or placement without regenerating the image. Have Fable finalize any new reader-facing captions in a single batch or the existing prose repair call.

## 5. Gate and deliver

Check the following against the final artifact:

- **Argument:** distinctive, defensible thesis; practical reader decision; developed mechanisms, tradeoffs, and meaningful section coverage.
- **Evidence:** every material claim is supported; numbers/quotes/qualifiers are faithful; internal destinations exist; no fabricated authority, byline, or brand proof.
- **Brand and prose:** selected voice and POV affect the recommendations; no cross-brand contamination, generic padding, reader put-downs, or unsupported claims introduced during revision.
- **Visuals:** actual pixels pass per-image checks; final bytes, sources, captions, placement, and set review agree; coverage shortfalls are explicit.
- **Delivery:** links and images resolve in the delivered file or destination; no placeholder is described as a completed asset; actual structure, metadata, captions, and byline survive readback.

Record each material failure with its location and next action. Optional media may be omitted with a justified coverage exception. Missing required explanations/assets remain visible gaps. An incomplete article can be handed over as a draft, never labeled publish-ready.

Default to a local article package. If the user requests Google Docs, Word, or another destination, use that destination's skill and verify the real result. Publication, CMS mutation, and sending messages require authorization from the task; creating this skill does not authorize them.

Hand off the article link/path, thesis, delivered visual count and exceptions, QA status, and measured provider costs with any unknowns. State whether costs exclude supervision or unpriced tools. Do not claim optimized quality/cost until comparable completed articles have been measured.
