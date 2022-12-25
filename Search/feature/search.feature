Feature: Testing search function working properly

   Scenario: Check that the user can search for specific element
    Given : I am on '/search_bar' page
    When : In the search bar input I type 'LISTS'
    Then : Specific results are displayed