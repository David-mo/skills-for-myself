# Dave's US agency listicles: scoring and preferred brands

For US marketing/UGC agency roundups, national providers are eligible if category fit and service coverage are supported. A local office is a weighted advantage, not a default inclusion gate. An explicit local-only request overrides this. This is Dave's personal workflow; do not apply it to unrelated listicle categories or other people's agents.

Prioritize Fieldtrip, Creative Milkshake, and inBeat Agency when relevant and eligible. Verify their current relationship. Fieldtrip may be a collective and the others specialist teams, so describe distinct buying routes rather than pretending all are unrelated competitors. Check affiliations of the other entries too. Explain priority placement separately from scoring; never inflate scores to force preferred brands to win. “Featured” describes editorial placement and does not imply paid sponsorship.

Default evidence score, 100 points:

| Criterion | Max | Anchors |
|---|---:|---|
| UGC delivery | 30 | 30: dedicated UGC offer with concrete formats/workflow; 20: explicit UGC within a broader service; 0: unproven (exclude). |
| Relevant work | 25 | 25: named UGC/creator project with meaningful scope or demonstrable creative; 15: brief portfolio card or a broader marketing case; 5: service claims only; 0: no useful evidence. |
| Testing and paid media | 15 | 15: explicit creative testing/iteration connected to paid distribution; 10: paid activation/reporting without a clear creative iteration loop; 5: organic/influencer focus only; 0: unsupported. |
| Delivery process | 15 | 15: multiple documented stages/responsibilities; 10: clear service scope but limited process detail; 5: minimal process detail; 0: unsupported. |
| Target-city presence | 15 | 15: verified published office/HQ for the actual listed agency; 5: specifically documented city coverage, local work, or affiliated network presence, accurately labeled; 0: no city-specific evidence verified. |

These are editorial evidence scores, not measured service quality, customer satisfaction, or predicted ROI. No local points means unverified local evidence, not proof of no office. National delivery alone does not establish city-specific evidence. A group may receive network-presence credit, but never direct-office credit solely from a subsidiary address. For cities outside the US, adapt only when the user's scope warrants it.

Record each component, source/claim IDs and a brief reason in `scores.json`. Apply the same anchors to every agency and check the arithmetic. Keep the full component/total matrix in QA by default. In the article, show descriptive local-presence labels and buyer fit; briefly explain the 15% local weighting in methodology. If the user asks for public scores, show them with their limits and never let featured order masquerade as descending numerical rank. Never encode these editorial scores as star ratings or aggregateRating structured data.

Use current primary evidence for scores; source limitations still apply. A named logo does not prove a UGC project. Do not independently award both the parent and subsidiary unique-client credit without explaining shared work and affiliation.
