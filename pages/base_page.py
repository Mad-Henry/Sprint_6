from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wdwait = WebDriverWait(driver, 10)

    def go_to_url(self, url, suffix=''):
        self.driver.get(url + suffix)

    def find(self, locator):
        return self.driver.find_element(*locator)

    def wait_for_an_element_and_find_it(self, locator):
        self.wdwait.until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)
    
    def click(self, locator):
        self.wait_for_an_element_and_find_it(locator).click()

    def send_text_to_an_element(self, locator, text):
        self.wait_for_an_element_and_find_it(locator).send_keys(text)

    def get_text_from_an_element(self, locator):
        return self.wait_for_an_element_and_find_it(locator).text

    def scroll_to_an_element(self, locator):
        element = self.wdwait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def format_locators(self, locator_x, num):
        method, locator = locator_x
        locator = locator.format(num)
        return [method, locator]
    
    def get_url(self):
        return self.driver.current_url    
    