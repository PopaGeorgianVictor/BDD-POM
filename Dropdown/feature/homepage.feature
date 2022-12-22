Feature: It is tested if the dropdowns work and if I can access the links

  Scenario: Check that the user can access '/dropdown' page
    Given : I am on homepage
    When : I click on  '--Please choose an option--' from 'Coding Languages List'
    Then : A dropdown menu opens with related options