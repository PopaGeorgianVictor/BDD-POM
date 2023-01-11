Feature: Testing if Radio Buttons working properly

     Background:
   Given : I am on '/radio_btn' page

   Scenario: Check if default button is selected
    Then : 'Rock FM' button is selected by default

   Scenario: Check if all button are selectable
    When : I select radio buttons one by one
    Then : I can select any button

   Scenario: Verify number of radio buttons
    Then : Number of radio buttons is as expected
