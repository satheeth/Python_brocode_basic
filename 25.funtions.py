# function = A block of reusable code
#            place() after the function name to invoke it

# def happy_birthday(name, age):
#     print(f"Happy birthiday to {name}!")
#     print(f"You are {age} old!")
#     print("Happy birthiday to you!")
#     print()
#
# happy_birthday("satheeth",23)
# happy_birthday("mohamed",24)
# happy_birthday("sahul",22)

#positional argument
def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"your bill of rs{amount:.2f} is due : {due_date}")

display_invoice("Mohamed", 100, "01/02")