Feature:Testing if user can login on site

   Background:
      Given register: I am a user on demostore My account page

     Scenario: Check that the user can login
       When : I complete Email address field with a right address
       When : I complete Password field with a right password
       When : I select checkbox Remerber me
       When : I click on Log in
       Then : I am able to log in