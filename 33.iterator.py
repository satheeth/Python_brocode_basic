# my_list = [1, 2, 3, 4]
#
# my_list = iter(my_list)
#
# print(next(my_list))
# print(next(my_list))
# print(next(my_list))
# print(my_list.__next__())

class PowTox:
    def __init__(self, max = 0):
        self.max = max
    def __iter__(self):
        self.n = 0
        return self
    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration

obj = PowTox(5)
i = iter(obj)

print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))

