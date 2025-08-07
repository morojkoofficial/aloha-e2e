import pytest

from src.pages.app.ui.main_page import MainPage


@pytest.fixture
def main_page(driver, config):
    return MainPage(driver, config)


@pytest.fixture(autouse=True)
def browser_with_one_page(pw_context):
    """Подготавливает браузер с одной открытой страницей"""
    url = "https://alohabrowser.com"

    page = pw_context.new_page()
    page.goto(url)

    for page in pw_context.pages:
        if url not in page.url:
            page.close()

    return page