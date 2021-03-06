from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import pytest


def pytest_addoption(parser):
    parser.addoption("--browser", "-B", action="store", default="chrome")
    parser.addoption("--url", "-U", action="store", default="http://localhost/")
    parser.addoption("--options", "-O", action="store", default="")


@pytest.fixture
def browser(request):
    browser_param = request.config.getoption("--browser")
    browser_options = request.config.getoption("--options")
    browser_url = request.config.getoption("--url")
    if browser_param == "chrome":
        if browser_options == 'headless':
            options = webdriver.ChromeOptions()
            options.add_argument('headless')
            driver = webdriver.Chrome(options=options)
        else:
            driver = webdriver.Chrome()
    elif browser_param == "firefox":
        if browser_options == 'headless':
            options = Options()
            options.add_argument('-headless')
            driver = webdriver.Firefox(options=options)
        else:
            driver = webdriver.Firefox()

    driver.get(browser_url)
    driver.maximize_window()
    request.addfinalizer(driver.close)
    return driver
