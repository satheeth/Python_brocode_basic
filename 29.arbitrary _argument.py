# *args     = allow yout o pass multiple non - key arguments
# **kwargs  = allows you to multiple keyword-arguments
#             * unpacking operator

# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total
#
# print(add(1,4,5,7))
#
# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")
#
# display_name("Dr.", "Spongebob", "Harold", "SquarePants", "III")

# def print_address(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
#
# print_address(street="123 street",
#               building_no = "851",
#               city="chennai",
#               state="tamil Nadu",
#               pincode="600000")

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if "build_no" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('build_no')}")

    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")

    else:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('pincode')}")


shipping_label("Dr.", "Spongebob","Squarepants", "III",
               street="1234 street.",
               pobox="PO box 123",
               city="chennai",
               state="Tamilnadu",
               pincode="600000")