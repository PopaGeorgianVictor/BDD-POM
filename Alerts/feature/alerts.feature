Feature: Testing if Alerts, Confirm & Prompts working properly

   Scenario: Check if html alerts is displayed
    Given : I am on '/alert_confirm_prompt' homepage
    When : I click on  '--Please choose an option--' from 'Coding Languages List'
    Then : A dropdown menu opens with related options
    When : I select options one by one from dropdown
    Then : I can select any option from dropdown