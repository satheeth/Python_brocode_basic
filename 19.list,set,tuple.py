# collection = single "variable" used to store multiple values
#   list  =  [] ordered and changeable. Duplicates ok
#   set   =  {} unordered and immutable, but Add/Remove OK. No duplicates
#   Tuple =  () ordered and unchangeable. Duplicates OK. Faster
# list
# fruits = ["apple", "orange", "banana", "coconut", "pineapple"]
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("custardapple" in fruits)

# fruits[1] = "custard apple"
# fruits.append("custard apple")
# fruits.extend(["gouva","grapes","mango"])

# fruits.insert(0, "custardapple")
# fruits.sort()
# fruits.reverse()
# fruits.remove("apple")
# fruits.pop() #its remove the last element
# fruits.pop(1)
# del fruits[0]
# fruits.clear()
# print(fruits.index("mango"))
# print(fruits.count("pineapple"))
# print(fruits[::-1])
# COMPREHENSIONS
# numbers = [1, 2, 3, 4]
# doubled_numbers = [num * 2 for num in numbers]
# print(doubled_numbers)


# for fruit in fruits:
#     print(fruit)

#set
# fruits = {"apple", "orange", "banana", "coconut", "pineapple", "orange"}
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("pineapple" in fruits)
# print(fruits[0])  #we are can't able use indexing in SET

# fruits.add("custardapple")
# fruits.update((1,8,9))
# fruits.remove("apple")
# fruits.discard("apple")
# fruits.pop()
# fruits.clear()
# print(fruits)

# for fruit in fruits:
#     print(fruit)
# difference
# A = {10, 20, 30, 40, 80}
# B = {100, 30, 80, 40, 60}
# print (A.difference(B))
# print (B.difference(A))

# difference update
# A = {10, 20, 30, 40, 80}
# B = {100, 30, 80, 40, 60}
# A.difference_update(B) # Modifies A and returns None
# print(A)

# intersection
# s1 = {1, 2, 3}
# s2 = {2, 3}
# print(s1.intersection(s2))

# intersetion_update
# s1 = {1, 2, 3}
# s2 = {2, 3}
# s1.intersection_update(s2)
# print(s1)

# union
# A = {2, 4, 5, 6}
# B = {4, 6, 7, 8}
# print("A U B:", A.union(B))

# symmetric_difference
# A = {1, 2, 3}
# B = {2, 3, 4}
# print(A.symmetric_difference(B))

# symmetric_difference_update
# A = {1, 2, 3}
# B = {2, 3, 4}
# A.symmetric_difference_update(B)
# print(A)

# disjoint
# Checks whether the sets are disjoint or not
# s1 = {1, 2, 3}
# s2 = {4, 5, 6}
# print(s1.isdisjoint(s2))

# issubset()
# Returns True if all elements of a set A are present in another set B
# s1 = {1, 2, 3, 4, 5}
# s2 = {4, 5}
# print(s2.issubset(s1))

# issuperset()
# Returns True if all elements of a set A occupies set B
# A = {4, 1, 3, 5}
# B = {6, 0, 4, 1, 5, 0, 3, 5}
# print("A.issuperset(B) : ", A.issuperset(B))
# print("B.issuperset(A) : ", B.issuperset(A))

#copy
# set1 = {1, 2, 3, 4}
# set2 = set1.copy() # function to copy the set
# print(set2) # prints the copied set


# tuple
# fruits = ("apple", "orange", "banana", "coconut", "pineapple", "orange")

# print(dir(fruits))
# print(len(fruits))
# print("custardapple" in fruits)
# print(fruits.index("orange"))
# print(fruits.count("orange"))

# for fruit in fruits:
#     print(fruit)
# print(fruits)
