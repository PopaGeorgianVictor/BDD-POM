Feature:Testing if user can login on site

   Background:
      Given register: I am a user on demostore My account page

     Scenario: Check that the user can login
       When : I complete Username or email address field with a right address
       When : I complete Password field with a right password
       When : I select checkbox  Remember me
       Then : The checkbox was selected
       When : I click on Log in button
       Then : I am able to log in

     Scenario: Check if empty email field error message appears
       When : I click on Log in button
       Then : I got the error message "Error: Username is required."

     Scenario: Check if empty password field error message appears
       When : I complete Username or email address field with a right address
       When : I click on Log in button
       Then : I got the error message "Error: The password field is empty."

     Scenario: Check if not registered username error message appears
       When : I complete Username or email address field with abc123
       When : I complete Password field with a random password
       When : I click on Log in button
       Then : I got the error message "Error: The username abc123 is not registered on this site. If you are unsure of your username, try your email address instead."

     Scenario: Check if wrong password error message appears
       When : I complete Username or email address field with a right address
       When : I entered a wrong password for the inserted username
       When : I click on Log in button
       Then : I got the error message "Error: The password you entered for the username test123@email.com is incorrect. Lost your password?"