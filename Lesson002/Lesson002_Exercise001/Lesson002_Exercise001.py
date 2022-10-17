# Write a program that takes a real or integer number as input and displays the sum of its digits.

from pickle import FALSE, TRUE


n = float(input("Enter Your number: "))
m = n # For nice display. Impossible to print origin (n), because it is processed at the moment of print

myList = []

if n.is_integer() == True: # check if input number (n) is either int or float
    while n > 0:
        myList.insert(0, n % 10)
        n = n // 10

    sum = myList[0]
    for i in range(len(myList) - 1):
        sum = sum + myList[i + 1]
    print("\nYour result:")
    print(int(m), "->", int(sum))
elif n.is_integer() == False:
    while (n.is_integer() == False):
        n = round((n * 10), 10) # Round to 10 symbols after dot is required for adequate operation of this part of the programm
    k = n
    print(k)
    while k > 0:
        myList.insert(0, k % 10)
        k = k // 10
    
    sum = myList[0]
    for i in range(len(myList) - 1):
        sum = sum + myList[i + 1]
    print("\nYour result:")
    print(m, "->", int(sum))

