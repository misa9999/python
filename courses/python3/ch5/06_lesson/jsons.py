import json


customers = {
    1: {
        "first_name": "misa",
        "last_name": "amane",
        "age": 25,
        "height": 1.70,
        "weight": 75,
    },
    2: {
        "first_name": "lucy",
        "last_name": "heartfilia",
        "age": 17,
        "height": 1.65,
        "weight": 57,
    },
    3: {
        "first_name": "utaha",
        "last_name": "kasumigaoka",
        "age": 16,
        "height": 1.70,
        "weight": 60,
    },
}

with open("customers.json", "w") as file:
    json.dump(customers, file, indent=4)
