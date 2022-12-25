Feature: Testing search function working properly

   Scenario: Check that the user can search for specific element
    Given : I am on '/search_bar' page
    When : In the search bar input I type 'LISTS'
    Then : Specific results are displayed


   Scenario: Check that the user can acces links
    Given : I am on '/search_bar' page
    When : I click on 'LISTS'
    Then : A new link are opened