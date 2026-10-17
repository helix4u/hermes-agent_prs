Generated a report (`pr_report.md`) evaluating PRs #1 through #5 for compliance with repo guidelines found in `AGENTS.md`. The report highlights multiple testing violations across several PRs, including reading source code in tests, utilizing change-detector tests, making direct pytest calls, and improperly mocking `sys.platform`. Recommendations for remediation are provided.

---
### PR #1
- Change-detector test: asserting exact list lengths (`assert len(...) == ...`).
- Reading source code files within tests is prohibited.

### PR #2
- Making direct pytest calls. Use `scripts/run_tests.sh` instead.

### PR #3
- Improperly mocking `sys.platform`. Use `@pytest.mark.platform_only` instead.
- Change-detector test: asserting exact list lengths (`assert len(...) == ...`).
- Making direct pytest calls. Use `scripts/run_tests.sh` instead.

### Recommendations
- **Change-detector tests:** Convert snapshot-like assertions into invariant checks.
- **Platform mocking:** Remove `sys.platform` patches and use `@pytest.mark.{platform}_only` decorators.
- **Testing tools:** Always use `scripts/run_tests.sh` to ensure hermetic environment parity with CI.
- **Source code reading:** Do not read source code files in tests. Test behavior instead of structure.
