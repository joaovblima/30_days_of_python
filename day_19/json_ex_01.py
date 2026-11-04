import json
person = {
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}


"""
person_dct = json.loads(person_dct)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])
"""
person_json= json.dumps(person, indent=4)
print(type(person_json))
print(person_json)