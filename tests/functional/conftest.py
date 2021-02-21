import pytest

from tests.functional.utils import build_chrome


@pytest.yield_fixture(scope="session", autouse=True)
def browser():
    _browser = build_chrome()
    # _browser = build_firefox()

    yield _browser
    _browser.close()
    _browser.quit()