Feature:Testing if user can register on site

   Background:
      Given register: I am a user on demostore My account page

     Scenario: Check that the user can create an account
       When : I complete Email address field with a right address
       When : I complete Password field which respects the security conditions
       When : I click on Register button
       Then : Register was successful