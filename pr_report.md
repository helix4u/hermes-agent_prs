# PR Review Report

This report evaluates all new PRs opened since the last scheduled run for adherence to the directives in `AGENTS.md`.

## Summary of Findings

- PR #3 (`fix(run_agent): recover primary client on openai transport errors`) has no major compliance issues.
- PRs #1, #2, #4, and #5 contain several violations of `AGENTS.md` guidelines, primarily related to testing practices.

## Detailed PR Breakdown

### PR #1: feat(gateway): add browser sidecar bridge and extension
**Impact:** Large architectural changes (1,292 files modified)
**Important Findings / Violations:**
- **Reading source code in tests (Banned):**
  ```typescript
  import { mkdirSync, readFileSync, writeFileSync, existsSync, readdirSync } from 'fs';
  ```
- **Potential change-detector test (Banned):** Contains strict equality assertions on list lengths.
  ```python
  assert len(tool_call_ids["terminal"]) == 2
  assert len(tool_call_ids["terminal"]) == 1
  ```
- **Change-detector test (Banned):** Asserting exact config version literals.
  ```python
  assert DEFAULT_CONFIG["_config_version"] == 11
  ```
- **Direct Pytest calls (Banned):** Direct `pytest` invocations are used instead of `scripts/run_tests.sh`.
  ```bash
  python -m pytest tests/ -q --ignore=tests/integration --ignore=tests/e2e --tb=short -n auto
  ```
- **Mocking `sys.platform` in tests (Banned):**
  ```python
  with patch("agent.skill_utils.sys") as mock_sys:
      mock_sys.platform = "linux"
  ```
  *(Tests should use `@pytest.mark.linux_only` instead of mocking sys.platform).*

### PR #2: fix(terminal): guard invalid command values
**Impact:** Large change set (1,493 files modified)
**Important Findings / Violations:**
Contains the same testing violations as PR #1:
- Uses `readFileSync` in tests.
- Contains change-detector tests (e.g., `assert len(tool_call_ids["terminal"]) == 2`, `assert DEFAULT_CONFIG["_config_version"] == 12`).
- Uses direct `pytest` calls instead of `scripts/run_tests.sh`.
- Mocks `sys.platform` in tests.

### PR #3: fix(run_agent): recover primary client on openai transport errors
**Impact:** 2 files changed, 25 insertions(+)
**Important Findings / Violations:**
- **No major compliance issues found.** The PR adds targeted error handling and uses Python mocks (`patch("run_agent.OpenAI")`) without violating `AGENTS.md` guidelines.

### PR #4: fix(run_agent): recover primary client on openai transport errors
**Impact:** Large change set (1,507 files modified)
**Important Findings / Violations:**
Contains the same testing violations as PRs #1 and #2:
- Uses `readFileSync` in tests.
- Contains change-detector tests (e.g., `assert DEFAULT_CONFIG["_config_version"] == 12`).
- Uses direct `pytest` calls instead of `scripts/run_tests.sh`.
- Mocks `sys.platform` in tests.

### PR #5: fix(send_message): deliver Matrix media via adapter
**Impact:** Large change set (1,705 files modified)
**Important Findings / Violations:**
Contains the same testing violations as PRs #1, #2, and #4:
- Uses `readFileSync` in tests.
- Contains change-detector tests (e.g., `assert raw["_config_version"] == 17`).
- Uses direct `pytest` calls instead of `scripts/run_tests.sh`.
- Mocks `sys.platform` in tests.

## Recommendations
For PRs 1, 2, 4, and 5:
1. Replace source code inspection in tests with behavioral assertions.
2. Refactor change-detector tests into invariant assertions.
3. Replace direct `pytest` usages in CI configurations/documentation with `scripts/run_tests.sh`.
4. Remove `sys.platform` mocks in tests and use platform-specific markers (`@pytest.mark.<os>_only`) as mandated by `AGENTS.md`.
