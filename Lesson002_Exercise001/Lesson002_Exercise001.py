# Write a program that takes a real or integer number as input and displays the sum of its digits.

from pickle import FALSE, TRUE


n = float(input("Enter Your number: "))
m = n # For nice display. If you put (n) in line 18 display will be 0->result, because in the end pf the program n==0

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
        print("n: ", n)
        n = round((n * 10), 10)
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

