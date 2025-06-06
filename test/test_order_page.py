import pytest
import allure
from pages.order_page import OrderPage
from pages.main_page import MainPage
from data import ORDER_1_DATA, ORDER_2_DATA, ORDER_PAGE_URL
from locators.order_page_locators import OrderPageLocators as OPL


@allure.title("Тесты на проверку кнопок заказа и оформления заказа")
class TestOrderPage:

    @allure.title("Проверка верхней кнопки Заказать")
    def test_upper_order_button(self, driver):
        order_page = MainPage(driver)
        order_page.open_main_page_url()
        order_page.click_upper_order_button()
        assert order_page.get_url() == ORDER_PAGE_URL, f'Верхняя кнопка заказать ведёт на: {order_page.get_url()}'

    @allure.title("Проверка нижней кнопки Заказать")
    def test_lower_order_button(self, driver):
        order_page = MainPage(driver)
        order_page.open_main_page_url()
        order_page.click_lower_order_button()
        assert order_page.get_url() == ORDER_PAGE_URL, f'Нижняя кнопка заказать ведёт на: {order_page.get_url()}'

    @allure.title("Проверка мастера создания заказов")
    @pytest.mark.parametrize(
        'order_data, period, color', 
        [
        (ORDER_1_DATA, OPL.RENTAL_PERIOD_SET_3_DAYS, OPL.GREY_COLOR_CHECKBOX), 
        (ORDER_2_DATA, OPL.RENTAL_PERIOD_SET_7_DAYS, OPL.BLACK_COLOR_CHECKBOX)
        ])
    def test_order_wissard(self, driver, order_data, period, color):
        order_page = MainPage(driver)
        order_page.open_main_page_url()
        order_page.click_upper_order_button()
        order_page = OrderPage(driver)
        order_page.accept_cockie()
        order_page.fill_firstname_field(order_data['firstname'])
        order_page.fill_surname_field(order_data['surname'])
        order_page.fill_city_field(order_data['city'])
        order_page.drop_down_subway_station(order_data['substation'])
        order_page.fill_telephone_field(order_data['telephone'])
        order_page.click_next()
        order_page.fill_delivery_date_field(order_data['date'])
        order_page.click_rental_period(period)
        order_page.click_color(color)
        order_page.fill_comment_field(order_data['comment'])
        order_page.click_finish_order()
        order_page.click_yes()
        order_created = order_page.confirm_order_created_window()
        assert order_created == 'Посмотреть статус', f'order_created value is {order_created}'
