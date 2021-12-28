from locators.login_locators import LoginLocators


class LoginPage:
    def __init__(self, browser):
        self.browser = browser

        self.login_input = self.browser.find_element(*LoginLocators.email_address_input)
        self.input_password = self.browser.find_element(*LoginLocators.password_input)
        self.button_enter = self.browser.find_element(*LoginLocators.enter_button)

    def enter_valid_credentials(self, login, password):
        self.login_input.send_keys(login)
        self.input_password.send_keys(password)
        self.button_enter.click()
