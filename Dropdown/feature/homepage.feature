Feature:Testing if the dropdowns work and if I can access the links

  Scenario: Check that the user can have access on dropdown 1
    Given : I am on '/dropdown' homepage
    When : I click on  '--Please choose an option--' from 'Coding Languages List'
    Then : A dropdown menu opens with related


  Scenario: Check that the user can have access on dropdown 2
    Given :I am on '/dropdown' homepage
    When : I click on  'Select GitHub Project'
    Then : A dropdown menu opens with related options