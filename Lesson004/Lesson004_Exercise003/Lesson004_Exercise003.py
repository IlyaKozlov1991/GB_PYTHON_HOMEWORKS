# A natural degree k is given. Randomly generate a list of coefficients (values from 0 to 100) of the polynomial and write the polynomial of degree k to the file

from random import randint
from datetime import date
from datetime import time
from datetime import datetime

k = int(randint(2, 10))
# exp = 0
# a = int(randint(0, 100))
# b = int(randint(0, 100))
# c = int(randint(0, 100))

print(f'\nYour random degree: {k}\n')

def add_coefficients(list, n): # Function to ceate a list of coefficients
    for i in range(n + randint(0, 5)): # Random number of coefficients
        a = int(randint(0, 100))
        list.append(a)


def polym(list1, list2, n): # Function to create polynominal of degree
    inter_list = []
    for i in range(len(list1)):
        while n >= 0:
            if n > 1:
                # print(f'if i: {i}')
                inter_list.append(f'{list1[i]}*x^{n}')
                list2.append(f'{list1[i]}*x^{n}')
                n = n - 1
                # print(inter_list)
                i += 1
            elif n == 1:
                # print(f'elif i: {i}')
                inter_list.append(f'{list1[i]}*x')
                list2.append(f'{list1[i]}*x')
                n = n -1
                i += 1
            elif n == 0 and i <= len(list1) - 1:
                # print(f'!!! i {i}')
                inter_list.append(f'{list1[i]}')
                list2.append(f'{list1[i]}')
                i += 1
                # print(f'!!! i: {i} inter_list: {inter_list}')
            break # VERY IMPORTANT!!! Otherwise  cycle will try to go over len(list1)
    # print(inter_list)
    # print(list)

list1 = []

list2 = []

add_coefficients(list1, k)

polym(list1, list2, k)

str1 = ""

for i in range(len(list2)):
    str1 = str1 + f'{list2[i]} + '

str1 = str1[:len(str1) - 2:] # Slice to remove extra " + " in str

print("Your polynomial of degree:")
print(f'\n{str1} = 0\n')

# my_date = date.today()

date_time = datetime.now()

file = open("Lesson004_Ex003.txt", "a")
file.write(f'\nYour random degree: {k}\nYour polynomial of degree:\n{date_time.day}/{date_time.month}/{date_time.year} {date_time.hour}:{date_time.minute}:{date_time.second}: {str1} = 0\n')
file.close()