# logical operator = evaluate multiple condition (or, and, not)
#                    or = at least one condition must be True
#                    and = both condition must be True
#                    not = inverts the condition (not False, not true)

'''
#or
temp = 30
is_raining = True

if temp > 32 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")
'''
'''
#and
temp = 20
is_sunny = True

if temp>= 28 and is_sunny:
    print("It is hot outside")
    print("It is sunny")

elif temp <= 0 and is_sunny:
    print("It is COLD outside")
    print("it is sunny")

elif temp < 28 and temp > 0 and is_sunny:
    print("It is WARM outside")
    print("it is sunny")
'''

temp = 0
is_sunny = False

if temp>= 28 and is_sunny:
    print("It is hot outside")
    print("It is sunny")

elif temp <= 0 and is_sunny:
    print("It is COLD outside")
    print("it is sunny")

elif temp < 28 and temp > 0 and is_sunny:
    print("It is WARM outside")
    print("it is sunny")

elif temp>= 28 and not is_sunny:
    print("It is hot outside")
    print("It is Cloudy")

elif temp <= 0 and not is_sunny:
    print("It is COLD outside")
    print("it is Cloudy")

elif temp < 28 and not is_sunny:
    print("It is WARM outside")
    print("it is Cloudy")