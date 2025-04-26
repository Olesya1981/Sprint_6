from selenium.webdriver.common.by import By

class RedirectPageLocators:

    LOGO_BUTTON = [By.CLASS_NAME, "Header_LogoScooter__3lsAR"]
    UPPER_ORDER_BUTTON = [By.CLASS_NAME, 'Button_Button__ra12g']
    YANDEX_BUTTON = [By.CSS_SELECTOR, "[alt='Yandex']"]
    YANDEX_SEARCH_BUTTON = [By.XPATH, ".//button[@class='arrow__button' and text() = 'Найти']"]
    CLOSE = [By.XPATH, ".//span[@aria-label='Закрыть']"]
    FRAME_BROWSER = [By.XPATH, ".//div[@class='h1a22e094']"]
    YANDEX_SEARCH_BUTTON_2 = [By.XPATH, "//button[@class = 'arrow__button' and @type= 'submit']"]
    DZEN_HEADER = [By.ID, "//*[@id='dzen-header']"]
    YANDEX_SEARCH_PLACEHOLDER = [By.XPATH,
                                 ".//div[@class='dzen-search-arrow-common__placeholder' and text() = 'Поиск Яндекса']"]
    SCOOTER_ON_MAIN = [By.CLASS_NAME, "Home_Header__iJKdX"]
    COOKIE_BUTTON = [By.ID, "rcc-confirm-button"]
