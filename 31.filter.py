#filter
# def is_even(n):
#     return  n%2 == 0
#
# nums = [3,2,6,8,4,6,2,9]
#
# evens = list(filter(is_even,nums))
#
# print(evens)

# filter using lambda
# nums = [3,2,6,8,4,6,2,9]
# evens = list(filter(lambda n : n % 2 == 0, nums))
# print(evens)

#map

# def update(n):
#     return n*2
#
# nums = [3,2,6,8,4,6,2,9]
# evens = list(filter(lambda n : n%2 == 0, nums))
# doubles = list(map(update,evens))
# print(evens)
# print(doubles)

# nums = [3,2,6,8,4,6,2,9]
# evens = list(filter(lambda n : n%2 == 0, nums))
# doubles = list(map(lambda n : n*2, evens))
# print(evens)
# print(doubles)

#reduce
# from functools import reduce
#
# def add_all(a,b):
#     return a + b
# nums = [3,2,6,8,4,6,2,9]
# evens = list(filter(lambda n : n%2 == 0, nums))
# doubles = list(map(lambda n : n*2,evens))
# sum = reduce(add_all, doubles)
# print(evens)
# print(doubles)
# print(sum)

from functools import reduce

nums = [3,2,6,8,4,6,2,9]
evens = list(filter(lambda n : n%2 == 0, nums))
doubles = list(map(lambda n : n*2,evens))
sum = reduce(lambda a,b : a+b, doubles)
print(evens)
print(doubles)
print(sum)