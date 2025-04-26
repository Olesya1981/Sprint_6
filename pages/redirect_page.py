from pages.base_page import *
import allure

class RedirectPage(BasePage):

    @allure.step('Кликаем на кнопку с лого')
    def click_logo_button(self, button):
        self.click_to_element(button)

    @allure.step('Получаем текст из элемента')
    def element_text(self, text):
        element_text = self.get_text_from_element(text)
        return element_text

    @allure.step('Проверяем редирект')
    @allure.title('Кликаем на лого, переходим на другую страницу, проверяем переход через элемент')
    def check_redirect(self, data):
        self.click_logo_button(data['button'])
        self.go_to_next_window()
        return self.element_text(data['element_text'])
