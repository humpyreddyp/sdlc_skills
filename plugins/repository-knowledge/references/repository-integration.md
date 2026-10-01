# Integrating repository knowledge

Read existing guidance and documentation first. Reuse suitable explanations and working instructions; fix relevant inaccuracies against evidence, preserve unrelated content, and add navigation when discoverability is the problem.

Use `AGENTS.md` for Codex and `CLAUDE.md` for Claude Code in the investigated repository. Follow requested host scope and existing nested conventions. For both-host preparation, use two short entry points pointing to the same ordinary Markdown knowledge and working instructions. Do not duplicate detailed explanations between host files or overwrite unrelated rules. The plugin installation is not the target repository.

Each entry point should route to the knowledge index, pages relevant to the request, implementation and tests linked from those pages, existing setup/verification commands, and the unfinished-investigation location when needed.

Use existing locations if suitable. Otherwise start with `docs/knowledge/index.md`, `docs/knowledge/capabilities/<capability>.md`, and, only if needed, `docs/work/investigation/<question>.md`. Create `docs/knowledge/engineering/<topic>.md` only for a shared explanation. Existing issues or delivery documents remain the owners of application changes.

A readiness result states requested scope, inspected source/working-tree context, environment prerequisites, commands actually executed and their results, and missing access or checks. Reuse an existing readiness or working document where appropriate. Link to maintained setup instructions instead of creating a second command list.

Preparation can assess readiness without making the environment ready. Relevant checks are within scope when authorized and available; missing setup does not automatically authorize dependency installation, application fixes, test-infrastructure changes, pushing, merging, deployment, or release. Respect already granted authorization and report only actions still needing it.
