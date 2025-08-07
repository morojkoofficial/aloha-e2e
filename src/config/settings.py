class AppiumServer:
    """
    Конфигурация подключения к Appium-server.

    Атрибуты:
        HOST (str): IP-адрес сервера Appium-server
        PORT (int): Порт, на котором запущен Appium-server.
        URL (str): Полный URL для подключения к Appium-server.
    """

    HOST = "127.0.0.1"
    PORT = 4723
    URL = f"http://{HOST}:{PORT}"


class Cdp:
    """
    Константы для подключения к браузеру через Chrome DevTools Protocol (CDP)

    Используется для удалённого подключения к уже запущенному браузеру,
    например, с параметром --remote-debugging-port, чтобы управлять вкладками
    или извлекать отладочную информацию через Playwright или другие CDP-клиенты

    Атрибуты:
        HOST (str): Хост, на котором открыт удалённый отладочный порт
        PORT (int): Порт для CDP-подключения
        URL (str): Полный URL подключения к CDP
    """

    HOST = "localhost"
    PORT = 9222
    URL = f"http://{HOST}:{PORT}"