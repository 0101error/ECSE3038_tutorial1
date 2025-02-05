numbers = [1, 2, 3, 4, 5]
print("a. Initial list:", numbers)

numbers.append(6)
print("\nb. List after appending 6:", numbers)

numbers.insert(0, 0)
print("\nc. List after inserting 0 at the beginning:", numbers)

numbers.remove(3)
print("\nd. List after removing 3:", numbers)

print("\ne. Modified list:", numbers)

is_five_in_list = 5 in numbers
print("\nf. Is 5 in the list?", is_five_in_list)