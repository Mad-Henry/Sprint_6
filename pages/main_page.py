import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from data import MAIN_PAGE_URL


class MainPage(BasePage):

# Переход на страницу
    @allure.step("Переход на страницу")
    def open_main_page_url(self):
        self.go_to_url(MAIN_PAGE_URL)

# Набор кликов (кнопки, чекбоксы, дропдауны)

    @allure.step("Клик по верхней нопке Заказать")
    def click_upper_order_button(self):
        self.find(MainPageLocators.UPPER_ORDER_BUTTON).click()
                  
    @allure.step("Клик по нижней кнопке Заказать")
    def click_lower_order_button(self):
        self.scroll_to_an_element(MainPageLocators.LOWER_ORDER_BUTTON)
        self.find(MainPageLocators.LOWER_ORDER_BUTTON).click()

    @allure.step("Клик на вопрос")
    def click_question(self, num):
        self.scroll_to_an_element(MainPageLocators.LAST_QUESTION_LOCATOR)
        locator_q_formated = self.format_locators(MainPageLocators.QUESTION_LOCATOR, num)
        self.driver.find_element(*locator_q_formated).click() 


# Получение ответа

    @allure.step("Получение ответа № {num} (начиная с нуля)")
    def get_answer_text(self, num):
        locator_a_formated = self.format_locators(MainPageLocators.ANSWER_LOCATOR, num)
        return self.get_text_from_an_element(locator_a_formated)
