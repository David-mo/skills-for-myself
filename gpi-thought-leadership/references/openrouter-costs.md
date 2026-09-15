# OpenRouter routing and article economics

## Model ownership

| Work | Default route | Output |
| --- | --- | --- |
| Source extraction, inventories, intent mapping, visual opportunities | `google/gemini-3.8-flash` | Compact evidence and planning records |
| Thesis/brief, article, substantive/voice edits, final captions/metadata | `anthropic/claude-fable-5.1` | Reader-facing prose and its editorial plan |
| Consolidated factual/brand/utility review | Flash plus supervising-agent adjudication | Exact findings, not rewritten prose |
| Actual image inspection | Available image-capable reviewer/tool | Asset-specific pixel findings with source context |
| Accurate charts, diagrams, counts, hashes, document assembly | Local deterministic tools | Files and integrity checks |
| Admitted raster illustrations | Available image-generation tool, following current tool instructions | Inspected original assets; account for separately if outside OpenRouter |

The image route must never be confused with the writer route: Fable produces article text, not raster image output. The inspected engine uses `google/gemini-3.1-flash-image` for image generation and a separate visual reviewer. Reuse that route only if it is callable, currently supported, and permitted by the active tools. If a required tool is unavailable, report the gap instead of inventing a successful asset.

The cheaper support/review allocation is a proposed standalone default. Its quality parity with the engine's stronger review models has not been measured. Escalate an ambiguous material finding to the supervisor with original evidence; a stronger paid review is a named, budgeted decision. Do not escalate routine formatting to the writer or silently change writer models after an error.

## Live preflight and credentials

Fetch the live OpenRouter model catalog/endpoints before spending: verify exact IDs, availability, context/output limits, supported parameters, provider pricing, and any long-context tier. Use current primary documentation for request semantics. A model listing is not a successful authenticated generation.

Use the existing shared credential file `~/.config/deepastra/openrouter-key`, or `OPENROUTER_API_KEY` if that file is absent. Read the secret privately inside the client process; do not print it, place it in prompts, write it to article files, or put it directly into shell command text. If neither is available, report the connection requirement. The skill documents an HTTP workflow; it does not install a new MCP tool or client.

Send text requests to `POST https://openrouter.ai/api/v1/chat/completions` with `Authorization: Bearer <privately loaded key>`. Example request body; replace values from real artifacts and the current budget:

```json
{
  "model": "anthropic/claude-fable-5.1",
  "messages": [
    {"role": "system", "content": "Stable role, editorial rules, resolved brand contract"},
    {"role": "user", "content": "Verified evidence, accepted brief, specific output request"}
  ],
  "max_tokens": 8000,
  "provider": {"sort": "price", "require_parameters": true}
}
```

This example is a shape, not a universal token budget. Size the completion allowance for the requested article and any model reasoning within that limit. Prefer low reasoning for bounded support work when supported; do not arbitrarily add a 32k reasoning reserve to every call. Detect length truncation, empty/error responses, and invalid structure before accepting an artifact. Preserve incomplete output as incomplete; never pass it as a finished article.

Use the single writer model ID; omit automatic model fallback lists. Same-model provider failover is allowed within price/capability/privacy constraints. Set `provider.max_price` from the forecast if useful; its prompt/completion values are **USD per million tokens**, whereas catalog `pricing.prompt`/`pricing.completion` values are per token. A price ceiling is not an article spending cap.

## Reduce repeated work

1. Cache source fetches and search results by URL/query, market, capture date, and retrieval options. Refresh when claim currency or the requested update requires it.
2. Cache completed, validated stage artifacts by hash of model, instructions, brand snapshot, schema, selected evidence, input text, and image hashes. Any changed dependency invalidates the affected work. Never reuse a partial/error response as a passing artifact.
3. Put stable role/brand/rules first, reusable evidence second, and volatile date/revision instructions last. Send only stage-relevant data; avoid full chat history, rejected image inventories, and repeated crawler dumps in Fable calls.
4. Use Anthropic content-block `cache_control: {"type":"ephemeral"}` when a sufficiently large unchanged prefix will actually be reused within its TTL. Verify current model/provider support and minimum size. Cache writes can cost extra; a one-off prefix may be cheaper uncached. Keep provider affinity where it helps, then inspect actual cached-token counters rather than assuming a hit. Do not add prose just to qualify for caching.
5. Combine related small outputs into the brief/draft/final-caption calls. Run one consolidated review instead of independent repeated fact, voice, structure, and metadata rewrites. Preserve independent verification of facts and actual image pixels.
6. Repair exact failed blocks and affected dependencies. Do not restart successful research or rebuild passing images after a local caption edit.

## Forecast, reserve, settle

Before each paid request, record a reservation in `calls.jsonl` and include it in available-budget calculations. Use an available tokenizer or conservative upper-bound estimate rather than a best-case word/token ratio. Include provider maximum completion tokens (including reasoning), images, long-context pricing, and known request fees. No cache discount belongs in the conservative preflight unless guaranteed.

```text
call reservation = input_token_ceiling * input_USD_per_token
                 + max_completion_tokens * output_USD_per_token
                 + known_image_or_request_costs
available = run_ceiling - settled_costs - outstanding_reservations
```

If a call cannot fit, reduce unnecessary context, scope a smaller repair, or surface the shortfall before calling. Do not shorten a needed article or omit factual checks silently. Allocate revision and image-discovery headroom before consuming the draft budget.

Record for every attempt: article/stage ID, timestamp, request hash, requested/returned model, actual provider, generation ID, attempt, status, reservation, input/output/reasoning/cache tokens, response `usage.cost` when present, and any external charges. Save output separately. Verify the returned writer identity before accepting prose.

Settle from actual reported cost; reconcile a missing cost through `GET https://openrouter.ai/api/v1/generation?id=<generation_id>` when an ID exists, using its `data.total_cost`. A missing cost is `unknown`, not zero. Do not add upstream inference cost to `usage.cost` if it is already included. Show any confirmed funding/payment fee separately; the old engine's configured 5.5% is not evidence that every current call owes an extra 5.5%.

Transport interruption or an uncertain provider outcome retains its reservation. Do not blindly retry a potentially completed charged request. Check the generation record first where possible. Stop on auth/balance/quota errors. At most one automatic retry for a clearly rejected transient request; count all attempts and stop repeated identical failures. Content repairs have the separate two-round limit in SKILL.md.

Track search/SEO API costs, image-generation costs, paid assets, and other tools separately. If tool pricing is unavailable, include an unpriced item and report the total as incomplete. Supervision/Codex usage must either be included from real usage evidence or explicitly excluded.

## Measure the result

The engine's $3 target is a planning aspiration. Use live rates and actual article requirements; no guaranteed price or percentage savings is established by this skill.

Report per article: settled text cost, search cost, visual cost, other known costs, pending reservations/unknowns, total known spend, elapsed time, retry count, QA result, and delivered visual coverage. Compare like-for-like articles and include failed attempts:

`cost per accepted article = all attributable attempts and repairs / accepted articles`

Before claiming improvement, compare several similar articles against an actual engine baseline on factual accuracy, brand fidelity, argument usefulness, image usefulness/coverage, and final delivery. A lower bill obtained by cutting required sourcing or shipping pending assets is not equivalent quality.

## Primary API references

- [Fable 5.1 model and pricing](https://openrouter.ai/anthropic/claude-fable-5.1)
- [Gemini 3.8 Flash model and pricing](https://openrouter.ai/google/gemini-3.8-flash)
- [Prompt caching and usage counters](https://openrouter.ai/docs/guides/best-practices/prompt-caching)
- [Provider routing and price controls](https://openrouter.ai/docs/guides/routing/provider-selection)
- [Model catalog](https://openrouter.ai/api/v1/models)
- [Generation lookup](https://openrouter.ai/docs/api/api-reference/generations/get-generation)

These references were checked during skill authoring on September 15, 2026; refresh live prices and capabilities for each run.
