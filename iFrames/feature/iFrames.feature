Feature: Testing if iFrames working properly

   Scenario: Check how many frames are in page
    Given : I am on '/iFrame' page
    Then :I can see how many frames is in page

   Scenario: Check that the user can make some actions outside iFrame
    Given : I am on '/iFrame' page
    When : I click on outside frames button
    Then : An alert is displayed


   Scenario: Check that the user can perform some actions inside iFrame
    Given : I am on '/iFrame' page
    When : I click on inside frames button
    Then :I can make actions inside iFrame

