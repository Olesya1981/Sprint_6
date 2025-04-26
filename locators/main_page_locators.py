from selenium.webdriver.common.by import By

class MainPageLocators:

    COOKIE_BUTTON = [By.ID, "rcc-confirm-button"]

    # вопросы о важном
    QUESTION_LOCATOR = [By.ID, "accordion__heading-{}"]
    ANSWER_LOCATOR = [By.ID, "accordion__panel-{}"]
    QUESTION_TO_SCROLL = [By.ID, 'accordion__heading-7']

    # Кнопки заказать
    UPPER_ORDER_BUTTON = [By.CLASS_NAME, 'Button_Button__ra12g']
    BOTTOM_ORDER_BUTTON = [By.XPATH, ".//button[@class = 'Button_Button__ra12g Button_Middle__1CSJM' and text() = 'Заказать']"]
