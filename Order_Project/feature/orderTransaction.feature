Feature: Order Transaction
    Tests related to Order Transaction

    Scenario Outline: Verify Order Success message shown in detail page
       Given place the item order with <username> and <password>
       And the user is on landing page
       When I login to portal with <username> and <password>
       And navigate to order page
       And select to order page
       Then order message is successfully displayed

       Examples:
            | username              | password   |
            | rahulshetty@gmail.com | Iamking@000 |
