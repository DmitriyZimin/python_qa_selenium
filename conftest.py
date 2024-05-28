import os

import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FFOptions


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="Default browser")
    parser.addoption("--url", default="http://192.168.0.160:8081/", help="Opencart base URL")
    parser.addoption("--headless", action="store_true")
    parser.addoption("--drivers", default=os.path.expanduser("~/Downloads/drivers"), help="Drivers path")


@pytest.fixture(scope="session")
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    drivers = request.config.getoption("--drivers")
    url = request.config.getoption("--url")

    if browser_name == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        service = ChromeService(executable_path=drivers + "/chromedriver")
        driver = webdriver.Chrome(service=service, options=options)
    elif browser_name == "firefox":
        options = FFOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
    else:
        driver = webdriver.Safari()

    driver.maximize_window()
    driver.fullscreen_window()

    request.addfinalizer(driver.close)

    driver.get(url)
    driver.url = url

    return driver
