Feature: Testing if Checkboxes working properly

   Scenario: Verify number of checkboxes
    Given : I am on '/checkbox' page
    Then : Number of checkboxes is as expected

   Scenario: Check that the user can select one checkbox
    Given : I am on '/checkbox' page
    When : I select one checkbox
    Then : I can select that particular checkbox

   Scenario: Check that the user can select all checkboxes
    Given : I am on '/checkbox' page
    When : I select checkboxes one by one
    Then : I can select all checkboxes