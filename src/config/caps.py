from appium.options.mac import Mac2Options
from appium.options.windows import WindowsOptions

from src.config.constants import AppMacOs, AppWindows
from src.config.enums.platforms import Platform


def get_caps(platform: Platform):
    """
    Возвращает Appium capabilities для указанной платформы

    Args:
        platform (Platform): Перечисление из допустимых платформ

    Returns:
        AppiumOptions: Объект настроек с соответствующими capabilities
    """

    if platform == Platform.MAC:
        options = Mac2Options()
        options.set_capability("platformName", "mac")
        options.set_capability("automationName", "mac2")
        options.set_capability("bundleId", AppMacOs.BUNDLE_ID)
        options.set_capability("arguments", ["--remote-debugging-port=9222"])
        return options

    elif platform == Platform.WINDOWS:
        options = WindowsOptions()
        options.set_capability("platformName", "Windows")
        options.set_capability("app", AppWindows.EXECUTABLE)
        return options

    else:
        raise ValueError(f"Неподдерживаемая платформа: {platform}")
