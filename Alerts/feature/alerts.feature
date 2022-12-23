Feature: Testing if Alerts, Confirm & Prompts working properly

   Scenario: Check if html alerts is displayed
    Given : I am on '/alert_confirm_prompt' homepage
    When : I click on  'Show an alert (html alert)' button
    Then : Is displayed an alert message , 'This is alert using just html.'
    When : I select options one by one from dropdown
    Then : I can select any option from dropdown