# Write a program wich takes a number N as input and displays a multiplication of numbers from 1 to N

n = int(input("Enter Your number N: "))

i = 1
result = i
myList = []

while i <= n:
    result = result * i
    i += 1
    myList.append(result)
print("If N = 4, then", myList)

