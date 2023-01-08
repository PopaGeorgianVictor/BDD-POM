Feature:Testing if user can register on site

   Background:
      Given register: I am a user on demostore My account page

     Scenario: Check that the user can create an account
       When : I complete Email address field with a right address
       When : I complete Password field which respects the security conditions
       When : I click on Register button
       Then : Register was successful

     Scenario: Check if invalid Email address error message appears
       When : I complete Email address field with a wrong address format
       When : I click on Register button
       Then : I got the error message "Please provide a valid email address"

     Scenario: Check if already registered address error message appears
       When : I complete Email address field with an already registered address
       When : I click on Register button
       Then : I got the error message "An account is already registered with your email address."

      Scenario: Check "hint" password
        When : I complete password field but without respecting the security requirements
        Then : A hint for my password is displayed "Hint: The password should be at least twelve characters long. To make it stronger, use upper and lower case letters, numbers, and symbols like ! " ? $ % ^ & )."
