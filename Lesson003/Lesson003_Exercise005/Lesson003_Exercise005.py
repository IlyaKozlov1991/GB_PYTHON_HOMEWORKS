# Set-up an array of random INT numbers with size of m*n (taken from console) so that number of items must be even. Print a table. Mix items so that each item will take a new place for not more than m*n / 2 iterations

from array import array
from random import random
from random import randint # this promt is required for further random filling of array

s = int(input("\nEnter number of strings: "))
c = int(input("Enter number of columns: "))

def create_array(m, n): # Function to create an array and fill it with random numbers
    inter_array = []
    for i in range(m):
        internal_arr = []
        for j in range(n):
            internal_arr.append(randint(0, 100)) # random INT numbers from 0 to 10
        inter_array.append(internal_arr)
    return inter_array

def print_array(array): # Function to print an array
    for i in range(len(array)):
        for j in range(len(array[i])):
            print(array[i][j], end = ' ')
        print()

# def to_string(array): # Function to convert array to string so it is possible to format final output dispaly
#     inter_string = str()
#     for i in range(len(array)):
#         for j in range(len(array[i])):
#             inter_string = inter_string + str(array[i][j])
#     print(inter_string)
#     return inter_string

# def format_string(string):
#     inter_string = str()
#     j = 0
#     k = 0
#     for i in range(len(string)):
#         while j < s:
#             while k < c:
#                 inter_string = string[k]

def mix_array(array):
    inter_array = []
    for i in range(len(array) - 1):
        for j in range(len(array) - 1):
            inter_array.insert(0, array[randint(0, c)])
            array.append(inter_array[0])
        print(f'Mix_arr: {array}')

if (s * c) % 2 == 0:
    myArray = create_array(s, c)
    print()
    print_array(myArray)
    print()
else:
    print("\nError! Try another dimensions!\n")
# myString = to_string(myArray)
# format_string(myString)
mix_array(myArray)