from selenium.webdriver.common.by import By

from features.page_objects.BasePage import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    my_account_option_xpath = "//span[text()='My Account']"
    login_option_link_text = "Login"
    register_option_link_text = "Register"

    def click_my_account(self):
        self.click(By.XPATH, self.my_account_option_xpath)

    def select_login_option(self):
        self.click(By.LINK_TEXT, self.login_option_link_text)

    def select_register_option(self):
        self.click(By.LINK_TEXT, self.register_option_link_text)

