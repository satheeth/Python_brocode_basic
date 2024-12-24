# conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#                          print or assign one of the two values based on a condition
#                          X if condition else Y

num = 7
a = 8
b = 5
age = 17
temperature = 18
user_role = "admin"

# print("Positive" if num > 0 else "Negative")

# result = "Even" if num % 2 == 0 else "Odd"
# print(result)

max_num = a if a > b else b
min_num = a if a < b else b
print(max_num)
print(min_num)

status = "Adult" if age >= 18 else "Child"
print(status)

wheather = "Hot" if temperature > 20 else "Cold"
print(wheather)

access_level = "Full Access" if user_role == "admin" else "Limited Access"
print(access_level)