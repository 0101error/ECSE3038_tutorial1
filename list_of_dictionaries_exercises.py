people = [
    {"name": "Bob", "age": 35, "city": "Cityville"},
    {"name": "Charlie", "age": 27, "city": "Townsville"},
    {"name": "Diana", "age": 42, "city": "Villagetown"}
]
print("a. Initial list of people:", people)

second_person_name = people[1]["name"] 
print("\nb. Name of the second person:", second_person_name)

people[2]["age"] = 30  
print("\nc. List after updating age of the third person:", people)

new_person = {"name": "Eve", "age": 24, "city": "Newtown"}
people.append(new_person)
print("\nd. List after adding a new person:", people)

print("\ne. Modified list of people:", people)