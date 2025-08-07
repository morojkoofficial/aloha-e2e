import time

from selenium.common import WebDriverException


def wait_until(condition_fn, timeout=10, poll_interval=0.5, error_msg="Ошибка ожидания"):
    """
    Ожидает выполнения условия в течение заданного времени

    Функция вызывает переданную функцию-условие `condition_fn` с заданной периодичностью (poll_interval),
    пока она не вернёт True или не истечёт таймаут. Если условие не выполнено вовремя — выбрасывается TimeoutError

    Args:
        condition_fn (Callable[[], bool]): Функция, возвращающая True, когда условие выполнено
        timeout (float, optional): Максимальное время ожидания в секундах. По умолчанию 10
        poll_interval (float, optional): Интервал между повторными проверками в секундах. По умолчанию 0.5
        error_msg (str, optional): Сообщение для исключения, если условие не выполнено. По умолчанию "Ошибка ожидания"

    Returns:
        bool: True, если условие выполнено в течение таймаута

    Raises:
        TimeoutError: Если условие не было выполнено в течение указанного времени
    """

    end_time = time.time() + timeout

    while time.time() < end_time:
        try:
            if condition_fn():
                return True
        except WebDriverException:
            pass

        time.sleep(min(poll_interval, end_time - time.time()))

    raise TimeoutError(error_msg)