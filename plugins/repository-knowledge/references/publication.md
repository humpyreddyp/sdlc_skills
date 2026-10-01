# Publishing repository knowledge

Use existing documentation conventions. Keep each explanation in one authoritative place and link from other pages. Avoid empty sections, duplicate product descriptions, or a parallel knowledge system.

## Explain behavior and implementation

A small knowledge index can also serve as the product overview: explain what the product does, who uses it, a typical journey supported by evidence, and routes to capabilities. Do not invent users, rationale, or requirements when evidence is absent.

A capability page normally explains purpose, behavior, rules or examples needing elaboration, implementation flow, and relevant limits. Omit sections that add nothing. Create a shared engineering page only when it avoids repeating an explanation across capabilities.

Use a behavior table with these meanings; adapt labels to repository conventions:

| ID | Condition or trigger | Behavior | Code and tests |
| --- | --- | --- | --- |
| Stable identifier | When this applies | Actor/system action and observable result | Inspected paths and symbols; identify what each referenced test checks |

Preserve IDs when wording or row order changes. Never reuse an ID for unrelated behavior. Place references beside supported claims. Use links that resolve from the page and identify symbols or tests; line numbers alone can drift.

## Evidence and prose

| Source | What it establishes |
| --- | --- |
| Inspected implementation | What examined code does under stated conditions |
| Existing test | What that test is written to check |
| Executed check | What passed, failed, or could not run in the recorded environment |
| Confirmed requirement | Intended behavior, with its source |
| Proposed change | Work considered or implemented, without claiming it already exists |

State conflicts rather than choosing intent without evidence. Name missing evidence or unavailable conditions precisely. Do not invent test results, reasons for behavior, completion, or deployment status.

Write concrete subjects, actions, conditions, and results. Define unfamiliar terms on first use. Explain why a referenced file or test matters. Add examples when rules or exceptions would otherwise be unclear. Avoid vague assurances and repetition.

Before publication, compare claims to inspected evidence, verify paths/symbols and links, check terminology, and ensure each paragraph adds information. Supported understanding belongs here; unresolved next actions belong in a minimal investigation record. Human answers become part of the explanation, not a separate default transcript or answer store.
