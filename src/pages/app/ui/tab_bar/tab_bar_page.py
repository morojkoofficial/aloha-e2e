from typing import Optional, List

from appium.webdriver import WebElement

from src.config.config import Config
from src.pages.app.base.base_page import BasePage
from src.pages.app.ui.tab_bar.tab_bar_locators import TabBarLocators


class Tab(BasePage):
    """
    Компонента отдельной вкладки

    Наследуется от BasePage, инкапсулирует взаимодействия с одной вкладкой
    """

    def __init__(self, element: WebElement, driver, config):
        """
        Инициализирует объект вкладки

        Args:
            element (WebElement): WebElement, представляющий вкладку
            driver: Экземпляр Appium WebDriver
            config: Объект конфигурации с информацией о платформе
        """
        super().__init__(driver, config)
        self._element = element

    def get_title(self) -> str:
        """
        Получает заголовок вкладки

        Returns:
            str: Текст заголовка вкладки из атрибута "label"
        """
        return self._element.get_attribute("label")

    def close(self):
        """
        Закрывает вкладку, кликая по кнопке закрытия внутри элемента вкладки
        """
        close_button = self._find_element_in(self._element, TabBarLocators.CLOSE_TAB)
        self._click(close_button)

    def is_active(self) -> bool:
        """
        Проверяет, активна ли вкладка

        Returns:
            bool: Активность вкладки
        """
        return self._element.get_attribute("selected") == "true"


class TabBar(BasePage):
    """
    Панель вкладок браузера. Отвечает за действия с вкладками
    Наследуется от BasePage и использует локаторы из TabBarLocators
    """

    def __init__(self, driver, config: Config):
        super().__init__(driver, config)

    def get_tabs(self) -> List[Tab]:
        """
        Возвращает список всех вкладок, найденных в панели вкладок
        """
        tabs_elements = self._find_elements(TabBarLocators.TAB)
        tabs = [Tab(el, self._driver, self._config) for el in tabs_elements]
        return tabs

    def get_current_tab(self) -> Optional[Tab]:
        """
        Возвращает текущую активную вкладку
        """
        tabs = self.get_tabs()
        for tab in tabs:
            if tab.is_active():
                return tab
        raise RuntimeError("Активная вкладка не найдена")