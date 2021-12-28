from locators.main_page_locators import MainPageLocators


class MainPage:
    def __init__(self, browser):
        self.browser = browser

        self.sign_in_button = self.browser.find_element(*MainPageLocators.sign_in_button)