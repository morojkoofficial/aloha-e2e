from appium.webdriver.common.appiumby import AppiumBy

from src.config.enums.platforms import Platform


class TabBarLocators:
    """
    Локаторы для элементов панели вкладок браузера
    Используются в Page Object `TabBar`

    Атрибуты:
        CLOSE_TAB (dict[Platform, tuple]): Локаторы вкладки
        CLOSE_TAB (dict[Platform, tuple]): Локаторы кнопки закрытия вкладки
    """
    TAB = {
        Platform.MAC: (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTab'),
        Platform.WINDOWS: (AppiumBy.ACCESSIBILITY_ID, "...")
    }
    CLOSE_TAB = {
        Platform.MAC: (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton'),
        Platform.WINDOWS: (AppiumBy.ACCESSIBILITY_ID, "...")
    }