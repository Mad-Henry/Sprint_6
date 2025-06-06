import pytest
from pages.main_page import MainPage
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()
