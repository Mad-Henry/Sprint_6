import allure
import pytest
from pages.main_page import MainPage
from data import answers_data


class TestMainPage:

    @allure.title("Проверка вопросов и ответов на главной странице")
    @pytest.mark.parametrize('num', list(range(8))) 
    def test_questions_and_answers_section_on_main_page(self, num, driver):
        page = MainPage(driver)
        page.open_main_page_url()
        page.click_question(num)
        answer_value = page.get_answer_text(num)
        assert answer_value == answers_data[num], f'Значение answer_value: {answer_value}, answers_data: {answers_data[num]}'
