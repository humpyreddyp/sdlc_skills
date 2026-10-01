# Repository Readiness and Knowledge Management — V1

Implementation was authorized by the user on 2026-10-01 after this baseline was saved. The original first-handoff status and boundary below are retained as design history; see [current results](../evals/results.md) and [installation guidance](../installation.md) for implementation status.

Source: [Repository Readiness and Knowledge Management — V1](https://chatgpt.com/space/page_c2ad846136688191ab39d7d8b916036c). Retrieved through Pages on 2026-10-01; source sequence 19, last updated 2026-10-01T14:16:14.761907Z. The source Page is unchanged.

Local adaptation: the user's repository handoff takes precedence over the source Page for host support, packaging, required creator tools, evaluation, and the current handoff boundary. See [changes from the source Pages](#changes-from-the-source-pages).

V1 provides two skills that help AI agents find their way around an existing repository, document how the system works, resume unfinished investigations, and update documentation after changes.

This document is for the person reviewing the design and the AI implementing it. The skill packages will contain the instructions needed during use.

**Status: draft for review. Implementation has not been authorized.**

## Document guide

| Section | What it defines |
| - | - |
| **1. Purpose and scope** | What Repository Readiness and Knowledge Management produce, and what V1 excludes. |
| **2. Capabilities, skills, and interaction** | The four capabilities, which skill handles each, and when the user participates. |
| **3. Published knowledge and writing standards** | Document layout, behavior tables, code references, and writing rules. |
| **4. Investigation and continuity** | What is saved for unfinished work, how another session resumes it, and when records are removed. |
| **5. Repository integration and authority** | Where instructions go, how existing documentation is reused, and which changes the skills may make. |
| **6. Execution mechanisms and supporting tools** | How searches, checks, working data structures, and model settings support the capabilities. |
| **7. Scenarios and validation** | The demonstrations and checks used to verify the skills. |
| **8. Packaging, use, and handoff** | What must be delivered, how the skills are invoked, and what happens after this design is approved. |

## 1. Purpose and scope

| Area | What V1 creates or updates |
| - | - |
| **Repository Readiness** | Repository instructions telling an agent where to start; an index linking product capabilities to their documentation, with routes to code and tests; setup and verification commands with their prerequisites; and a report of which commands ran, their results, and what prevented others from running. |
| **Knowledge Management** | A product overview describing who uses the product and what they do; capability pages containing behavior tables with stable IDs, conditions, and expected results; explanations linking those behaviors to code files, functions, and tests. These documents are corrected when the implementation or confirmed requirements change. |

Repository Readiness tells an agent **where to look and how to work**. Knowledge Management explains **what the system does and how the code produces that behavior**.

V1 works on the capabilities named or implied by the user’s request. The skills reuse existing documentation, add missing instructions and pages, and check claims against code, tests, and human input.

V1 excludes creating a new application, implementing application changes, managing changes through review and release, reorganizing unrelated repository files, running background monitoring, and coordinating simultaneous investigations.

## 2. Capabilities, skills, and interaction

V1 has four capabilities and two skills:

- **Knowledge Discover** investigates and publishes understanding. It also prepares repository instructions and navigation when requested.

- **Knowledge Maintain** updates published knowledge after a change.

A scenario is a concrete use of one of these capabilities. The scenarios used to test V1 appear in section 7.

| Capability | Skill | Interaction with the user | Result |
| - | - | - | - |
| **Understand or prepare a repository** | **Knowledge Discover** | Interpret the request and propose the relevant focus areas. Investigate available sources. Present related findings and questions together. | Product and capability explanations with code and test references. For preparation requests, also provide navigation, working instructions, and verification results. |
| **Resume an investigation** | **Knowledge Discover** | Read saved progress, check relevant source changes, and continue immediately. Recap only when asked. Ask questions when a decision is needed. | Additional published findings and an updated investigation record, or removal of the record when the investigation is finished. |
| **Investigate a gap during delivery** | **Knowledge Discover** | Investigate the question within the original request. Present related findings and decisions together without replacing the delivery task. | Publish supported findings as they become available. Save unresolved questions only when needed to continue the investigation. |
| **Update knowledge after a change** | **Knowledge Maintain** | Make updates supported by the change and its evidence. Then show a short summary and links. Ask before resolving ambiguity that would change the documented requirement or expand the request. | Corrected explanations, behavior tables, code references, and navigation. Report when no update is needed. |

Knowledge Discover publishes its findings directly. The user does not need to invoke Knowledge Maintain afterward.

### When to involve the user

Ask when available sources cannot establish intent, when sources disagree about a requirement, or when the next action would expand the authorized work.

Each question should explain:

- What the investigation established.

- What remains undecided.

- What the available choices would change.

Group related questions so the user can answer them together. Continue work that does not depend on unanswered questions.

Do not ask the user to choose routine file names, search methods, or internal data structures unless those choices conflict with repository conventions or an explicit preference.

Incorporate resolved answers into the appropriate explanation. Do not separately save interview transcripts or human answers by default.

## 3. Published knowledge and writing standards

Published knowledge is the shared reference for people and AI agents. It contains supported explanations, rather than a transcript of how those explanations were discovered.

### Documents and layout

| Document | Contents |
| - | - |
| **Knowledge index and product overview** | What the product does, who uses it, a typical user journey, and links to capability pages. These can share one page while the content is small. |
| **Capability page** | Purpose, behaviors, rules, examples, implementation flow, code and test references, and any limits a reader must know. |
| **Shared engineering page** | An explanation needed by several capability pages. Create one when it avoids repeating the same explanation. |
| **Repository working instructions** | Setup prerequisites, commands for running the application and relevant checks, and links to more detailed existing instructions. |
| **Readiness result** | The requested scope, checks actually performed, results, and missing setup or access. Include enough source and environment context to understand what the result applies to. |

A capability page normally follows this order:

1. What the capability does and who uses it.

2. Its behavior table.

3. Rules, examples, and exceptions that need further explanation.

4. How the implementation produces the behavior.

5. Relevant limits and supporting references.

Omit sections that add no information. Place references next to the claims they support rather than repeating them in several sections.

### Behavior tables

| Column | Required content |
| - | - |
| **ID** | A stable identifier for one behavior. |
| **Condition or trigger** | When the behavior applies. |
| **Behavior** | The actor or system action and its observable result. |
| **Code and tests** | Relevant file paths, symbols, and tests, with short descriptions where their role is not obvious. |

Preserve IDs when rows move or wording changes. Do not assign an existing ID to an unrelated behavior.

A **behavior** states what happens. A **rule** states a condition or constraint governing what happens. Put a rule in the behavior row when it fits; explain it separately when several behaviors depend on it.

### Evidence and uncertainty

Code references must point to inspected files and symbols. Test references must identify what the test checks.

Keep these distinctions explicit:

| Evidence | What it establishes |
| - | - |
| **Inspected implementation** | What the examined code does under the stated conditions. |
| **Existing test** | What the test is written to check. |
| **Executed test** | What passed or failed in the recorded run. |
| **Confirmed requirement** | What the product is intended to do. |
| **Proposed change** | What is being considered or implemented, without implying it already happens. |

When implementation and confirmed requirements disagree, state the disagreement. Do not rewrite one as though it proves the other.

Do not describe a working-branch change as merged or deployed without evidence. Do not invent reasons for existing behavior.

Published pages may identify a boundary in what is known. The investigation record holds the open questions and actions needed to resolve it.

### Writing standards

| Rule | How to apply it |
| - | - |
| **Name the subject and action.** | State who or what acts, under which conditions, and with what result. |
| **Use specific nouns and verbs.** | Replace phrases such as “handles appropriately” with the action the system performs. |
| **Explain purpose before implementation.** | Establish what the reader is trying to understand before introducing files, functions, or infrastructure. |
| **Define unfamiliar terms.** | Explain domain terms and acronyms on first use. Use each term consistently afterward. |
| **Explain references.** | Tell the reader why a file, function, or test matters. |
| **Avoid repetition.** | Keep an explanation in one place and link to it elsewhere. |
| **Use examples when needed.** | Add an example when a condition, exception, or sequence would otherwise remain unclear. |
| **State limits precisely.** | Name the missing evidence or unverified condition instead of using a general confidence disclaimer. |

Before publication, check that the explanation matches the evidence, references resolve, terminology is consistent, and each paragraph adds information.

## 4. Investigation and continuity

Resolved understanding belongs in published knowledge. Unfinished investigation context belongs in a work record.

### Suggested layout

Generated knowledge and investigation records belong in the repository being investigated, never in the plugin installation. Follow existing repository conventions where they already provide suitable locations. Otherwise, start with:

```
docs/
├── knowledge/
│   ├── index.md
│   ├── capabilities/
│   │   └── <capability>.md
│   └── engineering/
│       └── <shared-topic>.md
└── work/
    ├── investigation/
    │   └── <question>.md
    └── delivery/
        └── <change>.md
```

Create directories only when they contain needed documents.

`work/delivery/` is optional. If an existing issue tracker or delivery document already owns the requested change, link to it.

### Investigation record

Use one Markdown file per connected investigation. It should contain:

| Field | What to save |
| - | - |
| **Question and scope** | What needs to be established and which part of the repository is involved. |
| **Relevant progress** | Findings and checks needed to avoid repeating work, with links to published conclusions. |
| **Open questions** | What remains unresolved and which actions depend on it. |
| **Next actions** | What the next session should inspect, run, or ask. |
| **Source context** | Relevant paths, revision information, or uncommitted changes needed to recheck earlier findings. |
| **Related work** | Links to the delivery request or other records needed to continue. |

The Markdown file is the saved state. V1 does not require a separate YAML or JSON state file.

Update it when an unresolved question changes, a next action changes, or the session is about to pause. Do not record every search or message.

### Resuming

The skill reads the investigation record, follows relevant knowledge links, and checks whether the sources supporting earlier findings have changed.

It then continues from the next unresolved action. It does not repeat the full investigation or give a recap unless requested.

If no record can be found, use available task context and repository evidence. Ask for missing context only when it is necessary to proceed.

### Removing completed records

An investigation record can be removed when:

- Its useful conclusions have been published.

- Remaining implementation work is recorded or linked elsewhere.

- No unfinished task depends on information found only in that record.

- Incoming links have been updated.

No separate archive is required by default. Repository history retains prior versions.

## 5. Repository integration and authority

### Repository instructions

Use the instruction file recognized by the intended host: `AGENTS.md` for Codex and `CLAUDE.md` for Claude Code. Follow existing repository conventions. When preparing for both hosts, keep their entry points brief and route them to the same repository knowledge and working instructions.

Keep it short. It should tell an agent:

- Where the knowledge index is.

- How to find documentation, code, and tests for the requested capability.

- Where setup and verification commands are documented.

- Where unfinished investigations are stored.

- To read the pages relevant to the request.

Keep detailed product explanations in knowledge pages. Preserve unrelated repository instructions.

### Existing documentation

Inspect existing documents before adding new ones.

Correct or extend the current document when it already serves the purpose. Add an index or links when the main problem is navigation. Create a new page when the topic has no suitable home.

If two documents disagree, inspect their sources before choosing which statement to publish.

### Allowed changes

Within a request to discover, prepare, or maintain knowledge, the skills may inspect sources, run relevant checks, and create or update documentation and navigation.

Preparation identifies missing setup, access, or checks. It does not automatically authorize dependency installation, application fixes, or changes to test infrastructure. Perform those only when already authorized; otherwise report the specific work needed.

Editing repository documents does not itself authorize pushing commits, merging changes, deploying, or releasing.

## 6. Execution mechanisms and supporting tools

### Capability implementation

The capability names below match section 2.

| Capability | Mechanisms and intended use | Practical implementation |
| - | - | - |
| **Understand or prepare a repository** | Establish the focus, inspect existing entry points, gather evidence, and publish the findings. | Read existing instructions and documentation. Search relevant code and tests. Create missing guidance and an index as findings are published. Run relevant checks for preparation requests and record their results. |
| **Resume an investigation** | Restore necessary context and recheck evidence affected by changes. | Read the Markdown record and linked pages. Inspect Git status, relevant diffs, and affected sources. Continue the next unresolved action and update the record. |
| **Investigate a gap during delivery** | Answer the question without losing the original request. | Search the relevant implementation, inspect or run focused tests, and group questions requiring human input. Publish established findings and save only unfinished investigation context. |
| **Update knowledge after a change** | Identify affected pages and reconcile them with the changed system. | Inspect the supplied change or Git diff. Follow code and behavior references to related pages. Update explanations, preserve IDs, check links, and report the edits or that no edits were needed. |

### Starting conditions

| Repository condition | What the skill does |
| - | - |
| **No guidance or knowledge index** | Inspect existing files and documentation. Publish findings for the requested scope, create an index, and add instructions pointing to it. |
| **Guidance and knowledge already exist** | Use them to locate relevant sources, check the claims affected by the request, and update the existing documents. |
| **Some documents exist, but navigation is missing** | Connect existing documents through an index and repository instructions. Add content only where the investigation identifies a missing explanation. |

The skill does not require the user to create the documentation structure first. It also does not create empty pages for every possible topic.

### Shared tools and mechanisms

| Mechanism | Intended use | V1 implementation |
| - | - | - |
| **Selective reading** | Avoid loading unrelated repository content. | Read the index and relevant pages, then inspect the code and tests needed for the question. Load skill templates and detailed references only when needed. |
| **Search and navigation** | Locate implementation and dependencies. | File search, `rg`, and symbol navigation when available. Follow dependencies when they affect the behavior being investigated. |
| **Change inspection** | Identify evidence that needs rechecking. | Git status and diffs plus direct source inspection. Account for uncommitted changes; a commit identifier alone is insufficient. |
| **Verification** | Check documented behavior and working commands. | Existing repository commands and focused checks. Record what actually ran and what the result establishes. |
| **Grouped questions** | Resolve related decisions together. | Present findings, remaining questions, and choices in one group. Use clickable options when the host supports them. |
| **Publication checks** | Catch unsupported claims and broken references. | Review prose against inspected evidence and check referenced paths, symbols, and links. Add a small script if repeated checks justify it. |
| **Continuity records** | Support a fresh session. | Markdown investigation records containing the information specified in section 4. |
| **Model settings** | Match reasoning effort to the task. | Start with the host’s configured model. Recommend a stronger model for unresolved synthesis or conflicting evidence, or a lighter model for bounded extraction when appropriate. |
| **Context management** | Preserve progress as sessions grow. | Use available host context and usage features, read selectively, and save continuation context at meaningful checkpoints. |

### Internal working structures

The skill may maintain small temporary lists or maps during execution.

| Structure | Contents | Purpose |
| - | - | - |
| **Scope and progress** | Requested focus, active questions, completed checks, and next actions. | Prevent repeated work and unrelated investigation. |
| **Evidence map** | Findings or behavior IDs connected to code, tests, and conflicting evidence. | Support publication and identify what to recheck after changes. |
| **Publication plan** | Findings assigned to existing pages or necessary new pages. | Avoid duplicate explanations and missed updates. |

These structures can live in the current working context or in a helper’s ordinary data objects. They are not a second saved knowledge base.

Persist their results as follows:

- Supported understanding goes into knowledge pages.

- Necessary continuation context goes into investigation records.

- Temporary maps are discarded when no longer needed.

- Human answers are incorporated into the relevant explanation without a separate answer archive.

Start with Markdown, repository search, Git, and existing checks. Add a rebuildable cache or other helper only if actual use shows repeated work that it would remove.

Measure efficiency through repeated reads, context use, and completion time. Check those gains against missed dependencies, unsupported claims, and failed resumption.

## 7. Scenarios and validation

Use isolated copies and variants of one small repository fixture to demonstrate the four capabilities in both Codex and Claude Code. Define expected outcomes before running evaluations and keep expected answers separate from executing sessions. The detailed cases and reporting method are in the [evaluation plan](../evals/plan.md).

| Capability | Demonstration | Required evidence |
| - | - | - |
| **Understand or prepare a repository** | Request preparation for work on one capability. Run once without established knowledge and once with existing documentation. | Focus matches the request. Instructions and navigation lead to the right pages, code, and tests. Published claims have supporting references. Readiness results identify checks run and missing prerequisites. |
| **Resume an investigation** | Stop with an unresolved question, change a relevant source, and continue in a fresh session. | The new session uses the saved record, notices the relevant change, rechecks affected findings, and continues without repeating unrelated work. |
| **Investigate a gap during delivery** | Introduce a question about a rule during a requested change. | The original task remains identifiable. Available evidence is investigated before questions are asked. Supported findings are published, and unfinished work can be resumed. |
| **Update knowledge after a change** | Change a documented behavior, update the knowledge, and run maintenance again. | Affected explanations and references are corrected. Behavior IDs remain stable where the behavior retains its identity. The second run makes no unnecessary edits. |
| **Conflicting evidence or unavailable checks** | Introduce a conflict between requirements, implementation, and a test, and separately make a relevant check unavailable. | The agent identifies the conflicting sources or missing prerequisite, publishes only supported findings, and does not invent intent, test results, or completion. |

### Publication and usability checks

Verify that:

- A reader can move from the product overview to a capability, its behavior, and its implementation.

- Code and test references resolve.

- Statements distinguish current implementation, confirmed intent, proposed changes, and unknowns.

- Verification reports identify which checks actually ran.

- Existing useful documentation and unrelated instructions remain intact.

- Completed investigations can be removed without losing conclusions or continuation context.

### Completion reporting

At the end of an invocation, state:

| Status | Meaning |
| - | - |
| **Complete** | The requested scope has been satisfied. |
| **Partial** | Some requested work is finished; name what remains and its next action. |
| **Blocked** | A required action cannot proceed; name the missing input, access, or prerequisite. |

Include links to changed documents and any remaining investigation record.

A completed preparation request may identify a setup blocker; assessing readiness does not necessarily mean making the repository ready. The result must state which outcome the request required and which was achieved.

Validate the skills behaviorally in both Codex and Claude Code, including fresh-session continuation within each host and between hosts in both directions. Inspect the resulting artifacts and observed behavior rather than grading exact wording or heading matches. File structure checks alone do not establish that invocation, questions, publication, and resumption work.

Record host and model information, inputs, outputs, pass/fail results, and failures. Measure elapsed time and token usage where available; explicitly mark unavailable measurements. Compare representative runs with and without the plugin under comparable conditions. Fix demonstrated failures and rerun affected evaluations. Do not claim validation for a host that was not tested.

Keep fixtures, expected answers, execution records, and evaluation reports separate from resources loaded during ordinary skill use. Model evaluations begin only after implementation is authorized.

## 8. Packaging, use, and handoff

### Deliverables

| Deliverable | Contents |
| - | - |
| **Knowledge Discover skill** | Instructions for preparation, investigation, publication, and resumption. |
| **Knowledge Maintain skill** | Instructions for identifying and updating knowledge affected by a change. |
| **Supporting resources** | Flexible templates, writing rules, and only the helpers justified by validation. |
| **Repository integration instructions** | How to add or update guidance, navigation, and work-record locations. |
| **Demonstration repository and results** | Repeatable demonstrations of the four capabilities, including fresh-session continuation. |
| **Installation and usage guide** | Installation, update, invocation, and removal instructions for both Codex and Claude Code; expected outputs and known limitations. |

V1 must be an installable plugin supporting both Codex and Claude Code. Maintain each skill's instructions and shared resources in one place; add host-specific metadata and instructions only where required. Test the actual packaged skills in both hosts before claiming support has been validated.

### Required creation tools

Use Codex's installed `skill-creator` skill to create and revise both Knowledge Discover and Knowledge Maintain. Use its `scripts/quick_validate.py` on each completed or revised skill. Use Codex's installed `plugin-creator` skill for Codex packaging and its `scripts/validate_plugin.py` before handing back the package. Read the installed creator instructions when implementation begins, and report a missing creator rather than silently substituting another workflow.

Both creator skills and their validation scripts were found and read during this design handoff. No initializer, scaffold, validator for a plugin, installation, or model evaluation has been run in this phase.

### Packaging decision and official requirements

Official requirements were checked on 2026-10-01. OpenAI documents a portable root `plugin.json` and continued support for `.codex-plugin/plugin.json` as a compatibility fallback; the installed creator still generates that supported Codex form. Skills sit at the plugin root under `skills/`. [OpenAI packaging documentation](https://developers.openai.com/plugins/build/plugins)

Claude Code uses `.claude-plugin/plugin.json` for manifest metadata and discovers `skills/<name>/SKILL.md` at the plugin root. Referenced components must remain inside the plugin. Its manifest validation command is `claude plugin validate <plugin-directory>`. [Claude Code manifest reference](https://code.claude.com/docs/en/plugins-reference)

The proposed V1 layout uses the creator-generated Codex compatibility manifest and a Claude Code manifest around a single shared skills tree. A portable root manifest is not required for this choice; revisit only if the verified host requirements change before implementation. This is a design sketch, not a scaffold:

```text
plugins/
└── repository-knowledge/
    ├── .codex-plugin/plugin.json
    ├── .claude-plugin/plugin.json
    ├── skills/
    │   ├── knowledge-discover/SKILL.md
    │   └── knowledge-maintain/SKILL.md
    └── references/                 # only shared resources that are needed
docs/
├── design/
└── evals/
evals/                             # fixtures and reports; outside plugin root
```

`repository-knowledge` is the proposed package name. Codex UI metadata may live in each skill's `agents/openai.yaml`. Common writing and publication guidance should have one authoritative resource linked by both skills; capability-specific details belong with their skill. Host differences must not fork the common workflow. Do not add empty resource directories, helpers, caches, hooks, or MCP components without demonstrated need.

Keep evaluation material outside the installable plugin root and out of normal skill references. Choose and verify host-specific distribution metadata during implementation; do not alter any personal marketplace or host configuration in this phase. The eventual guide must cover fresh installation, updates and session reload behavior, explicit invocation of each skill, and removal in both hosts. Removal instructions must preserve knowledge and work records generated in target repositories.

### Everyday use

The guide should show requests such as:

- “Help me understand this repository.”

- “Prepare this repository for work on this capability.”

- “Continue this investigation.”

- “Investigate this rule as part of the current change.”

- “Update the knowledge to reflect this change.”

Users should not need to select internal data structures, search tools, or saving mechanisms.

### Handoff

The user has supplied the target repository, [humpyreddyp/sdlc_skills](https://github.com/humpyreddyp/sdlc_skills), and connected its local directory to this Codex project.

This first handoff saves the source designs with the requested updates, a README, and the evaluation plan, and proposes one small preparation example. It stops before scaffolding, implementation, installation, model evaluations, release, or push. Implementation and evaluation require the user's subsequent go-ahead.

This conversation and any approved Pages remain the place for design discussion. The repository holds the published design baseline and, after authorization, implementation and validation results. Revisions must be explicitly carried between them.

**Building the skills remains a separate, explicitly authorized step.**

### Changes from the source Pages

- The overview preserves the Page's prose and table. Its empty Page link now has a descriptive label and points to this local design.
- This V1 design replaces the Claude Code-only target with Codex and Claude Code, adds their instruction entry points, and places generated knowledge and investigation records in the investigated repository.
- It adds the shared package proposal, required creator skills and validators, current official packaging references, and installation/update/invocation/removal requirements for both hosts.
- It expands validation to isolated behavioral runs in both hosts, continuation in both directions, conflicting evidence and unavailable checks, separate expected answers, plugin/no-plugin comparisons, measurement, reporting, and failure repair.
- It updates the handoff to the supplied repository and the explicit design-only boundary. All other source design content is retained.
