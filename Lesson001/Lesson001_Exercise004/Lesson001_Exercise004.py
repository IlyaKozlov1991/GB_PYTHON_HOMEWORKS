# Write a simple calculator which will receive: number 1, number 2 and operation and then proceed

#Supported operations: +, -, /, *, mod (remainder of division), pow (exponent), div (integer division)

n1 = float(input("Enter Number 1: "))
n2 = float(input("Enter Number 2: "))
operation = input("Enter Operation: ")

if operation == "+":
    print(n1 + n2)

if operation == "-":
    print(n1 - n2)

if operation == "/" and n2 != 0.0:
    print(n1 / n2)

if operation == "*":
    print(n1 * n2)

if operation == "mod" and n2 != 0.0:
    print(n1 % n2)

if operation == "pow":
    print(n1 ** n2)

if operation == "div" and n2 != 0.0:
    print(n1 // n2)

if (operation == "/" or "mod" or "div") and n2 == 0: # Check for division by 0
    print("Division by 0!")
