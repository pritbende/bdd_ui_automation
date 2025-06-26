from selenium.webdriver.common.by import By

from features.page_objects.BasePage import BasePage


class AccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    edit_your_account_info_link_text = "Edit your account information"

    def display_status_of_edit_your_account_info(self):
        return self.is_displayed(By.LINK_TEXT, self.edit_your_account_info_link_text)