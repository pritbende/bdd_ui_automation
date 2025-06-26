from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'Navigated to home page')
def step_impl(context):
    assert context.driver.title.__eq__('Your Store')

@when(u'Enter valid product into Seach box field')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").send_keys("HP")


@when(u'Clik on Search button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//div[@id='search']//button").click()

@then(u'Valid product should display in search result')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT, "HP LP3065").is_displayed()
    context.driver.quit()


@when(u'Enter invalid product into Seach box field')
def step_impl(context):
    print(u'STEP: When Enter invalid product into Seach box field')


@then(u'Respective message should be displayed in search result')
def step_impl(context):
    print(u'STEP: Then Respective message should be displayed in search result')


@when(u'Do not enter product into Seach box field')
def step_impl(context):
    print(u'STEP: When Do not enter product into Seach box field')