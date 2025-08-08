from typing import List, Union, Tuple, Dict

from appium.webdriver import WebElement
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.config.config import Config
from src.config.enums.platforms import Platform
from src.config.timeouts import DEFAULT_TIMEOUT


class BasePage:
    """
    Базовый класс для всех Page Object
    Содержит общие методы для взаимодействия с элементами интерфейса через Appium WebDriver
    """

    def __init__(self, driver, config: Config):
        """
        Инициализирует страницу с переданным Appium WebDriver

        Args:
            driver: Экземпляр Appium WebDriver
            config: Общая конфигурация
        """
        self._driver = driver
        self._config = config

    def _get_locator(self, platform_locators: dict[Platform, tuple]) -> tuple:
        """
        Возвращает локатор для текущей платформы

        Args:
            platform_locators (dict): Словарь соответствия платформе - локатору.

        Returns:
            tuple: Локатор (by, value) для текущей платформы.

        Raises:
            KeyError: Если для текущей платформы локатор не указан
        """
        try:
            return platform_locators[self._config.platform]
        except KeyError:
            raise KeyError(f"Локатор не назначен для платформы: {self._config.platform}")

    def _find_element(self, platform_locators: Dict[Platform, Tuple[str, str]],
                      timeout: int = DEFAULT_TIMEOUT) -> WebElement:
        """
        Ожидает появления элемента, соответствующего локатору текущей платформы,
        и возвращает первый найденный элемент.

        Args:
            platform_locators (dict): Словарь {Platform: (by, value)} с локаторами для платформ.
            timeout (int): Максимальное время ожидания в секундах.

        Returns:
            WebElement: Первый найденный элемент.

        Raises:
            TimeoutException: Если элемент не найден за указанное время.
            KeyError: Если локатор для текущей платформы не назначен.
        """
        by, value = self._get_locator(platform_locators)

        try:
            element = WebDriverWait(self._driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
            return element
        except TimeoutException:
            raise TimeoutException(f"Элемент не найден ({by}, '{value}')")

    def _find_elements(self, platform_locators: dict, timeout: int = DEFAULT_TIMEOUT) -> List[WebElement]:
        """
        Ожидает появления хотя бы одного элемента, соответствующего локатору текущей платформы,
        и возвращает список всех найденных элементов

        Args:
            platform_locators (dict): Словарь {Platform: (by, value)} с локаторами для платформ
            timeout (int): Максимальное время ожидания в секундах

        Returns:
            List[WebElement]: Список найденных элементов

        Raises:
            TimeoutException: Если ни один элемент не найден за указанное время
            KeyError: Если локатор для текущей платформы не назначен
        """
        by, value = self._get_locator(platform_locators)

        try:
            WebDriverWait(self._driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
            elements = self._driver.find_elements(by, value)
            return elements
        except TimeoutException:
            raise TimeoutException(f"Элементы не найдены ({by}, '{value}')")

    def _find_element_in(self, parent_element: WebElement, platform_locators: dict, timeout: int = DEFAULT_TIMEOUT) -> WebElement:
        """
        Ожидает и возвращает первый найденный элемент внутри другого элемента
        """
        by, value = self._get_locator(platform_locators)

        try:
            element = WebDriverWait(self._driver, timeout).until(
                lambda driver: parent_element.find_element(by, value)
            )
            return element
        except TimeoutException:
            raise TimeoutException(f"Элемент не найден внутри родителя ({by}, '{value}')")

    def _click(
            self,
            target: Union[dict, Tuple[str, str], WebElement],
            timeout: int = DEFAULT_TIMEOUT
    ):
        """
        Кликает по элементу. Аргумент может быть:

        - словарь {Platform: (by, value)} — локаторы по платформам
        - кортеж (by, value) — конкретный локатор
        - WebElement — уже найденный элемент

        Args:
            target (dict|tuple|WebElement): локатор или элемент для клика
            timeout (int): время ожидания кликабельности (для локатора)
        """
        if isinstance(target, dict):
            by, value = self._get_locator(target)
            try:
                element = WebDriverWait(self._driver, timeout).until(
                    EC.element_to_be_clickable((by, value))
                )
            except TimeoutException:
                raise TimeoutException(f"Элемент не кликабелен ({by}, '{value}')")
        elif isinstance(target, tuple):
            by, value = target
            try:
                element = WebDriverWait(self._driver, timeout).until(
                    EC.element_to_be_clickable((by, value))
                )
            except TimeoutException:
                raise TimeoutException(f"Элемент не кликабелен ({by}, '{value}')")
        elif isinstance(target, WebElement):
            element = target
        else:
            raise TypeError(f"Неподдерживаемый тип аргумента: {type(target)}")

        element.click()

    def _wait_for_element(self, platform_locators: dict, timeout: int = DEFAULT_TIMEOUT) -> WebElement:
        """
        Ожидает появления и видимости элемента, выбранного по текущей платформе

        Args:
            platform_locators (dict): Словарь {Platform: (by, value)} с локаторами для платформ
            timeout (int, optional): Максимальное время ожидания в секундах. По умолчанию DEFAULT_TIMEOUT

        Returns:
            WebElement: Найденный и видимый элемент

        Raises:
            TimeoutException: Если элемент не найден или не виден за указанное время
            KeyError: Если локатор не определён для текущей платформы
        """
        by, value = self._get_locator(platform_locators)
        try:
            return WebDriverWait(self._driver, timeout).until(
                EC.visibility_of_element_located((by, value))
            )
        except TimeoutException as e:
            raise TimeoutException(f"Элемент не найден или не виден ({by}, '{value}')") from e
