class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, by, locator_value):
        self.driver.find_element(by, locator_value).click()

    def send_keys(self, by, locator_value, text):
        self.driver.find_element(by, locator_value).send_keys(text)

    def is_displayed(self, by, locator_value):
        return self.driver.find_element(by, locator_value).is_displayed()

    def get_text(self, by, locator_value):
        return self.driver.find_element(by, locator_value).text