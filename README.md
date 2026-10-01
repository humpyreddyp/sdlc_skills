# Repository Readiness and Knowledge Management

An installable plugin that helps people and AI prepare an existing repository, publish supported product and engineering knowledge, resume investigations, and keep knowledge current after changes.

**Status: implemented; Codex evaluated; Claude behavioral evaluation blocked by missing authentication.** Target hosts are **Codex and Claude Code**. Structural validation, installation, and changed-version updates passed in both hosts. Claude behavior and cross-host continuation remain unverified. See the [installation guide](docs/installation.md) and [evaluation results](docs/evals/results.md) for evidence and limitations. No release or push has been performed.

The plugin contains two skills:

- **Knowledge Discover:** understand or prepare a repository, resume an investigation, and investigate a gap during delivery; publish supported findings directly.
- **Knowledge Maintain:** update published knowledge after a change.

Skill instructions and resources are shared across hosts. Generated knowledge and investigation records belong in the repository being investigated. The installation guide covers installation, update, invocation, and removal for both hosts.

## Design and evaluation documents

| Saved document | Purpose | Source |
| --- | --- | --- |
| [AI SDLC overview](docs/design/ai-sdlc-overview.md) | Overall promise and four connected areas | [Source Page](https://chatgpt.com/space/page_bf0e0412a6448191882216af183595bc) |
| [Repository Readiness and Knowledge Management — V1](docs/design/repository-readiness-and-knowledge-management-v1.md) | Capabilities, evidence, continuity, integration, packaging, and authorized scope | [Source Page](https://chatgpt.com/space/page_c2ad846136688191ab39d7d8b916036c) |
| [Evaluation plan](docs/evals/plan.md) | Expected outcomes, isolated host runs, comparisons, and reporting | Derived from the V1 Page and the user's repository handoff |

The Pages were read through the Pages tools on 2026-10-01 and left unchanged. The overview preserves its source content with a link correction. The V1 document incorporates the handoff's two-host, packaging, creator-skill, and evaluation requirements; its final section lists the changes.

Repository supplied by the user: [humpyreddyp/sdlc_skills](https://github.com/humpyreddyp/sdlc_skills). The inspected local checkout initially contained only `.git`, had no commits or repository-specific instructions, and had no Git remote configured. Saving these documents does not verify or alter the remote repository.

## Small preparation example

The evaluated fixture is a tiny Python task-list repository with a command-line entry point, a task module, standard-library tests, and a short README containing setup instructions. A user can add a nonempty task, list tasks, and mark an existing task complete. Blank titles and missing task IDs are rejected.

Starting files include `tasklist/cli.py`, `tasklist/tasks.py`, `tests/test_tasks.py`, and `README.md`, with no agent instructions or knowledge index. The fixture is small enough that a reviewer can inspect its full implementation and tests.

User request: **“Prepare this repository for Codex and Claude Code to work on task completion. Explain the current behavior, point me to the relevant code and tests, and report whether the existing checks run.”**

Expected documents in the fixture repository:

| Document | What the user can inspect |
| --- | --- |
| `AGENTS.md` and `CLAUDE.md` | Short routes to the same knowledge index, existing setup instructions, relevant checks, and unfinished-investigation location |
| `docs/knowledge/index.md` | A concise product overview and links from task completion to the capability explanation |
| `docs/knowledge/capabilities/task-completion.md` | Current completion behavior, stable behavior IDs, conditions, observable results, and inspected function/test references |
| `docs/knowledge/readiness.md` | Requested scope, prerequisites, exact checks actually run, results, and any limitations |

Reuse and link the README's working instructions. Add no investigation record if the scope is resolved. If intent cannot be established, publish supported findings and save only the necessary open question and next action under `docs/work/investigation/`.

Inspect the [actual Codex preparation run](evals/runs/E1-codex-plugin-r1-1/), including its before/after snapshots, generated host instructions, capability explanations, and actual check output. This is one preparation example; the evaluation plan reuses isolated variants for the other required cases. The implemented fixture lives in `evals/fixtures/tasklist/`; execution artifacts are kept outside the installed plugin.

## Implementation and validation

The user authorized implementation and evaluation after reviewing the saved design. The original design remains the preserved baseline; its first-handoff stop boundary has now been satisfied.

- [Install, update, invoke, and remove in both hosts](docs/installation.md)
- [Evaluation results and outstanding limitations](docs/evals/results.md)
- [Knowledge Discover](plugins/repository-knowledge/skills/knowledge-discover/SKILL.md)
- [Knowledge Maintain](plugins/repository-knowledge/skills/knowledge-maintain/SKILL.md)

Build a local distributable with `python3 scripts/package.py`. The archive contains shared skills, their resources, and both host manifests; it excludes fixtures and evaluation records. It is a local build, not a published release.
