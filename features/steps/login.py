from behave import *

from features.page_objects.AccounPage import AccountPage
from features.page_objects.HomePage import HomePage
from features.page_objects.LoginPage import LoginPage


@given(u'Navigated to login page')
def step_impl(context):
    context.hp = HomePage(context.driver)
    context.hp.click_my_account()
    context.hp.select_login_option()

@when(u'Enter valid email as "{email}" and password as "{password}" in password field')
def step_impl(context, email, password):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email_address(email)
    context.login_page.enter_password(password)


@when(u'Click on Login button')
def step_impl(context):
    context.account_page = context.login_page.click_login_button()


@then(u'User should get logged in')
def step_impl(context):
    assert context.account_page.display_status_of_edit_your_account_info()


@when(u'Enter invalid email and valid password')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email_address("<PASSWORD>@gmail.com")
    context.login_page.enter_password("slowbird3286")


@then(u'User should get warning message')
def step_impl(context):
    expected_message = "Warning: No match for E-Mail Address and/or Password."
    assert context.login_page.get_warning_message() == expected_message


@when(u'Enter valid email and invalid password')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email_address("pritbende@gmail.com")
    context.login_page.enter_password("slowbird6")


@when(u'Enter invalid email and invalid password')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email_address("<PASSWORD>@gmail.com")
    context.login_page.enter_password("slord3286")


@when(u'User do not enter any credentials')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email_address("")
    context.login_page.enter_password("")
