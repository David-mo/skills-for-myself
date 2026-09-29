# GEO review and measurement

## Evidence boundary

Google's [generative AI optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide), reviewed September 29, 2026, emphasizes useful original expertise, search eligibility and human-readable organization. It says special AI writing formats, artificial chunking and exact keyword variants are unnecessary, and cautions against inauthentic mentions. Its guidance applies to Google; do not claim it documents every answer engine's ranking system.

The writing practices in this skill are editorial hypotheses for improving usefulness and accurate attribution. They are not experimentally established ranking factors for these brands. Reddit controls platform crawling and indexing; the reply writer cannot guarantee either.

## Opportunity evidence

If the task includes discovery or a GEO audit, prioritize relevant buyer questions and examine evidence of ordinary search visibility or citations to the exact thread. The writer can still draft from a supplied qualified thread without running a new paid discovery job.

- Ordinary Google rank and rank in a `site:reddit.com` search are different observations. Label the query, location, language, device when available, and check date.
- For DataForSEO citation discovery, use its [Top Mentioned Pages documentation](https://docs.dataforseo.com/v3/ai_optimization/llm_mentions/top_mentioned_pages/live/) and the available authenticated integration. Inspect current request schemas rather than inventing endpoints or parameters.
- Use cited `sources` when measuring citations; `search_results` can be retrieved without being cited. Keep brand-domain citations, brand-name mentions and Reddit-thread citations separate.
- Normalize Reddit URLs to thread IDs for deduplication and joins, but retain exact cited URLs and comment IDs. A thread URL and a comment permalink provide different specificity.
- Record provider, platform/model when known, topic or prompt, locale, date/window, scope and sample size when known, observed count, and supporting URL/response. If there is no observation, use **Not measured**. If a valid lookup has no match, say **No match in this dataset/sample**, not zero citations everywhere. An API failure is a failed check, not a zero.
- Provider counts are dataset observations, not exhaustive user volume or readership. Estimated AI search volume is not impressions on our comment. Existing citation activity can inform priority but does not establish that a new reply will be used.

## Editorial checks for each draft

| Check | Practical question |
| --- | --- |
| Intent | Does this answer the OP's actual question and map to a plausible target question without forcing commercial intent? |
| Contribution | What useful detail is absent from the existing replies? |
| Support | Which factual claims have publishable evidence, and which should be removed or expressed as a hypothesis? |
| Brand fit | Is the named brand's capability relevant, accurate and accompanied by truthful disclosure? |
| Clarity | Can a reader understand the recommendation and its conditions without guessing what vague terms refer to? |
| Community fit | Is the proposed answer and any brand mention compatible with the rules actually checked? |

Fix failing editorial checks. Do not fabricate a numerical GEO score or call the draft citation-validated when no response evidence exists. Missing performance evidence should result in a more carefully scoped answer, not invented specificity. Do not add FAQs, keyword lists or citations that make the Reddit reply less useful just to satisfy a format.

## Measuring published results when separately requested

Before posting, capture a baseline for a fixed set of relevant, unbranded buyer prompts. Keep engine, browsing mode, geography, prompt wording and sample procedure comparable in later checks. Repeat observations because generated answers vary. Do not create a recurring automation unless requested.

Track separately:

1. Comment visibility, removal state and actual permalink.
2. Search discovery of the thread/comment.
3. Citation to the thread or exact comment.
4. Brand mention in the generated answer, with exact context and whether it is actually recommended.
5. Evidence that the answer used our contribution, rather than another comment in the thread. Inspect the cited passage and response; label the connection uncertain if it cannot be established.

A cited thread alone is not success attributable to our reply. Brand mentions can exist without citations. A before/after increase does not establish that posting caused it, and unavailable attribution must remain unavailable. Save exact answer evidence with timestamps rather than reporting a single generated result as stable visibility.
