from locators.redirect_page_locators import *


class Urls:
    main_page_url = "https://qa-scooter.praktikum-services.ru/"
    order_page_url = "https://qa-scooter.praktikum-services.ru/order"


numbers = [i for i in range(8)]

answer_texts = ['Сутки — 400 рублей. Оплата курьеру — наличными или картой.',
                'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями,'
                ' можете просто сделать несколько заказов — один за другим.',
                'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. '
                'Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли '
                'самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.',
                'Только начиная с завтрашнего дня. Но скоро станем расторопнее.',
                'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.',
                'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься '
                'без передышек и во сне. Зарядка не понадобится.',
                'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.',
                'Да, обязательно. Всем самокатов! И Москве, и Московской области.']
# OrderPage

ORDER_1 = {
    'name': 'Иван',
    'last_name': 'Иванов',
    'address': 'улица Космонавта Волкова 9, кв.125',
    'metro_station': 'Сокольники',
    'telephone': '79119565859',
    'comment': 'Тише пожалуйста',
    'date': '29',
    'colour': 'black',
    'period': 'двое суток'
}

ORDER_2 = {
    'name': 'Екатерина',
    'last_name': 'Каргопольская',
    'address': 'улица Пушкинская, 379-197',
    'telephone': '89755555575',
    'metro_station': 'Черкизовская',
    'comment': '',
    'date': '30',
    'colour': 'grey',
    'period': 'трое суток'
}

# RedirectPage
redirect_dzen = {
    'url': Urls.main_page_url,
    'button': RedirectPageLocators.YANDEX_BUTTON,
    'element_text': RedirectPageLocators.YANDEX_SEARCH_PLACEHOLDER
}

redirect_logo = {
    'url': Urls.order_page_url,
    'button': RedirectPageLocators.LOGO_BUTTON,
    'element_text': RedirectPageLocators.SCOOTER_ON_MAIN
}
