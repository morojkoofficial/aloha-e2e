from dataclasses import dataclass

from appium.options.common import AppiumOptions

from src.config.enums.platforms import Platform
from src.config.timeouts import DEFAULT_TIMEOUT

@dataclass(frozen=True)
class Config:
    """
    Общая конфигурация для тестов
    """
    platform: Platform
    options: AppiumOptions
    timeout: int = DEFAULT_TIMEOUT
