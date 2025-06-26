from selenium.webdriver.common.by import By

from features.page_objects.AccounPage import AccountPage
from features.page_objects.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    email_field_name = "email"
    password_field_name = "password"
    login_button_xpath = "//input[@value='Login']"
    login_error_message_xpath = "//div[@id='account-login']/div[1]"

    def enter_email_address(self, email):
        self.send_keys(By.NAME, self.email_field_name, email)

    def enter_password(self, password):
        self.send_keys(By.NAME, self.password_field_name, password)

    def click_login_button(self):
        self.click(By.XPATH, self.login_button_xpath)
        return AccountPage(self.driver)

    def get_warning_message(self):
        return self.get_text(By.XPATH, self.login_error_message_xpath)