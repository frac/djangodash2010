Feature: Main record things
    In order to catalog phonograph records 
    As the db I should have all this stuff

    Scenario: Collections exist
        Given I have a Collection model
        And the model has the following attributes
            | attr         |
            | title        |
            | album_set    |
            | notes        |

    Scenario: Albuns exist
        Given I have an Album model
        And the model has the following attributes
            | attr               |
            | title              |
            | alt_title          |
            | collection         |
            | label              |
            | label_issue_number |
            | date_event         |
            | notes              |

    Scenario: Labels exist
        Given I have a Label model
        And the model has the following attributes
            | attr       |
            | name       |
            | album_set  |
            | notes      |

    Scenario: Disks exist
        Given I have a Disk model
        And the model has the following attributes
            | attr         |
            | album_id     |
            | disk_speed   |
            | disk_size    |
            | disk_type    |
            | track_set    |
            | notes        |

    Scenario: Tracks exist
        Given I have a Track model
        And the model has the following attributes
            | attr           |
            | disk_id        |
            | title          |
            | track_num      |
            | disk_side      |
            | duration       |
            | date_recording |
            | notes          |

    Scenario: Credits exist
        Given I have a Credit model
        And the model has the following attributes
            | attr           |
            | track_id       |
            | person_id      |
            | role_id        |
            | notes          |

        
    Scenario: People exist
        Given I have an Person model
        And the model has the following attributes
            | attr      |
            | name      |
            | birthdate |
            | deathdate |
            | notes     |
        
    Scenario: Roles exist
        Given I have an Role model
        And the model has the following attributes
            | attr      |
            | name      |
            | notes     |
        
