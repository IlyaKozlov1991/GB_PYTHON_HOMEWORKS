# Set 2D array from User's console and then sort its elements low->high from left to right and from bottom to top

from array import array
from random import random
from random import randint # this promt is required for further random filling of array
from ssl import RAND_add


s = int(input("Enter number of strings: "))
c = int(input("Enter number of columns: "))

def create_array(m, n): #function to create an array and fill it with random numbers
    myArray = []
    for i in range(m):
        internal_arr = []
        for j in range(n):
            internal_arr.append(randint(0, 10)) # random INT numbers from 0 to 10
        myArray.append(internal_arr)
    return myArray

userArray = create_array(s, c)

def sort_array(array, n): # function to sort an array; n is required for cyclic processing of all elements in all strings 
    for k in range(n - 1):
        for i in range(len(array)):
            for j in range(len(array[i]) - 1):
                if array[i][j]  > array[i][j + 1]:
                    int_var = array[i][j]
                    array[i][j] = array[i][j + 1]
                    array[i][j + 1] = int_var
                else:
                    j = j + 1


def print_array(array): # function to print an array
    for i in range(len(array)):
        for j in range(len(array[i])):
            print(array[i][j], end=' ')
        print()

print()
print("Your array:\n")
print_array(userArray)

sort_array(userArray, c)
print()
print("Your sorted array:\n")
print_array(userArray)