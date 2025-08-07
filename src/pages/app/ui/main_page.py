from src.pages.app.base.base_page import BasePage
from src.pages.app.ui.tab_bar.tab_bar_page import TabBar


class MainPage(BasePage):
    def __init__(self, driver, config):
        super().__init__(driver, config)
        self.tab_bar = TabBar(driver, config)