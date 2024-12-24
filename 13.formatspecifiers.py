# format specifiers = {value:flags} format a value based on what
#                              flags are inserted

# .(number)f = round to that many decimal places (fixed points)
# .(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center justify
# :+ = use a plus sign to indicates postive value
# := = place sign to leftmost position
# :  = insert a space before postive numbers
# :, = comma separator

price1 = 3.14159
price2 = -987.65
price3 = 12.34

price4 = 446426.44
price5 = 2325551.2
price6 = 85466.464

print(f"Price 1 is {price1:.3f}")
print(f"Price 2 is {price2:.1f}")
print(f"Price 3 is {price3:.2f}")

print(f"Price 1 is {price1:10}")
print(f"Price 2 is {price2:10}")
print(f"Price 3 is {price3:10}")

print(f"Price 1 is {price1:010}")
print(f"Price 2 is {price2:010}")
print(f"Price 3 is {price3:010}")

print(f"Price 1 is {price1:<10}")
print(f"Price 2 is {price2:<10}")
print(f"Price 3 is {price3:<10}")

print(f"Price 1 is {price1:>10}")
print(f"Price 2 is {price2:>10}")
print(f"Price 3 is {price3:>10}")

print(f"Price 1 is {price1:^10}")
print(f"Price 2 is {price2:^10}")
print(f"Price 3 is {price3:^10}")

print(f"Price 1 is {price1:+}")
print(f"Price 2 is {price2:+}")
print(f"Price 3 is {price3:+}")

print(f"Price 4 is {price4:,}")
print(f"Price 5 is {price5:,}")
print(f"Price 6 is {price6:,}")

print(f"Price 4 is {price4:,.2f}")
print(f"Price 5 is {price5:,.2f}")
print(f"Price 6 is {price6:,.2f}")

print(f"Price 4 is {price4:+,.2f}")
print(f"Price 5 is {price5:+,.2f}")
print(f"Price 6 is {price6:+,.2f}")