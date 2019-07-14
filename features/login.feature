Feature: Login Functionality
         Here we will test the functionality of login by admin, super admin, guest and customers

  Background:
    Given User is on Login Page

  Scenario Outline: Login by Admin
    When User enter Admin Username as <Username>
    And User enter Admin Password as <Password>
    And User clicks on Login Button
    Then User should be logged in Successfully with Admin Id

    Examples:
    |Username|Password|
    |Admin |admin123|