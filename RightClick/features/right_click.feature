Feature: Testing if right click working properly

   Scenario: Check that the user can handle right click menu
    Given : I am on '/right_click_menu' page
    When : I perform a right click on page
    Then : A right click menu opened
    When : I click on option from menu
    Then : A new link with related results are opened


