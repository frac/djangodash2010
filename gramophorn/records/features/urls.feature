Feature: Full url list
    In order to use the site
    As a user I should see all the following

    Scenario: Home page
        Given I want to navigate the site
        When I go to the /
        Then I should see a working page

    Scenario: Home page
        Given I want to navigate the site
        When I go to the /settings/
        Then I should see a working page

    Scenario: Home page
        Given I want to navigate the site
        When I go to the /records/
        Then I should see a working page


