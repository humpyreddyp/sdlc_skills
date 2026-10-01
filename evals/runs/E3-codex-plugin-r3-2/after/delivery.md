# Confirmation-message change

Add a friendly confirmation message when the user completes a task. Investigate repeated completion before implementing the message. Application implementation remains pending.

Current behavior and verification are documented in [task completion](docs/task-completion.md). The evidence investigation is complete; product decisions remain open in the [repeated-completion investigation](docs/work/investigation/repeated-completion.md): whether repeats should succeed, whether they should have distinct feedback, and how friendly feedback should coexist with JSON output. Proposed answers are not accepted requirements.

After those decisions are confirmed, record acceptance criteria here, implement the confirmation behavior, and verify first completion, repeated completion, output, and missing-ID handling. This document retains ownership of that pending application work.
