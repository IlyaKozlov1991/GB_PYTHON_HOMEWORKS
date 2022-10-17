# Set-up a list of numbers. Write a program which finds sum ODD of list's items.

from random import randint


def create_fill_list (list): # Function to create and fill a list
    inter_list = []
    for i in range(randint(5, 10)): # Set-up random length length (from 5 to 10) of the list
        inter_list.insert(0, randint(0, 10)) # Fill internal list with random INT numbers from 0 to 10
        list.append(inter_list[0]) # Fill main list with items from internal list
    print(f'\nYor list: {list}')

def find_sum_odd(list): # Function to sort the list and find sum of its odds
    inter_list = []
    sum = 0
    for i in range(len(list) - 1):
        inter_list = list[1::2] # Sorting is done by means of slicing starting from index 1 with step of 2
    print(f'\nOdd items in Your list: {inter_list}')
    for k in range(len(inter_list)):
        sum = sum + inter_list[k]
    print(f'Sum of odds: {sum}')

myList = []

create_fill_list(myList)

find_sum_odd(myList)