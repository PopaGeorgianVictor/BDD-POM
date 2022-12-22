Feature:Testing if the dropdowns work and if I can selected options and accesing links

  Scenario: Check that the user can have access on dropdown menu 1
    Given : I am on '/dropdown' homepage
    When : I click on  '--Please choose an option--' from 'Coding Languages List'
    Then : A dropdown menu opens with related options and I can select any option from menu


  Scenario: Check that the user can have access on dropdown menu 2
    Given :I am on '/dropdown' homepage
    When : I click on  'Select GitHub Project'
    Then : A dropdown menu opens with related options


  Scenario: Check that the user can selected option from 'Coding Languages List'
    Given : I am on '/dropdown' homepage
    When : I selected options from dropdown menu
    Then : I can select any option from dropdown


  Scenario: Check that the user can selected option from 'Select GitHub Project'
    Given : I am on '/dropdown' homepage
    When : I selected options from dropdown menu
    Then : I can select any option from dropdown and I have acces to the right link