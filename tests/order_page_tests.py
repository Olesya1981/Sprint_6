import data
from pages.main_page import *
from conftest import *
from pages.order_page import *
import allure


class TestOrderPage:

    @pytest.mark.parametrize(
        'locator, order_data',
        [
            (MainPageLocators.UPPER_ORDER_BUTTON, data.ORDER_1),
            (MainPageLocators.BOTTOM_ORDER_BUTTON, data.ORDER_2)
        ]
    )
    @allure.title('Проверяем создание заказа через разные кнопки заказать')
    def test_order_page(self, driver, locator, order_data):
        main_page = MainPage(driver)
        driver.get(Urls.main_page_url)
        main_page.click_cookie_button()
        main_page.click_to_element_with_wait(locator)
        order_page = OrderPage(driver)
        order_page.set_order(order_data)
        assert order_page.check_order()
