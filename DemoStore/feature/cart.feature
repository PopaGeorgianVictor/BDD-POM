Feature: DemoStore cart feature

  Background:
      Given home: I am a user on demostore Home page
      When home: I search after "Cap"
      When products: I add product to basket "Cap"
      When products: I click on Cart