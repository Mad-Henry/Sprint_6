import allure
import pytest
from pages.main_page import MainPage
from data import answers_data


@allure.title("Тесты на проверку вопрсоов")
class TestMainPage:

    @pytest.mark.parametrize('num', list(range(8))) 
    def test_questions_and_answers(self, num, driver):
        main_page = MainPage(driver)
        main_page.open_main_page_url()
        main_page.click_question(num)
        answer_value = main_page.get_answer_text(num)
        assert answer_value == answers_data[num], f'Значение answer_value: {answer_value}, answers_data: {answers_data[num]}'
