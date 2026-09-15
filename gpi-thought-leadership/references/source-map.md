# Provenance and intentional simplifications

Source repository: `https://github.com/David-mo/content-pipeline-gpi`.
Authoring inspection: September 15, 2026, fetched `origin/main` at commit `95d86379fad3705c9f8214c06d6181c8309f221d`.
Local source checkout: `/Users/davidmorneau/Documents/content-pipeline-gpi`. Its checked-out branch was older; this skill uses the fetched main snapshot for current policy. No engine source or deployment was changed.

| Source at that commit | Preserved behavior |
| --- | --- |
| `pipeline/standards/editorial_policy.md` | Substance takes precedence over inherited quotas; brand truth, useful explanations, factual support, lossless delivery |
| `pipeline/standards/{research,brief,draft,quality_gate}.md` | Verified source ledger, thesis and reader decision, structured coverage, evidence-linked review findings |
| `pipeline/standards/visuals.md` | Candidate admission, real-image observation, branded original graphics, pixel review, coverage/recovery, truthful recreations |
| `pipeline/visual_coverage.py:22` | Site-specific coverage target, selected vs delivered counts, long sections without visuals |
| `pipeline/source_images.py:21` | Five distinct search rounds and bounded acquisition |
| `pipeline/prompts.py:132` | Generated illustrations as executable requests; conceptual vs artifact recreation; no fabricated evidence |
| `pipeline/config.py:26` | Fable writer, separate support/review/image models, cost target |
| `pipeline/providers.py:529` | Stable/shared/tail messages and existing Anthropic caching |
| `pipeline/providers.py:553` | Validated response reuse, token/reservation accounting, incomplete-response rejection |
| `pipeline/prompts.py:309` | Existing stage-specific context pruning |
| `config/sites/{gpi,inbeat}.json` and companion prose files | Brand voice, proof, POV, visual tokens and targets |

The engine already has prompt caching, context pruning, artifact reuse, and conservative cost reservations. This skill does not claim to invent these or diagnose an absence of them. High reasoning allowances and many separately orchestrated stages are opportunities to assess, not proof of actual waste on every article.

Intentional standalone changes:

- Use Flash for bounded extraction and consolidated review, with supervisor adjudication, instead of copying every stronger model/recovery stage. Quality equivalence needs measured article trials.
- Keep Fable on all article prose, including final metadata/captions. Fold small outputs into existing calls.
- Draft with voice rules up front; run a targeted voice repair only when findings justify it.
- Retain the latest visual coverage effort and source-image quality rules. Save cost by caching, reusing, and repairing only changed work, not by skipping image identification/creation.
- Use article artifacts rather than engine database contracts, scheduling, CMS state, or application recovery machinery.
- Do not impose the old personal inBeat skill's blanket 5–8 visuals, 10–16 internal links, three CTAs, or compulsory Google Docs delivery.

Validation of this documentation does not prove a live article completed through these routes, prove the current deployed engine revision, or establish a cost/quality benchmark.
