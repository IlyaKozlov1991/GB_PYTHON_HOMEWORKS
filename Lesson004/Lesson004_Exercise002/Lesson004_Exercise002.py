# Set-up a sequence of numbers. Write a program which prints list of non-repeating items of original sequence

from random import randint

def create_fill_list (list): # Function to create and fill a list
    inter_list = []
    for i in range(randint(10, 15)): # Set-up random length length (from 10 to 15) of the list
        inter_list.insert(0, randint(1, 50)) # Fill internal list with random INT numbers from 0 to 50
        list.append(inter_list[0]) # Fill main list with items from internal list
    print(f'\nYor random list: {list}\n')

def find_repeats(list1, list2): # Function to find repeating elements. The idea of this function is to have a list of elements which are repeating. And then compare this list with origin list and remove all repeating
    inter_list = []
    inter_var = 0
    for i in range(len(list1)):
        inter_var = list1[0] # Take a value of first element of origin list
        list1 = list1[1::] # Slicing (sorting) from 1st element of origin list
        if inter_var in list1:
            inter_list.append(inter_var)
            list2.append(inter_var) # This list is required for further comparison
            i += 1
        elif inter_var in inter_list:
            inter_list.append(inter_var)
            list2.append(inter_var)
            i += 1
        else:
            i += 1


def compare_list(list1, list2): # Function to compare items of list1 and list2 and remove from list1 if present
    for i in range(len(list2)):
        if list2[i] in list1:
            list1.remove(list2[i])
            i += 1
        else:
            i += 1
    print(f'\nNon-repeating elements in Your list: {list1}\n')

list1 = []
list2 = []

create_fill_list(list1)
find_repeats(list1, list2)
compare_list(list1, list2)