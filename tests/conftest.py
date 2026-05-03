from __future__ import annotations

import pytest
from support import REPO_ROOT


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption(
        "--run-live-api",
        action="store_true",
        default=False,
        help="run tests that require external APIs, credentials, or network access",
    )


def pytest_collection_modifyitems(config: pytest.Config, items: list[pytest.Item]) -> None:
    if config.getoption("--run-live-api"):
        return

    skip_live_api = pytest.mark.skip(reason="needs --run-live-api to enable external API tests")
    for item in items:
        if "live_api" in item.keywords:
            item.add_marker(skip_live_api)


@pytest.fixture
def repo_root():
    return REPO_ROOT