import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store',
                     default='en', help='Choose language: ru or en-gb')


@pytest.fixture(scope='function')
def browser(request):
    # user_language = request.config.getoption("language")
    # browser = None
    # options = Options()
    # options.add_experimental_option(
    #     'prefs', {'intl.accept_languages': user_language})

    # browser = webdriver.Chrome(options=options)
    browser = webdriver.Firefox()
    browser.maximize_window()

    yield browser
    print('\nquit browser..')
    # time.sleep(20)
    browser.quit()
