from src.config.constants import AppMacOs, AppWindows
from src.config.enums.platforms import Platform
from src.utils.process_check import is_process_running
from src.utils.wait_helpers import wait_until


class App:
    """
    Класс для работы с приложением в зависимости от платформы

    Атрибуты:
        config: Объект конфигурации
    """

    def __init__(self, config):
        """
        Инициализирует экземпляр класса с заданной конфигурацией

        Args:
            config: Объект конфигурации
        """
        self.config = config

    def is_running(self) -> bool:
        """
        Проверяет, запущен ли процесс приложения для текущей платформы

        Returns:
            bool: True, если процесс запущен, иначе False.

        Raises:
            ValueError: Если платформа не поддерживается
        """
        platform = self.config.platform
        if platform == Platform.MAC:
            return is_process_running(AppMacOs.APP_NAME)
        elif platform == Platform.WINDOWS:
            return is_process_running(AppWindows.APP_NAME)
        else:
            raise ValueError(f"Неподдерживаемая платформа: {platform}")

    def wait_for_browser_close(self):
        return wait_until(
            lambda: not self.is_running(),
            timeout=10,
            error_msg="Браузер не закрылся"
        )