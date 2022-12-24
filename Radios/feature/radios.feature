Feature: Testing if Radio Buttons working properly

   Scenario: Check if default button is selected
    Given : I am on '/radio_btn' page
    Then : 'Rock FM' button is selected by default

   Scenario: Check if all button are selectable
    Given : I am on '/radio_btn' page
    When : I select radio buttons one by one
    Then : I can select any button

   Scenario: Verify number of radio buttons
    Given : I am on '/radio_btn' page
    Then : Number of radio buttons is as expected
