import pytest

from src.pages.app.ui.main_page import MainPage


@pytest.fixture
def main_page(driver, config):
    return MainPage(driver, config)


@pytest.fixture
def browser_with_one_page(pw_context):
    """Подготавливает браузер с одной открытой страницей"""
    url = "https://alohabrowser.com"

    page = pw_context.new_page()
    page.goto(url)
    page.wait_for_load_state("domcontentloaded")

    for p in pw_context.pages:
        if url not in p.url:
            p.close()

    return page