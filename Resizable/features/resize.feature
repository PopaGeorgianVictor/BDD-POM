Feature: Testing if Resizable Element working properly

   Scenario: Check that the user can resize element
    Given : I am on '/resizable' page
    When : I pull the edges element for resize
    Then : I can resize the element
    When : I tight the element for resize back
    Then : I can resize back the element