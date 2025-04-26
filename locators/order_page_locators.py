from selenium.webdriver.common.by import By

class OrderPageLocators:

    # форма для кого самокат
    NAME = [By.XPATH,".//input[@type= 'text' and @placeholder = '* Имя']"]
    ORDER_FORM = [By.XPATH, ".//div[@class ='Order_Form__17u6u']/following-sibling::input[@placeholder='* Имя']"]
    LAST_NAME = [By.XPATH, ".//input[@type= 'text' and @placeholder = '* Фамилия']"]
    ADDRESS = [By.XPATH, ".//input[@type= 'text' and @placeholder = '* Адрес: куда привезти заказ']"]
    METRO_STATION = [By.XPATH, ".//input[@tabindex ='0' and @placeholder = '* Станция метро']"]
    ACCORDION_METRO = [By.XPATH, ".//div[@class='select-search has-focus']"]
    TELEPHONE_NUMBER = [By.XPATH, ".//input[@type ='text' and @placeholder='* Телефон: на него позвонит курьер']"]
    METRO_STATION_CHOOSE = [By.XPATH, "//*[text()='{}']"]
    NEXT_PAGE_BUTTON = [By.XPATH, ".//button[text() = 'Далее']"]

    #  форма когда привезти самокат
    DATETIMEPICKER = [By.XPATH, ".//input[@type = 'text' and @placeholder = '* Когда привезти самокат']"]
    DATETIMEPICKER2 = [By.XPATH, ".//div[@class = 'react-datepicker__day react-datepicker__day--0{}']"]
    DATETIMEPICKER1 = [By.XPATH, "//*[text()='25.04.2025']"]
    RENTAL_PERIOD = [By.XPATH, ".//*[text() = '* Срок аренды']"]
    RENTAL_PERIOD_DAYS = [By.XPATH, ".//div[text() = '{}']"]
    SCOOTER_COLOUR = [By.ID, '{}']
    COMMENT_FOR_COURIER = [By.XPATH, ".//input[@type = 'text' and @placeholder='Комментарий для курьера']"]
    FINISH_ORDER_BUTTON = [By.XPATH, ".//button[@class = 'Button_Button__ra12g Button_Middle__1CSJM' and text() = 'Заказать']"]

    # кнопки подтверждения заказа
    YES_BUTTON = [By.XPATH, ".//button[@class = 'Button_Button__ra12g Button_Middle__1CSJM' and text() = 'Да']"]
    ORDER_BUTTONS = [By.XPATH, ".//div[@class = 'Order_Buttons__1xGrp']"]
    ORDER_CONFIRMED = [By.XPATH, ".//div[text() = 'Заказ оформлен']"]

    VIEW_THE_STATUS = [By.XPATH, ".//div[@class = 'Order_ModalHeader__3FDaJ' and text() = 'Заказ оформлен']"]
    VIEW_STATUS_BUTTON = [By.XPATH, ".//button[text() = 'Посмотреть статус']"]