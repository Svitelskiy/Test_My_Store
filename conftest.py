import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome(executable_path="C:\\Users\\admin\\PycharmProjects\\"
                                               "Test_My_Store\\chromedriver_win32\\chromedriver.exe")
    browser.get("http://automationpractice.com/index.php?id_category=4&controller=category")
    browser.implicitly_wait(5)
    yield browser
    browser.quit()
