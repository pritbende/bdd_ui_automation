Feature: Search Functionality

  @completed
  Scenario: Search for a valid product
    Given Navigated to home page
    When Enter valid product into Seach box field
    And Clik on Search button
    Then Valid product should display in search result

  Scenario: Search for invalid product
    Given Navigated to home page
    When Enter invalid product into Seach box field
    And Clik on Search button
    Then Respective message should be displayed in search result

  Scenario: Search without entering product
    Given Navigated to home page
    When Do not enter product into Seach box field
    And Clik on Search button
    Then Respective message should be displayed in search result
