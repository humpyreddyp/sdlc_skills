# Install and use Repository Knowledge

The plugin contains Knowledge Discover and Knowledge Maintain for Codex and Claude Code. Both hosts load the same skill instructions and shared resources. See the [evaluation report](evals/results.md) for what was actually tested and remaining limitations.

Use an up-to-date host that supports plugins. The tested local runtimes are Codex CLI `0.158.0-alpha.2.1` and Claude Code `2.1.285`. A host installation and authenticated model access are prerequisites for running skills. The plugin itself has no runtime dependencies, hooks, servers, or credentials.

The commands below assume this checkout is already available locally. Set `RK_REPO` to its absolute path; `RK_TARGET` is the separate repository you want to investigate. Do not point the target at the plugin installation.

```sh
RK_REPO=/absolute/path/to/sdlc_skills
RK_TARGET=/absolute/path/to/your/project
```

## Codex

Register this explicit repository marketplace and install the plugin:

```sh
codex plugin marketplace add "$RK_REPO"
codex plugin add repository-knowledge@sdlc-skills
```

Start a fresh chat in the target repository. Invoke either skill explicitly:

```text
Use $knowledge-discover to prepare this repository for work on task completion.
Use $knowledge-maintain to update published knowledge for this change.
```

If another plugin supplies the same skill name, use `$repository-knowledge:knowledge-discover` or `$repository-knowledge:knowledge-maintain`. The package keeps implicit skill discovery enabled.

For a published version update, first update your local checkout through your normal Git workflow, then reinstall with `codex plugin add repository-knowledge@sdlc-skills` and open a new chat. During local plugin development, use the installed plugin-creator's `read_marketplace_name.py --marketplace-path "$RK_REPO/.agents/plugins/marketplace.json"` and `update_plugin_cachebuster.py "$RK_REPO/plugins/repository-knowledge"` before reinstalling. The cachebuster changes the Codex manifest's build suffix; it is not a product version release. Do not hand-edit marketplace configuration for development updates.

Remove the plugin and, optionally, its now-unused marketplace:

```sh
codex plugin remove repository-knowledge@sdlc-skills
codex plugin marketplace remove sdlc-skills
```

The registered marketplace is the explicit `sdlc-skills` repository marketplace, not the automatically discovered personal marketplace. These commands follow the [official Codex packaging workflow](https://developers.openai.com/plugins/build/plugins) and the installed plugin-creator instructions.

## Claude Code

Register the local marketplace and install:

```sh
claude plugin marketplace add "$RK_REPO"
claude plugin install repository-knowledge@sdlc-skills --scope user
cd "$RK_TARGET"
claude
```

Invoke the namespaced skills in a fresh session:

```text
/repository-knowledge:knowledge-discover Prepare this repository for work on task completion.
/repository-knowledge:knowledge-maintain Update the knowledge to reflect this change.
```

For a temporary session without a persistent plugin installation, use `claude --plugin-dir "$RK_REPO/plugins/repository-knowledge"` from the target repository. The same skills are available for that session.

After updating your local checkout, refresh and update the plugin, then restart the Claude Code session:

```sh
claude plugin marketplace update sdlc-skills
claude plugin update repository-knowledge@sdlc-skills
```

Remove the plugin and, optionally, its unused marketplace:

```sh
claude plugin uninstall repository-knowledge@sdlc-skills --scope user
claude plugin marketplace remove sdlc-skills
```

Claude's manifest lives in `.claude-plugin/plugin.json`; skills live at the plugin root under `skills/`. Validate a local copy with `claude plugin validate "$RK_REPO/plugins/repository-knowledge"`. See the [official manifest reference](https://code.claude.com/docs/en/plugins-reference) and [CLI reference](https://code.claude.com/docs/en/cli-reference) for host behavior.

## Working in a repository

Discover supports understanding, preparation, resumption, and a bounded investigation during delivery. For example: “Continue the investigation in docs/work/investigation/completion.md,” or “Investigate repeated completion as part of this change.” Maintain reconciles published explanations after a known change. Discover publishes supported findings directly; Maintain is not a required follow-up.

Existing documentation and conventions take precedence over suggested locations. For a repository without guidance, preparation creates short host entry points, knowledge navigation, supported capability explanations, and readiness results. Investigation records exist only for unfinished work. Questions requiring product intent are grouped; routine implementation choices do not require an interview.

Removal affects host plugin configuration and caches. It must leave generated `AGENTS.md`, `CLAUDE.md`, knowledge pages, and investigation records in target repositories intact. Those files remain ordinary repository documents. Review or remove them separately only if you intend to change repository guidance.

## Packaging and validation for contributors

Both skills were created with Codex's built-in skill-creator, and the Codex package and marketplace were generated with plugin-creator. Use those installed creators for revisions. Run their `quick_validate.py` once for each skill, `validate_plugin.py` on `plugins/repository-knowledge`, and Claude's manifest validator. Their Python validators require PyYAML; use a virtual environment if your Python lacks it.

Run `python3 scripts/package.py` to build a local ZIP containing only the installable package. Evaluation fixtures, expected answers, logs, and reports are excluded. Packaging is not publishing or releasing. Behavioral validation uses the [evaluation plan](evals/plan.md); structural success alone does not validate a host.
