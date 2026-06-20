# Run Before / After Prompt

## Before

Run the task without adding the new repo context audit rules. Save the result as `before.md`.

## Context Audit

Use `checklist/repo-context-audit-checklist.md` to slim and update `AGENTS.md` or `CLAUDE.md`.

Only add rules that directly address known AI failure patterns.

## After

Run the same task again with the audited context. Save the result as `after.md`.

## Comparison

Write `comparison.md`:

- Did the output fit the repo better?
- Which context rule changed behavior?
- What still failed?
- Could the improvement come from a clearer task description instead?
- Verdict: effective / weakly effective / no effect / worse.
