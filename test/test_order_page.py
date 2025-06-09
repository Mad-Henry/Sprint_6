import pytest
import allure
from pages.order_page import OrderPage
from pages.main_page import MainPage
from data import ORDER_1_DATA, ORDER_2_DATA, ORDER_PAGE_URL
from locators.order_page_locators import OrderPageLocators as OPL


@allure.title("Тесты на проверку кнопок заказа и оформления заказа")
class TestOrderPage:

    @allure.title("Проверка верхней кнопки Заказать")
    def test_redirect_to_order_wissard_for_upper_order_button(self, driver):
        page = MainPage(driver)
        page.open_main_page_url()
        page.click_upper_order_button()
        assert page.get_url() == ORDER_PAGE_URL, f'Верхняя кнопка заказать ведёт на: {page.get_url()}'

    @allure.title("Проверка нижней кнопки Заказать")
    def test_redirect_to_order_wissar_for_lower_order_button(self, driver):
        page = MainPage(driver)
        page.open_main_page_url()
        page.click_lower_order_button()
        assert page.get_url() == ORDER_PAGE_URL, f'Нижняя кнопка заказать ведёт на: {page.get_url()}'

    @allure.title("Проверка мастера создания заказов")
    @pytest.mark.parametrize(
        'order_data, period, color', 
        [
        (ORDER_1_DATA, OPL.RENTAL_PERIOD_SET_3_DAYS, OPL.GREY_COLOR_CHECKBOX), 
        (ORDER_2_DATA, OPL.RENTAL_PERIOD_SET_7_DAYS, OPL.BLACK_COLOR_CHECKBOX)
        ])
    def test_order_wissard_and_order_creation(self, driver, order_data, period, color):
        page = MainPage(driver)
        page.open_main_page_url()
        page.click_upper_order_button()
        page = OrderPage(driver)
        page.accept_cockie()
        page.fill_firstname_field(order_data['firstname'])
        page.fill_surname_field(order_data['surname'])
        page.fill_city_field(order_data['city'])
        page.drop_down_subway_station(order_data['substation'])
        page.fill_telephone_field(order_data['telephone'])
        page.click_next()
        page.fill_delivery_date_field(order_data['date'])
        page.click_rental_period(period)
        page.click_color(color)
        page.fill_comment_field(order_data['comment'])
        page.click_finish_order()
        page.click_yes()
        order_created_proof = page.confirm_order_created_window()
        assert order_created_proof == 'Посмотреть статус', f'order_created value is {order_created_proof}'
