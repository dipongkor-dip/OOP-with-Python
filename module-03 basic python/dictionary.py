# key value pair = dictionary
# object
# hash table
# overlap with set
# {key: value, key: value}

person = {"name": "hani", "address": "ali nagar", "age": 23}

person["language"] = "python"  # insert
person["name"] = "hani sag"  # update

del person["age"] # delete

# special dictionary looping
for k,v in person.items():
    print(k, v)    

# print(person)
