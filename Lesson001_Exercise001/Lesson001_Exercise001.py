# Write a code that will receive a number corresponding to a day of a week and check if it is weekend

# First day of week is MONDAY (1)

n = int(input("Enter your Number: "))

if n == 6 or n == 7:
    print("Yes. It is a weekend")
else:
    print("No. It is not a weekend")