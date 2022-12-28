Feature: Testing if search function working properly
    Background:
   Given : I am on '/search_bar' page

   Scenario: Check that the user can search for specific element
    When : In the search bar input I type 'LISTS'
    Then : Specific results are displayed

   Scenario: Check that the user can acces links
    When : I click on 'LISTS'
    Then : A new link are opened