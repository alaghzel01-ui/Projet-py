person = {"name": "Ahmed", "age": 25, "city": "Rabat"}
print(person["name"])
print(person["age"])
print(person["city"])

person["age"] = 26
print("Age b3d ttbdil:", person["age"])
person["job"] = "Developer"
print(person)

print("") 
print("Loop for all:") 
for key in person: 
    print(key, ":", person[key])