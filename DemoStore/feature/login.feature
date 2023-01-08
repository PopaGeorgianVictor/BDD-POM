Feature:Testing if user can login on site

   Background:
      Given register: I am a user on demostore My account page

     Scenario: Check that the user can login
       When : I complete Username or email address field with a right address
       When : I complete Password field with a right password
       When : I select checkbox  Remember me
       When : I click on Log in button
       Then : I am able to log in

     Scenario: Check if empty field error message appears
       When : I click on Log in button
       Then : I got the error message "Error: Username is required."

     Scenario: Check if empty password field error message appears
       When : I complete Username or email address field
       When : I click on Log in button
       Then : I got the error message "Error: The password field is empty."

     Scenario: Check if wrong password error message appears
       When : I complete Username or email address field with test@email.com
       When : I entered a wrong password for the inserted username
       When : I click on Log in button
       Then : I got the error message "Error: The password you entered for the username test@email.com is incorrect. Lost your password?"