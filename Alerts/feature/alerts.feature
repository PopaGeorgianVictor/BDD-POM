Feature: Testing if Alerts, Confirm & Prompts working properly

   Scenario: Check if html alerts is  and I can close it
    Given : I am on '/alert_confirm_prompt' homepage
    When : I click on  'Show an alert (html alert)' button
    Then : Is displayed an alert message , 'This is alert using just html.'
    When : I click on close icon , 'X'
    Then : I am able to close this alert