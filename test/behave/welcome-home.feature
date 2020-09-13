Feature: welcome-home

  Scenario: Welcome home
    Given an english speaking user
     When the user says "I am home"
     Then "welcome-home" should reply with dialog from "welcome.home.dialog"
