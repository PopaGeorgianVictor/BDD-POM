Feature: DemoStore cart feature

  Background:
      Given home: I am a user on demostore Home page
      When home: I search after "Cap"
      When products: I add product to basket "Cap"
      When products: I click on Cart


   @cart1
    Scenario: Test cart total sum functionality
      Then cart: I verify that total price is correct "$18.99"


    @cart2
    Scenario: Test cart remove product functionality
      When cart: I click on remove item icon
      Then cart: I verify empty cart message is displayed