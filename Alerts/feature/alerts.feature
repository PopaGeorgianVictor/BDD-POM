Feature: Testing if Alerts, Confirm & Prompts working properly

   Scenario: Check if html alert is displayed and user can close it
    Given : I am on '/alert_confirm_prompt' homepage
    When : I click on  'Show an alert (html alert)' button
    Then : Is displayed an alert message , 'This is alert using just html.'
    When : I click on close icon , 'X'
    Then : I am able to close this alert


   Scenario: Check if JavaScript  alert is displayed and user can close it
    Given : I am on '/alert_confirm_prompt' homepage
    When : I click on  'Show JavaScript Alert' button
    Then : Is displayed an alert message , 'I am a JavaScript Alert'
    When : I click  on "OK" button
    Then : I am able to close this alert

   Scenario: Check if Confirm alert working and after user click 'OK' button, the messages are displayed accordingly
    Given : I am on '/alert_confirm_prompt' homepage
    When : I click on  'Show a Confirm Alert' button
    Then : Is displayed an alert message , 'Do you like Selenium? 'Cancel' for No, 'Ok' for Yes.'
    When : I click  on 'OK' button
    Then : I am able to close this alert and message 'Great! You will love it!' is displayed

   Scenario: Check if Confirm alert working and after user click 'Cancel' button, the messages are displayed accordingly
    Given : I am on '/alert_confirm_prompt' homepage
    When : I click on  'Show a Confirm Alert' button
    Then : Is displayed an alert message , 'Do you like Selenium? 'Cancel' for No, 'Ok' for Yes.'
    When : I click  on 'Cancel' button
    Then : I am able to close this alert and message 'Too bad!!! You would've loved it!' is displayed

   Scenario: Check if Prompt alert working and after user click 'Cancel' button,  no message are showing
    Given : I am on '/alert_confirm_prompt' homepage
    When : I click on  'Show a Prompt' button
    Then : Is displayed a input
    When : I click  on 'Cancel' button
    Then : I am able to close this alert and no message are showing

   Scenario: Check if Prompt alert working and after user click 'OK' button without complete field,the messages are displayed accordingly
    Given : I am on '/alert_confirm_prompt' homepage
    When : I click on  'Show a Prompt' button
    Then : Is displayed a input
    When : I click  on 'OK' button
    Then : I am able to close this alert and 'You have entered: none' message are showing

   Scenario: Check if Prompt alert working and after user click 'OK' button with complete field,the messages are displayed accordingly
    Given : I am on '/alert_confirm_prompt' homepage
    When : I click on  'Show a Prompt' button
    Then : Is displayed a input
    When : I complete the field with 'test' message
    When : I click  on 'OK' button
    Then : I am able to close this alert and 'You have entered: test' message are showing