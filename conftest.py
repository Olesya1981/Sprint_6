import pytest
from selenium import webdriver
@pytest.fixture
def driver():
    options = webdriver.FirefoxOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()