import allure
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.redirects_page_locators import RedirectsPageLocators
from data import MAIN_PAGE_URL


class RedirectPage(BasePage):

# Переход на страницу

    @allure.step("Переход на страницу")
    def open_main_page_url(self):
        self.go_to_url(MAIN_PAGE_URL)


# Набор кликов 

    @allure.step("Клик по лого Яндекса")
    def click_ya_logo(self):
        self.click(RedirectsPageLocators.YA_LOGO_LOCATOR)    

    @allure.step("Клик по лого Самоката")
    def click_smkt_logo(self):
        self.click(RedirectsPageLocators.SAMOKAT_LOGO_LOCATOR)    


# Проверка URL после перехода

    @allure.step("Определение текущей страницы после клика по лого Самоката")
    def get_url_for_smkt_logo(self):
        return self.get_url()

    @allure.step("Определение текущей страницы после клика по лого Яндекса")
    def get_url_for_ya_logo(self):
        return self.get_url()


# Дополнительные проверки

    @allure.step("Получение всех открытых вкладок")
    def get_all_tabs_list(self):
        return self.driver.window_handles

    @allure.step("Переход на крайнюю справа вкладку")
    def switch_to_tab(self, tab):
        self.driver.switch_to.window(tab)

    @allure.step("Ожидаем загрузку страницы Яндекса и появление попапа")
    def wait_for_ya_page_download(self, driver):
        self.wait_for_about_blank(driver)
        self.wait_for_presence(driver, RedirectsPageLocators.YA_PAGE_LOCATOR)
