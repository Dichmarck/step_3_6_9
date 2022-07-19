import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption("--language", action="store", default="ru",
                     help="Choose language: en, ru, fr, etc...")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        print("\nStarting chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        print("\nstarting firefox browser for test..")
        firefox_profile = webdriver.FirefoxProfile()
        firefox_profile.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(firefox_profile=firefox_profile)

    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser

    print("\nQuit browser after test..")
    browser.quit()


