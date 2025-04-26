import allure
import data
from conftest import *
from pages.order_page import *
from pages.redirect_page import RedirectPage


class TestRedirect:

    @pytest.mark.parametrize(
        'redirect_data',
        [
            data.redirect_dzen,
            data.redirect_logo
        ]
    )
    @allure.title('Проверяем редирект по клику на лого')
    def test_check_redirect(self, driver, redirect_data):
        driver.get(redirect_data['url'])
        redirect_page = RedirectPage(driver)
        assert redirect_page.check_redirect(redirect_data)
