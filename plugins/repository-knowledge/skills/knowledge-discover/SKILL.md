---
name: knowledge-discover
description: Understand or prepare an existing repository, resume an unfinished investigation, or investigate a knowledge gap during delivery. Publish supported product and engineering explanations with routes to code and tests. Use knowledge-maintain to update established knowledge after a known change.
---

# Knowledge Discover

Investigate the user's scope and publish what the evidence supports. Preparation also establishes where an agent should start and what work can be verified. This skill does not implement application changes or take ownership of the surrounding delivery workflow.

Read [publication rules](../../references/publication.md) before publishing. For preparation, read [repository integration](../../references/repository-integration.md). For unfinished work or resumption, read [continuity](../../references/continuity.md). Resolve resource links relative to this skill directory. Write generated documents in the repository being investigated.

## Start from the request

Identify the requested capability and intended outcome from the request and available task context. Read applicable instructions and the knowledge index, if present, then follow relevant documentation, implementation, and tests. Use repository search to fill gaps. Missing instructions or an index are starting conditions to handle, not prerequisites the user must supply.

State an inferred focus briefly when useful and proceed with independent investigation. Do not interview the user about routine filenames, search methods, or internal structures. Keep unrelated application work and documentation out of scope.

## Understand or prepare

Trace concrete behavior from its user-facing entry point through relevant implementation and tests. Inspect dependencies when they affect that behavior. Explain product purpose before implementation; do not infer product intent from code alone.

Reuse or correct a suitable existing page. Connect scattered material through navigation; create pages only for missing explanations. Publish supported findings during discovery—no separate Maintain invocation is needed. Group related findings and questions so the user can make necessary decisions together.

For preparation, add or update short host instructions and knowledge navigation. Find setup prerequisites and verification commands in repository evidence, run relevant available checks within scope, and record actual results and limits. An assessment may be complete while the environment still has a setup blocker; state the outcome requested and achieved. Missing dependencies do not themselves authorize installation or application fixes.

## Resume

Read the Markdown record and relevant published knowledge first. Check Git status, relevant diffs, and supporting sources, including uncommitted changes. Recheck affected conclusions, then continue the next unresolved action immediately. Do not recap or restart the whole investigation unless asked.

If no record exists, use available task context and evidence; ask only for context necessary to proceed. When conclusions are published and remaining work has a durable home, remove completed records and update incoming links according to the continuity rules.

## Investigate during delivery

Retain the original request and its existing issue or delivery document. Investigate the specific gap, distinguishing current implementation, confirmed requirements, and the proposed change. Do not replace the delivery task with repository-wide preparation or make application changes under this skill's authority.

Inspect available evidence before asking about intent. Present related decisions together with what is established, what remains unresolved, and what each choice changes. Continue independent work while answers are pending. Incorporate resolved answers into published explanations without a separate answer archive.

When the user explicitly asks whether existing behavior should remain, code and tests establish current behavior, not acceptance of that product decision. You may recommend preserving it, but label the recommendation as a proposal and keep the requested decision open until confirmed. Group it with related unresolved choices rather than silently narrowing the user's options.

Save only necessary unfinished context when a question remains or the session is pausing. Link remaining implementation work to its existing owner; create a delivery note only if necessary to avoid losing the request.

## Finish

Review claims against inspected sources, check references, and preserve existing useful content. Report complete, partial, or blocked for the requested scope with document links, checks actually run, and specific remaining actions. Do not imply merged, deployed, tested, or ready without evidence.
