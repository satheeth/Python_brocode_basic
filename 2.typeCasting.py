#TypeCasting = the process pf converting a variable from one data type to another
#              str(), int(), float(), bool()

name = "Satheeth"
name2 = ""
age= 23
gpa = 8.5
is_student= False

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

gpa = int(gpa)
print(gpa)

sage = float(age)
print(sage)

age = str(age)
print(age)
print(type(age))

age += "1"
print(age)

name = bool(name)
print(name)

name2 = bool(name2)
print(name2)
