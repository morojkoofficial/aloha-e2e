from playwright.sync_api import Page


class BaseWebPage:
    """
    TODO: В будущее, если будет необходимо управлять именно страницей

    Базовый класс для всех страниц Playwright

    Оборачивает Page и предоставляет удобные методы для поиска,
    ожидания и взаимодействия с элементами
    """

    def __init__(self, page: Page):
        self.page = page

    def get_url(self):
        """
        Возвращает текущий URL страницы

        Возвращает:
            str: Текущий URL страницы
        """
        return self.page.url

    def goto(self, url):
        """
        Переходит на указанную страницу

        Args:
            url (str): URL страницы, на которую нужно перейти
        """
        self.page.goto(url)

    def close(self):
        """
        Закрывает текущую страницу

        Закрывает текущую страницу, после чего нельзя будет использовать
        объект Page
        """
        self.page.close()
