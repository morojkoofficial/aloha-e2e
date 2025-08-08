# E2E Тесты для Aloha Browser (macOS)

Автоматизированные E2E тесты на Python с использованием:
- `pytest` — фреймворк для тестирования;
- `Appium` — автоматизация приложения;
- `Appium-Python-Client` - клиентская библиотека Appium для Python;
- `Playwright` — для работы с страницами;
- `pytest-html` — отчёты тестов.

---

## Структура проекта
```
.
├── .venv/                  # Виртуальное окружение Python
├── reports/                # HTML-отчёты
├── src/                   
│   ├── config/             # Конфигурации и настройки
│   │   ├── enums/         
│   │   ├── caps.py         # Capabilities для Appium/WebDriver
│   │   ├── config.py       # Загрузка конфигурации
│   │   ├── constants.py    # Константы проекта
│   │   ├── settings.py     # Глобальные настройки
│   │   └── timeouts.py     # Таймауты ожиданий
│   │
│   ├── pages/              
│   │   ├── app/            # POM для приложения
│   │   │   ├── base/       # Базовый класс POM приложения
│   │   │   ├── core/       # Логика взаимодействия с приложением
│   │   │   └── ui/         
│   │   └── web/            # POM для страниц
│   │
│   ├── utils/              # Утилиты и вспомогательные модули
│   │   ├── process_check.py  
│   │   └── wait_helpers.py   
├── tests/                  
├── conftest.py             # Общие фикстуры для Pytest
├── pytest.ini              # Конфигурация Pytest      
└── README.md          

```
## Установка Appium и драйвера Mac2
- Установленное приложение **Aloha Browser**
- Запущенный **Appium-server** с установленным драйвером `mac2`
- Доступ в `System Preferences → Security & Privacy → Accessibility`:
  - Terminal (или IDE)
  - Appium
---

## Запуск тестов
### 1. Установка зависимостей
#### Requirements
- Python 3.13
- pip
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Запуск
Закрыть Aloha браузер если он был открыт, запущен Appium-server
```bash
pytest -o platform=mac -m smoke
```

TODO:
- Очищение приложений (переустановка)
- Подключение windows тестов
- Подключить парсинг логов --enable-logging и --log-net-log и их проверку после теста
- ...
