# Tool execution and receipts

Resolve `SKILL` to this skill directory. The examples below use Dave's installation. Helpers need Python 3.9+ on macOS/Linux, standard library only. Run one operation at a time per run; a file lock prevents overlapping budget reservations.

```sh
python3 /Users/davidmorneau/.codex/skills/research-listicle/scripts/research.py doctor --live-models
python3 /Users/davidmorneau/.codex/skills/research-listicle/scripts/research.py search --run work/listicle-miami --query 'Miami UGC agency creator content production' --max-results 6
python3 /Users/davidmorneau/.codex/skills/research-listicle/scripts/research.py extract --run work/listicle-miami --urls-file work/listicle-miami/urls.json
python3 /Users/davidmorneau/.codex/skills/research-listicle/scripts/research.py worker --run work/listicle-miami --role extract --prompt-file work/listicle-miami/extract-prompt.txt --input-file work/listicle-miami/source-packet.json
python3 /Users/davidmorneau/.codex/skills/research-listicle/scripts/research.py worker --run work/listicle-miami --role draft --prompt-file work/listicle-miami/draft-prompt.txt --input-file work/listicle-miami/approved-packet.json
python3 /Users/davidmorneau/.codex/skills/research-listicle/scripts/research.py worker --run work/listicle-miami --role verify --prompt-file work/listicle-miami/verify-prompt.txt --input-file work/listicle-miami/review-packet.json
python3 /Users/davidmorneau/.codex/skills/research-listicle/scripts/gate.py work/listicle-miami/evidence.json
```

`urls.json` is an array of 1–10 actual discovered HTTP(S) URLs. Requests return compact receipts with result paths, never whole page content. Search results are saved as provider JSON. Extraction additionally saves immutable source text and a source manifest: classify each manifest source (`official`, `client`, etc.) before including it in evidence.json. IDs are based on URL; if a later extraction refreshes the same URL, choose one version and its path deliberately, never duplicate the source ID. Read failure URLs even on partial success; a completed extraction is not proof every requested URL worked.

Build `source-packet.json` with brief, the relevant evidence contract, and source ID/URL/content for just the current batch. Include enough context around excerpts to detect caveats. Create prompt files from the role section in worker-prompts.md. Helpers do not automatically read references or inject the schema: include the relevant contract in the prompt/input packet. For the writer, filter to selected agencies and claims with status `verified`, retaining each supporting URL and excerpt. Strip test annotations, machine statuses, and internal gate commentary from the writer's brief. Do not pass unverified claims and hope the writer ignores them. Reviewer input contains final draft, approved cards, and supporting excerpts. Parse and inspect worker output; fenced JSON is not a valid evidence file until explicitly parsed and saved.

Defaults checked against the live OpenRouter catalogue on 2026-09-14: Gemini `google/gemini-3.8-flash` for extract/verify and DeepSeek `deepseek/deepseek-v4.1-flash` for prose, with low reasoning. These are configurable defaults, not timeless best-price claims. No automatic model fallback. If the existing gemini-reader MCP fails at transport level, its documented shell reader is an available route; don't silently switch model/provider. Do not retry auth/quota failures. A separate cheap verifier does not replace Astra's acceptance.

## Credentials

Tavily: configured private file `~/.config/listicle-research/tavily-key`, or `TAVILY_KEY_FILE`, then `TAVILY_API_KEY` if no file exists. OpenRouter: existing shared `~/.config/deepastra/openrouter-key`, or `OPENROUTER_KEY_FILE`, then `OPENROUTER_API_KEY` if no file exists. Paths can also be set in config. `doctor` reports presence only; `--live-models` checks public model availability, not authentication.

Never print keys or put them in a brief, prompt, output, argument, source URL, or generated skill. If missing, ask for an existing credential-file location or use hidden terminal entry (`getpass`) to save to a private file with mode 0600. Do not ask the user to paste a key in chat. Do not overwrite shared credentials as routine troubleshooting.

## Budget and failure behavior

Each attempted external request reserves a receipt before sending. Identical successful requests are reused within the same research run; identical failed/uncertain requests are blocked for review. Network errors are not automatically retried. Provider error bodies are not printed. Token-limit, refusal, and empty worker outputs fail even when HTTP succeeds. Keep saved output/usage for diagnosis; split an oversized packet, don't accept a truncated answer.

Call ceilings count attempts, including failures; editing configuration to raise a ceiling is a deliberate brief/budget decision, never an error workaround. `--config /absolute/run-config.json` precedes the subcommand when a user-approved run requires different limits/models. A clock timeout is not a cost limit. A provider failure with no receipt of usage may still have been billed: report it as unknown.

`receipts.json` records provider, operation, request ID, model, timestamps, raw returned usage and returned cost. For Tavily retain returned credit usage without assuming it is a dollar charge. Extract credits can be reported in grouped increments. Sum known costs but explicitly list requests with unknown costs; don't substitute zero. Separate other tool/reader/Luna/Astra usage when available. No asserted token savings without a measured baseline.

## API sources

The helper uses Tavily's [Search](https://docs.tavily.com/documentation/api-reference/endpoint/search) and [Extract](https://docs.tavily.com/documentation/api-reference/endpoint/extract) REST endpoints, and OpenRouter [chat completions](https://openrouter.ai/docs/quickstart), [model catalogue](https://openrouter.ai/docs/api/api-reference/models/get-models), and [usage accounting](https://openrouter.ai/docs/cookbook/administration/usage-accounting). Verify current official docs if endpoint behavior changes. Search uses explicit basic depth by default, disables synthesized answers/raw page content, and requests usage. Extraction saves original content separately; model requests contain no tools or automatic fallback model.
