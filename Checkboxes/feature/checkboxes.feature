Feature: Testing if Checkboxes working properly

 Background:
  Given : I am on '/checkbox' page

   Scenario: Verify number of checkboxes

    Then : Number of checkboxes is as expected

   Scenario: Check that the user can select one checkbox

    When : I select one checkbox
    Then : I can select that particular checkbox

   Scenario: Check that the user can select all checkboxes

    When : I select checkboxes one by one
    Then : I can select all checkboxes