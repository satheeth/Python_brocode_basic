# Iterables  = An object/collection that can return its elements on at a time
#              allowing it to be iterated over in loop

numbers = (1, 2, 3, 4, 5)

# for item in reversed(numbers):
#     print(item, end=" - ")
#
# fruits = {"apple", "orange", "banana", "coconut"}
#
# # for item in reversed(fruits):
# #     print(item)
#
# for item in fruits:
#     print(item)

# name = "Mohamed Satheeth"
# for character in name:
#     print(character, end = " ")

my_dictionary = {"A":1, "B":2, "C":3}

# for key in my_dictionary:
#     print(key)

# for value in my_dictionary.values():
#     print(value)

for key, value in my_dictionary.items():
    print(f"{key} : {value}")