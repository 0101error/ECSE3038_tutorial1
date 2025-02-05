squares = []
even_numbers = []
upper_case_names = []

for number in range(1, 6): 
    square = number ** 2
    squares.append(square)
print("a. List of squares:", squares)

for number in range(2, 11): 
    if number % 2 == 0: 
        even_numbers.append(number)
print("\nb. List of even numbers:", even_numbers)


people = [  
    {"name": "Bob", "age": 35, "city": "Cityville"},
    {"name": "Charlie", "age": 27, "city": "Townsville"},
    {"name": "Diana", "age": 42, "city": "Villagetown"}
]

for person in people:
    name = person["name"]
    upper_case_name = name.upper()  
    upper_case_names.append(upper_case_name)
print("\nc. List of uppercase names:", upper_case_names)