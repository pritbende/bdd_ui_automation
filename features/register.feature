Feature: Register Functionality

  Scenario: Register with all mandetory fields
    Given Navigated to Register page
    When User enter all mandetory field
    And User click on Register button
    Then Account should get created

  Scenario: Register with existing email
    Given Navigated to Register page
    When User enter existing email and all other fields
    And User click on Register button
    Then Respective register error message should display