Feature: Login Functionality

  @pom1 @login
  Scenario Outline: Login with valid email and password
    Given Navigated to login page
    When Enter valid email as "<email>" and password as "<password>" in password field
    And Click on Login button
    Then User should get logged in
    Examples:
      |email                      |password|
      |pritbende@gmail.com        |slowbird3286|
      |amotoorisampleone@gmail.com|secondone|

  @login @pom2
  Scenario: Login with invalid email and valid password
    Given Navigated to login page
    When Enter invalid email and valid password
    And Click on Login button
    Then User should get warning message

  @login @pom3
  Scenario: Login with valid email and invalid password
    Given Navigated to login page
    When Enter valid email and invalid password
    And Click on Login button
    Then User should get warning message

  @login @pom4
  Scenario: Login with invalid credentilas
    Given Navigated to login page
    When Enter invalid email and invalid password
    And Click on Login button
    Then User should get warning message

  @login @pom5
  Scenario: Login without any credentials
    Given Navigated to login page
    When User do not enter any credentials
    And Click on Login button
    Then User should get warning message