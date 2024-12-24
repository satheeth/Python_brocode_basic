import time
my_time = int(input("enter the time in scondes: "))
# for x in range(0, my_time):
#     print(x)
#     time.sleep(1)
# print(("Time's up!"))


#reverse
# for x in range(my_time, 0, -1):
#     print(x)
#     time.sleep(1)
# print("Time's up!")

for x in range(my_time, 0 , -1):
    second = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{second:02}")
    time.sleep(1)

print("Time's up")