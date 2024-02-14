from reporting_client_v2 import check_ship


def test():
    test_carrier_1 = """{"alignment": "Enemy", "name": "Star Destroyer", 
    "class_ship": "Carrier", "length": 123.90185546875, "crew_size": 9, 
    "armed": true, "officers": 
    [{"first_name": "Nova", "last_name": "Stellar", "rank": "Commander"}, 
    {"first_name": "Luna", "last_name": "Nebula", "rank": "Commander"}, 
    {"first_name": "Astrid", "last_name": "Nebula", "rank": "Captain"}, 
    {"first_name": "Orion", "last_name": "Stellar", "rank": "Commander"}]}"""
    assert check_ship(test_carrier_1) == False

    test_carrier_2 = """{"alignment": "Ally", "name": "Star Destroyer", 
    "class_ship": "Carrier", "length": 1230.90185546875, "crew_size": 152, 
    "armed": false, "officers": 
    [{"first_name": "Nova", "last_name": "Stellar", "rank": "Commander"}, 
    {"first_name": "Luna", "last_name": "Nebula", "rank": "Commander"}, 
    {"first_name": "Astrid", "last_name": "Nebula", "rank": "Captain"}, 
    {"first_name": "Orion", "last_name": "Stellar", "rank": "Commander"}]}"""
    assert check_ship(test_carrier_2) == True

    test_corvette_1 = """{"alignment": "Ally", "name": "Star Destroyer", 
    "class_ship": "Corvette", "length": 1203.90185546875, "crew_size": 9, 
    "armed": true, "officers": 
    [{"first_name": "Nova", "last_name": "Stellar", "rank": "Commander"}, 
    {"first_name": "Luna", "last_name": "Nebula", "rank": "Commander"}, 
    {"first_name": "Astrid", "last_name": "Nebula", "rank": "Captain"}, 
    {"first_name": "Orion", "last_name": "Stellar", "rank": "Commander"}]}"""
    assert check_ship(test_corvette_1) == False

    test_corvette_2 = """{"alignment": "Ally", "name": "Star Destroyer", 
    "class_ship": "Corvette", "length": 123.90185546875, "crew_size": 9, 
    "armed": true, "officers": 
    [{"first_name": "Nova", "last_name": "Stellar", "rank": "Commander"}, 
    {"first_name": "Luna", "last_name": "Nebula", "rank": "Commander"}, 
    {"first_name": "Astrid", "last_name": "Nebula", "rank": "Captain"}, 
    {"first_name": "Orion", "last_name": "Stellar", "rank": "Commander"}]}"""
    assert check_ship(test_corvette_2) == True

    test_destroyer_1 = """{"alignment": "Ally", "name": "Star Destroyer", 
    "class_ship": "Destroyer", "length": 1203.90185546875, "crew_size": 55, 
    "armed": true, "officers": 
    [{"first_name": "Nova", "last_name": "Stellar", "rank": "Commander"}, 
    {"first_name": "Luna", "last_name": "Nebula", "rank": "Commander"}, 
    {"first_name": "Astrid", "last_name": "Nebula", "rank": "Captain"}, 
    {"first_name": "Orion", "last_name": "Stellar", "rank": "Commander"}]}"""
    assert check_ship(test_destroyer_1) == False

    test_destroyer_2 = """{"alignment": "Enemy", "name": "Star Destroyer", 
    "class_ship": "Destroyer", "length": 1230.90185546875, "crew_size": 55, 
    "armed": true, "officers":
    [{"first_name": "Nova", "last_name": "Stellar", "rank": "Commander"}, 
    {"first_name": "Luna", "last_name": "Nebula", "rank": "Commander"}, 
    {"first_name": "Astrid", "last_name": "Nebula", "rank": "Captain"}, 
    {"first_name": "Orion", "last_name": "Stellar", "rank": "Commander"}]}"""
    assert check_ship(test_destroyer_2) == True


if __name__ == '__main__':
    test()
