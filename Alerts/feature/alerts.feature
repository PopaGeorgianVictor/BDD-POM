Feature: Testing if Alerts, Confirm & Prompts working properly

   Scenario: Check if html alert is displayed and I can close it
    Given : I am on '/alert_confirm_prompt' homepage
    When : I click on  'Show an alert (html alert)' button
    Then : Is displayed an alert message , 'This is alert using just html.'
    When : I click on close icon , 'X'
    Then : I am able to close this alert


   Scenario: Check if JavaScript  alert is displayed and I can close it
    Given : I am on '/alert_confirm_prompt' homepage
    When : I click on  'Show JavaScript Alert' button
    Then : Is displayed an alert message , 'I am a JavaScript Alert'
    When : I click  on "OK" button
    Then : I am able to close this alert