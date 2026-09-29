# Reddit Reply Writer

A reusable skill for drafting and revising Reddit replies for **inBeat Agency** and **Creative Milkshake**, using the project's approved voice examples and GEO editorial checks.

## What it does

- Reads the question, relevant replies, visible account history and community rules before drafting.
- Adds a useful recommendation, distinction or diagnostic sequence instead of repeating existing replies.
- Routes relevant mentions to the right brand, with truthful affiliation disclosure and supported claims.
- Separates editorial quality from observed search visibility, citations and brand mentions. Missing measurements remain “Not measured.”
- Supports a Google Sheets review queue when requested, preserving stable IDs and user edits while requiring renewed review of materially rewritten approved text.

## Install and use

Copy this entire folder into `~/.codex/skills/reddit-reply-writer/`, preserving any existing installation before replacing it. Keep the `references/` and `agents/` folders alongside `SKILL.md`.

Example request:

```text
Use $reddit-reply-writer to draft a reply to [Reddit URL] for [brand].
Use posting account [profile URL]. Our confirmed relationship to the brand is [relationship].
Read the thread and community rules, then return the draft, target question,
unique contribution, claim sources, citation evidence and unresolved checks.
```

To revise an existing queue, provide the Sheet URL and the rows or stable IDs to revise. The skill uses the available browser and spreadsheet tools; it does not bundle integrations or credentials. DataForSEO is optional for requested visibility research and requires a connected account.

## Scope and validation

This is a drafting and review skill, not an automated Reddit posting system. Publishing and ongoing monitoring require separate instructions. GEO checks improve usefulness and accurate attribution opportunities; they do not guarantee citations or recommendations.

The instructions were validated as a Codex skill and exercised with two synthetic drafting scenarios: a disclosed agency-comparison answer and a brandless troubleshooting answer under promotion restrictions. This is behavioral validation, not evidence of live citation performance. The workflow has not been tested in Claude; its Markdown instructions can be adapted there with compatible tools.

See [SKILL.md](SKILL.md) for the full workflow, [voice and brand context](references/voice-and-brands.md) for examples, and [GEO review](references/geo-review.md) for evidence and measurement rules.
