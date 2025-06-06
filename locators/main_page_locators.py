from selenium.webdriver.common.by import By


class MainPageLocators:
    
    # Локаоры "Заказать"
    UPPER_ORDER_BUTTON = [By.XPATH, "//button[@class='Button_Button__ra12g']"]
    LOWER_ORDER_BUTTON = [By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]

    # Локаторы вопросов и ответов
    QUESTION_LOCATOR = [By.XPATH, "//div[@id='accordion__heading-{}']"]
    ANSWER_LOCATOR = [By.XPATH, "//div[@id='accordion__panel-{}']/p"]
    LAST_QUESTION_LOCATOR = [By.XPATH, "//div[@id='accordion__heading-7']"]