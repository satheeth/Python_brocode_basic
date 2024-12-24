# Excercise 2 shopping Cart Program

item = input("What item would you like to buy?: ")
price = int(input("What is the price?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity

print(f" you have bought {quantity} x {item}/s")
print(f"your total is {total}")
