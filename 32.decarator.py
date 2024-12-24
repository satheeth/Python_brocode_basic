# Decarator = A function that extends the behavior of another funtion
#             w/o modifying the base function
#             Pass the base function as an arguments to the decartor

#             @add_sprinkles
#             @get_ics_cream("vanilla")

# def add_sprinkles(func):
#     def wrapper(*args, **kwargs):
#         print("you add sprinkles")
#         func(*args, **kwargs)
#     return wrapper
#
# def add_fudge(func):
#     def wrppper(*args, **kwargs):
#         print("you add you fudge")
#         func(*args, **kwargs)
#     return wrppper
#
# @add_fudge
# @add_sprinkles
# def get_ice_cream(flavour):
#     print(f"Here is your {flavour} ice cream")
#
# get_ice_cream("vannila")

# def this_is_dec(func):
#     def greeting():
#         print("Assalamu Alaikum")
#         func()
#         print("thanks for coming to my house")
#     return greeting
#
# def House():
#     print("Welcome to my House")
#
# House = this_is_dec(House)
# House()

def this_is_dec(func):
    def greeting():
        print("Assalamu Alaikum")
        func()
        print("thanks for coming to my house")
    return greeting
@this_is_dec
def House():
    print("Welcome to my House")

House()