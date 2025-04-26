from pages.base_page import *
from locators.main_page_locators import *
import allure


class MainPage(BasePage):

    @allure.step("Кликаем на вопрос из списка")
    def click_question(self, num):
        locator_question_formatted = self.format_locator(MainPageLocators.QUESTION_LOCATOR, num)
        self.scroll_to_element(MainPageLocators.QUESTION_TO_SCROLL)
        self.click_to_element_with_wait(locator_question_formatted)

    @allure.step("Получаем текст ответа")
    def get_text_answer(self, num):
        locator_answer_formatted = self.format_locator(MainPageLocators.ANSWER_LOCATOR, num)
        return self.get_text_from_element(locator_answer_formatted)

    @allure.step("Нажимаем не кнопку ""Заказать")
    def click_order_button(self, locator):
        self.click_to_element(locator)

    @allure.step('Нажимаем кнопку куки')
    def click_cookie_button(self):
        self.click_to_element_with_wait(MainPageLocators.COOKIE_BUTTON)