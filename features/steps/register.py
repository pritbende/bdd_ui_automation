from behave import *

@given(u'Navigated to Register page')
def step_impl(context):
    print(u'STEP: Given Navigated to Register page')


@when(u'User enter all mandetory field')
def step_impl(context):
    print(u'STEP: When User enter all mandetory field')


@when(u'User click on Register button')
def step_impl(context):
    print(u'STEP: When User click on Register button')


@then(u'Account should get created')
def step_impl(context):
    print(u'STEP: Then Account should get created')


@when(u'User enter existing email and all other fields')
def step_impl(context):
    print(u'STEP: When User enter existing email and all other fields')


@then(u'Respective register error message should display')
def step_impl(context):
    print(u'STEP: Then Respective register error message should display')
