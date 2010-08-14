Feature: Main record things
    In order to storage records 
    As the owner I should

    Scenario: Records exist
        Given I have a Record model
        And the Record model has the following attributes
            | attr |
            | name |
        And the record has multiple songs

    Scenario: Songs exist
        Given I have a Song model
        And the Song model has the following attributes
            | attr |
            | name |
        And the song has multiple artists
        
    Scenario: Artists exist
        Given I have an Artist model
        And the Artist model has the following attributes
            | attr |
            | name |
        
        
