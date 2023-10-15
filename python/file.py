import json

data = {
    {
        "empid": "SJ011MS",
        "personal": {
            "name": "Smith Jones",
            "gender": "Male",
            "age": 28,
            "address": {
                "domain":"Finance",
                "streetaddress": "724th Street",
                "city": "New York",
                "state": "NY",
                "postalcode": "10038",
            },
        },
        "profile": {"designation": "Deputy General", "department": "Finance"},
    },
    {
        "empid": "SJ011MF",
        "personal": {
            "name": "Smith Jones",
            "gender": "Male",
            "age": 28,
            "address": {
                "domain":"Telecom",
                "streetaddress": "724th Street",
                "city": "New York",
                "state": "NY",
                "postalcode": "10038",
            },
        },
        "profile": {"designation": "Deputy General", "department": "Finance"},
    },

}
json_data = json.dumps(data)
with open('data.json', 'w') as f:
    f.write(json_data)

# file = open('data.json', 'r')
#
# data = json.load(file)
print(data)
