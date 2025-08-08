import os
import time

import pytest

from src.config.caps import get_caps
from src.config.config import Config
from src.config.enums.platforms import Platform

def pytest_addoption(parser):
    """
    Регистрирует дополнительную опцию конфигурации 'platform' в pytest

    Эта опция указывает целевую платформу для выполнения тестов
    Значение по умолчанию — "mac"

    Args:
        parser: Объект парсера опций pytest, используемый для добавления ini-опций
    """
    parser.addini("platform", "Целевая платформа для выполнения тестов", default="mac")

def pytest_configure(config):
    os.makedirs("reports", exist_ok=True)
    ts = time.strftime("%Y%m%d-%H%M%S")
    config.option.htmlpath = f"reports/report-{ts}.html"

@pytest.fixture(scope="session")
def config(pytestconfig) -> Config:
    """
    Фикстура конфигурационного объекта для всей сессии
    """
    platform_str = pytestconfig.getini("platform").lower()

    try:
        platform_enum = Platform(platform_str)
    except ValueError:
        raise ValueError(f"Неподдерживаемая платформа: {platform_str}")

    return Config(platform=platform_enum,
                  options=get_caps(platform_enum))

