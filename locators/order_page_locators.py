from selenium.webdriver.common.by import By


class OrderPageLocators():
    
    # Локаторы первого шага
    FIRSTNAME_INPUT_FIELD =  [By.XPATH, "//input[@placeholder='* Имя']"]
    SURNAME_INPUT_FIELD = [By.XPATH, "//input[@placeholder='* Фамилия']"]
    CITY_INPUT_FIELD = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]
    SUBWAY_ST_INPUT_FIELD = [By.CSS_SELECTOR, ".select-search__input"]
    TELEPHONE_INPUT_FIELD = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]
    NEXT_BUTTON = [By.XPATH, "//button[text()[contains(., 'Далее')]]"]
    
    # Локаторы второго шага
    ARRIVAL_DATE_INPUT_FIELD = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    RENTAL_PERIOD_DROPDOWN = [By.XPATH, "//*[@class='Dropdown-arrow']"]
    RENTAL_PERIOD_SET_3_DAYS = [By.XPATH, "//*[@class='Dropdown-option'][3]"]
    RENTAL_PERIOD_SET_7_DAYS = [By.XPATH, "//*[@class='Dropdown-option'][last()]"]
    BLACK_COLOR_CHECKBOX = [By.XPATH, "//*[text()[contains(., 'чёрный жемчуг')]]"]
    GREY_COLOR_CHECKBOX = [By.XPATH, "//*[text()[contains(., 'серая безысходность')]]"]
    COMMENT_INPUT_FIELD = [By.XPATH, "//input[@placeholder='Комментарий для курьера']"]
    ORDER_BUTTON = [By.XPATH, ".//*[@class='Button_Button__ra12g Button_Middle__1CSJM']"]
    FINISH_ORDER_WISSARD_BUTTON = [By.XPATH, ".//*[@class='Button_Button__ra12g Button_Middle__1CSJM']"]

    # Локатор(-ы) подтверждения заказа ("Хотите оформить заказ?")
    CONFIRM_BUTTON =  [By.XPATH, "//*[text()[contains(., 'Да')]]"]

    # Локаторы окон "Заказ оформлен" и деталей заказа
    ORDER_STATUS_BUTTON = [By.XPATH, "//*[text()[contains(., 'Посмотреть статус')]]"]
    STATUS_PAGE_TEXT = [By.XPATH, "//*[text()[contains(., 'Самокат на складе')]]"]
    
    # Куки
    COOKIE_BUTTON = [By.XPATH, "//*[@id='rcc-confirm-button']"]

    # Локаторы станций из выпадающего
    @staticmethod
    def set_subway_station(station):
        return (By.XPATH, f"//button[.='{station}']")