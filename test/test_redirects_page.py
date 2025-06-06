import allure
from pages.redirects_page import RedirectPage
from data import MAIN_PAGE_URL, DZEN_URL


@allure.title("Тесты на проверку переходов по ссылкам из лого")
class TestRedirectsPage:

    @allure.title("Тест на проверку перехода по ссылкам из лого Самоката")
    def test_redirect_for_samokat_logo(self, driver):
        main_page = RedirectPage(driver)
        main_page.open_main_page_url()
        main_page.click_smkt_logo()
        smkt_redirect_url = main_page.get_url()
        assert smkt_redirect_url == MAIN_PAGE_URL, f'Значение smkt_redirect_url: {smkt_redirect_url}'
        
    @allure.title("Тест на проверку перехода по ссылкам из лого Яндекса")
    def test_redirect_for_yandex_logo(self, driver):
        main_page = RedirectPage(driver)
        main_page.open_main_page_url()
        main_page.click_ya_logo()
        tabs = main_page.get_all_tabs_list()
        main_page.switch_to_tab(tabs[-1])
        main_page.wait_for_ya_page_download(driver)
        ya_redirect_url = main_page.get_url()
        assert ya_redirect_url == DZEN_URL, f'Значение ya_redirect_url: {ya_redirect_url}'
        