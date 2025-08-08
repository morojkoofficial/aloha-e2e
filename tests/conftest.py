import pytest

from appium import webdriver
from appium.webdriver.client_config import AppiumClientConfig

from playwright.sync_api import sync_playwright
from selenium.common import WebDriverException

from src.config.settings import AppiumServer, Cdp
from src.pages.app.core.app import App


@pytest.fixture(scope="function")
def driver(config):
    """
    Фикстура для инициализации и управления сессией Appium WebDriver

    Создаёт подключение к удалённому Appium-серверу с заданной конфигурацией,
    предоставляет объект `driver` для взаимодействия с приложением,
    а после завершения теста закрывает сессию

    Args:
        config: объект с настройкам

    Yields:
        Appium WebDriver (webdriver.Remote): активная сессия Appium для управления приложением
    """

    try:
        client_config = AppiumClientConfig(
            remote_server_addr=AppiumServer.URL,
            direct_connection=True,
            keep_alive=False,
            ignore_certificates=True
        )

        driver = webdriver.Remote(
            options=config.options,
            client_config=client_config
        )

        yield driver

        driver.quit()
    except WebDriverException as e:
        pytest.fail(f"Не удалось создать сессию Appium: {e}")


@pytest.fixture(scope="session")
def app(config):
    """
    Фикстура для работы с приложением в зависимости от платформы
    """
    return App(config)


@pytest.fixture(scope="function")
def pw_context(driver):
    """
    Фикстура подключается к уже запущенному браузеру через CDP
    и возвращает первый доступный контекст браузера.
    """
    with sync_playwright() as pw:
        browser = pw.chromium.connect_over_cdp(Cdp.URL)
        try:
            if not browser.contexts:
                raise RuntimeError("Нет доступных контекстов в браузере")
            context = browser.contexts[0]
            yield context
        finally:
            browser.close()