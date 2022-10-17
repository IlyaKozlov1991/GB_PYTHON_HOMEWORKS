# Write a programm which finds production of pairs of items in a list. Pair is first and last items, second and penultimate  etc.

from random import randint

def create_fill_list (list): # Function to creat and fill a list
    inter_list = []
    for i in range(randint(5, 10)): # Set-up random length length (from 5 to 10) of the list
        inter_list.insert(0, randint(0, 10)) # Fill internal list with random numbers from 0 to 10
        list.append(inter_list[0]) # Fill main list with items from internal list
    # print(f'\nYor list: {list}')

def pares(list): # Function to find pairs and multiply them
    inter_list = []
    for i in range(len(list) - 1):
        while i <= (len(list) - 1) / 2: # This cycle is needed not to oversort the list
            inter_list.append((list[i] * list[(len(list) - 1) - i]))
            i += 1
        else:
            break
    print(f'\n{list} => {inter_list}\n')

myList = []

create_fill_list(myList)
pares(myList)