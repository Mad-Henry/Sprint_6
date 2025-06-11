import allure
from pages.redirects_page import RedirectPage
from data import MAIN_PAGE_URL, DZEN_URL


class TestRedirectsPage:

    @allure.title("Тест на проверку перехода по ссылкам из лого Самоката")
    def test_redirect_from_samokat_logo_to_main_page(self, driver):
        page = RedirectPage(driver)
        page.open_main_page_url()
        page.click_smkt_logo()
        smkt_redirect_url = page.get_url()
        assert smkt_redirect_url == MAIN_PAGE_URL, f'Значение smkt_redirect_url: {smkt_redirect_url}'
        
    @allure.title("Тест на проверку перехода по ссылкам из лого Яндекса")
    def test_redirect_from_yandex_logo_to_dzen_page(self, driver):
        page = RedirectPage(driver)
        page.open_main_page_url()
        page.click_ya_logo()
        tabs = page.get_all_tabs_list()
        page.switch_to_tab(tabs[-1])
        page.wait_for_ya_page_download(driver)
        ya_redirect_url = page.get_url()
        assert ya_redirect_url == DZEN_URL, f'Значение ya_redirect_url: {ya_redirect_url}'
        