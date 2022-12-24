Feature: Testing if Radios Buttons working properly

   Scenario: Check if html alert is displayed and user can close it
    Given : I am on '/radio_btn' page
    When : I click on  'Show an alert (html alert)' button
    Then : Is displayed an alert message , 'This is alert using just html.'
    When : I click on close icon , 'X'
    Then : I am able to close this alert