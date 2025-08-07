import psutil

def is_process_running(app_name):
    """
    Проверка процесса с указанным именем
    Перебирает все активные процессы и ищет совпадение по имени

    Args:
        app_name (str): Название процесса

    Returns:
        bool: Если процесс запущен - True, иначе False
    """

    for process in psutil.process_iter(['name']):
        if app_name.lower() in process.info['name'].lower():
            return True
    return False
