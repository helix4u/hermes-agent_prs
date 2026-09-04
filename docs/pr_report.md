# PR Review Report

This report evaluates all new PRs opened since the last scheduled run for adherence to the directives in `AGENTS.md`.

## Summary of Findings

- PRs fix/oversized-context-file-fallback have no major compliance issues.
- PRs fix/bot-mode-live-local-dm, codex/fix-bot-mode-live-local-dm contain several violations of `AGENTS.md` guidelines, primarily related to testing practices.

## Detailed PR Breakdown

### PR fix/bot-mode-live-local-dm
**Important Findings / Violations:**
- **Potential change-detector test (Banned):** Contains strict equality assertions on list lengths.

### PR fix/oversized-context-file-fallback
**Important Findings / Violations:**
- **No major compliance issues found.**

### PR codex/fix-bot-mode-live-local-dm
**Important Findings / Violations:**
- **Potential change-detector test (Banned):** Contains strict equality assertions on list lengths.

## Recommendations
For the PRs with violations:
1. Replace source code inspection in tests with behavioral assertions.
2. Refactor change-detector tests into invariant assertions.
3. Replace direct `pytest` usages in CI configurations/documentation with `scripts/run_tests.sh`.
4. Remove `sys.platform` mocks in tests and use platform-specific markers (`@pytest.mark.<os>_only`) as mandated by `AGENTS.md`.
