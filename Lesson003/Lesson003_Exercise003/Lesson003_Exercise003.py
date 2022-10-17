# Set up a list of real numbers. Write a program which finds difference between max and min values of functional part of items

from random import randint
from random import random

def create_fill_list (list): # Function to create and fill a list
    inter_list = []
    for i in range(randint(5, 10)): # Set-up random length length (from 5 to 10) of the list
        n = random()
        n = float('{:.2f}'.format(n)) # Formating to have 2 digits after comma
        inter_list.insert(0, (randint(0, 10) * round(n, 2))) # Fill internal list with random REAL numbers from 0 to 10
        # list.append(inter_list[0]) # Fill main list with items from internal list
        list.append(float('{:.2f}'.format(inter_list[0]))) # Formating to have 2 digits after comma
    print(f'\nYor list: {list}')

def min_max_func(list): # Function to find min and max functional parts
    intert_list = []
    for k in range(len(list)): # Cycle to cut-ot functional parts and put into internal list
        x = 0
        x = myList[k] * 100
        intert_list.append(x % 100)
    for j in range(len(intert_list)): # Cycle to sort items of inteernal list from min to max
        for l in range(len(intert_list) - j - 1):
            if intert_list[l] > intert_list[l + 1]:
                intert_list[l], intert_list[l + 1] = intert_list[l + 1], intert_list[l]
    print(f'Min functional part: {intert_list[0] / 100}')
    print(f'Max functional part: {intert_list[len(intert_list) - 1] / 100}')
    print(f'Difference Max-Min: {(intert_list[len(intert_list) - 1] - intert_list[0]) / 100}')

myList = []

create_fill_list(myList)
print()
min_max_func(myList)
print()