from dataclasses import dataclass

from selenium.webdriver.common.by import By


@dataclass
class MainPageLocators:
    sign_in_button = (By.XPATH, "//a[contains(.,'Sign in')]")