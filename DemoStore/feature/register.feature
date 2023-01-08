Feature:Testing if user can register on site

   Background:
      Given register: I am a user on demostore My account page

     Scenario: Check that the user can create an account
       When : I complete Email address field with a right address
       When : I complete Password field which respects the security conditions
       When : I click on Register button
       Then : Register was successful

     Scenario: Check if alert email adress message appears
       When : I complete Email address field with an already registered address
       When : I click on Register button
       Then : I got the error message "Error: An account is already registered with your email address. Please log in."