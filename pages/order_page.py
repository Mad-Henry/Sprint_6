import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from data import ORDER_PAGE_URL


class OrderPage(BasePage):

# Переход на страницу

    @allure.step("Переход на страницу")
    def open_order_page_url(self):
        self.go_to_url(ORDER_PAGE_URL)


# Набор кликов (кнопки, чекбоксы, дропдауны)

    @allure.step("Закрытие cookie")
    def accept_cockie(self):
        self.find(OrderPageLocators.COOKIE_BUTTON)
        self.click(OrderPageLocators.COOKIE_BUTTON)

    @allure.step("Клик по Далее")   
    def click_next(self):
        self.find(OrderPageLocators.NEXT_BUTTON)
        self.click(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Выбор срока аренды {period}")   
    def click_rental_period(self, period):
        self.click(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)      
        self.click(period)

    @allure.step("Выбор цвета самоката {color}")   
    def click_color(self, color):     
        self.click(color)

    @allure.step("Нажатие на Заказать в конце мастера создания заказа")
    def click_finish_order(self):
        self.find(OrderPageLocators.FINISH_ORDER_WISSARD_BUTTON)
        self.click(OrderPageLocators.FINISH_ORDER_WISSARD_BUTTON)

    @allure.step("Нажатие на Да в окне Хотите оформить заказ?")
    def click_yes(self):
        self.find(OrderPageLocators.CONFIRM_BUTTON)
        self.click(OrderPageLocators.CONFIRM_BUTTON)


# Набор дял заполнение полей

    @allure.step("Заполнение поля Имя ({firstname})")
    def fill_firstname_field(self, firstname):
        self.wait_for_an_element_and_find_it(OrderPageLocators.FIRSTNAME_INPUT_FIELD)
        self.send_text_to_an_element(OrderPageLocators.FIRSTNAME_INPUT_FIELD, firstname)

    @allure.step("Заполнение поля Фамилия ({surname})")
    def fill_surname_field(self, surname):
        self.wait_for_an_element_and_find_it(OrderPageLocators.SURNAME_INPUT_FIELD)
        self.send_text_to_an_element(OrderPageLocators.SURNAME_INPUT_FIELD, surname)

    @allure.step("В поле адрес вносится название города ({city})")
    def fill_city_field(self, city):
        self.wait_for_an_element_and_find_it(OrderPageLocators.CITY_INPUT_FIELD)
        self.send_text_to_an_element(OrderPageLocators.CITY_INPUT_FIELD, city)

    @allure.step("Выбор станции метро ({station})")
    def drop_down_subway_station(self, station):
        input_field = self.wait_for_an_element_and_find_it(OrderPageLocators.SUBWAY_ST_INPUT_FIELD)
        input_field.click()
        input_field.send_keys(station)
        option = self.wait_for_an_element_and_find_it(OrderPageLocators.set_subway_station(station))
        option.click()

    @allure.step("Заполнение поля Телефон ({telephone})")
    def fill_telephone_field(self, telephone):
        self.wait_for_an_element_and_find_it(OrderPageLocators.TELEPHONE_INPUT_FIELD)
        self.send_text_to_an_element(OrderPageLocators.TELEPHONE_INPUT_FIELD, telephone)

    @allure.step("Заполнение поля Когда привезти ({date})")
    def fill_delivery_date_field(self, date):
        self.wait_for_an_element_and_find_it(OrderPageLocators.ARRIVAL_DATE_INPUT_FIELD)
        self.send_text_to_an_element(OrderPageLocators.ARRIVAL_DATE_INPUT_FIELD, date)        

    @allure.step("Заполнение поля Комментарий ({comment})")
    def fill_comment_field(self, comment):
        self.wait_for_an_element_and_find_it(OrderPageLocators.COMMENT_INPUT_FIELD)
        self.send_text_to_an_element(OrderPageLocators.COMMENT_INPUT_FIELD, comment)   


# Набор для считывания информации.

    @allure.step("Проверка появления Посмотреть статус, подтверждающей появление окна Заказ оформлен")
    def confirm_order_created_window(self):
        return self.get_text_from_an_element(OrderPageLocators.ORDER_STATUS_BUTTON)
