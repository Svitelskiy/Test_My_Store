from dataclasses import dataclass

from selenium.webdriver.common.by import By


@dataclass
class LoginLocators:
    email_address_input = (By.ID, "email")
    password_input = (By.ID, "passwd")
    enter_button = (By.ID, "SubmitLogin")