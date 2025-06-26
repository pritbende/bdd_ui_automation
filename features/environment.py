import os

import allure
from selenium import webdriver

from utilities import ConfigReader


def before_scenario(context, scenario):
    print(f"Starting scenario: {scenario.name}")
    browser_name = ConfigReader.read_config("info", "browser")
    if browser_name.__eq__("chrome"):
        context.driver = webdriver.Chrome()
    elif browser_name.__eq__("firefox"):
        context.driver = webdriver.Firefox()
    else:
        print(f"Invalid browser type {browser_name}")
    context.driver.maximize_window()
    context.driver.get(ConfigReader.read_config("info", "url"))

def after_scenario(context, scenario):
    context.driver.quit()

def after_step(context, step):
    if step.status == 'failed':
        # screenshot_path = f"screenshots/{step.name.replace(' ', '_')}.png"
        # os.makedirs("screenshots", exist_ok=True)
        # context.driver.save_screenshot(screenshot_path)
        # print(f"[FAILED STEP] Screenshot saved to: {screenshot_path}")
        allure.attach(context.driver.get_screenshot_as_png(),
                      name=step.name,
                      attachment_type=allure.attachment_type.PNG)