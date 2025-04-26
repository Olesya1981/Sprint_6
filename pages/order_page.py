from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import *
from conftest import *
from locators import *
from locators.order_page_locators import *
from data import *
import allure
class OrderPage(BasePage):

    @allure.step('Заполняем форму заказа данными из словаря')
    def set_order(self, data):
        # для кого самокат
        self.add_text_to_element(OrderPageLocators.NAME, data['name'])
        self.add_text_to_element(OrderPageLocators.LAST_NAME, data['last_name'])
        self.add_text_to_element(OrderPageLocators.ADDRESS, data['address'])
        self.click_to_element(OrderPageLocators.METRO_STATION)
        self.click_to_element_with_wait(self.format_locator(OrderPageLocators.METRO_STATION_CHOOSE, data['metro_station']))
        self.add_text_to_element(OrderPageLocators.TELEPHONE_NUMBER, data['telephone'])
        self.click_to_element(OrderPageLocators.NEXT_PAGE_BUTTON)
        # когда привезти самокат
        self.click_to_element_with_wait(OrderPageLocators.DATETIMEPICKER)
        self.click_to_element_with_wait(self.format_locator(OrderPageLocators.DATETIMEPICKER2, data['date']))
        self.click_to_element(OrderPageLocators.RENTAL_PERIOD)
        self.click_to_element(self.format_locator(OrderPageLocators.RENTAL_PERIOD_DAYS, data['period']))
        self.click_to_element(self.format_locator(OrderPageLocators.SCOOTER_COLOUR, data['colour']))
        self.add_text_to_element(OrderPageLocators.COMMENT_FOR_COURIER, data['comment'])
        self.click_to_element(OrderPageLocators.FINISH_ORDER_BUTTON)
        self.click_to_element(OrderPageLocators.YES_BUTTON)

    @allure.step('Получаем текст элемента')
    def check_order(self):
        return self.get_text_from_element(OrderPageLocators.ORDER_CONFIRMED)

    @allure.step('Нажимаем кнопку подтверждения заказа')
    def click_yes_button(self):
        self.driver.find_element(OrderPageLocators.YES_BUTTON).click()

    @allure.step("Нажимаем кнопку куки")
    def click_cookie_button(self):
        self.click_to_element(OrderPageLocators.COOKIE_BUTTON).click()





