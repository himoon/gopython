## Test Structure

This repository is chapter-first and script-first, so the default test strategy stays simple:

1. Compile every `step*.py` file to catch syntax and parser errors.
2. Run only the scripts that should terminate locally without user input or external APIs.
3. Mark real API scripts with `@pytest.mark.live_api` so they are opt-in.

### Conventions

- Keep tests chapter-local when possible.
- Prefer subprocess execution over custom import loaders.
- Mark any real API tests with `@pytest.mark.live_api`. They stay skipped unless `pytest --run-live-api` is used.