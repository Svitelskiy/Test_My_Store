import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    b = webdriver.Chrome(executable_path="C:\\Users\\admin\\PycharmProjects\\"
                                         "Test_My_Store\\chromedriver_win32\\chromedriver.exe")
    b.get("https://automationpractice.com/index.php?id_category=4&controller=category")
    b.implicitly_wait(5)
    yield b
    b.quit()


def user():
    return {"login": "sashko@gmail.com",
            "password": "qwe123qwer"}
