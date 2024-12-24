# 2D_list = [list1, list2, list3]

# fruits =     ["apple", "orange", "banana", "coconut"]
# vegetables = ["celery", "carrots", "potatoes"]
# meats =      ["chicken", "fish", "turkey"]
#
# groceries = [fruits, vegetables, meats]
# print(groceries[2])
# print(groceries[0][2])
# print(groceries[2][2])

# or do like this
groceries = [["apple", "orange", "banana", "coconut"],
             ["celery", "carrots", "potatoes"],
             ["chicken", "fish", "turkey"]]

print(groceries[2])
print(groceries[0][2])
print(groceries[2][2])

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()