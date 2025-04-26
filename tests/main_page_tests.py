from data import *
from pages.main_page import *
from conftest import *
import allure


@allure.title('Проверяем соответствие ответов вопросам на главной странице')
class TestMainPageQuestions:

    @pytest.mark.parametrize(
        'num',
        numbers
    )
    def test_main_page_questions(self, driver, num):
        driver.get(Urls.main_page_url)

        main_page = MainPage(driver)
        main_page.click_question(num)
        assert main_page.get_text_answer(num) == answer_texts[num]
