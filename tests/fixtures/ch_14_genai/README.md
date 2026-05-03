## Chapter 14 Fixtures

Keep small, deterministic artifacts here for tests that should not depend on live API calls.

- If `ch_14_genai/output/...` already contains a usable artifact, tests should prefer that file.
- If the chapter output is missing, tests should fall back to this fixture tree.