import pytest


@pytest.mark.smoke
@pytest.mark.description("ALOHA-007: Закрытие единственной вкладки")
def test_close_tab_button_closes_browser(app, main_page):
    current_tab = main_page.tab_bar.get_current_tab()
    current_tab.close()
    assert app.wait_for_browser_close(), "Браузер не закрылся после закрытия последней вкладки"