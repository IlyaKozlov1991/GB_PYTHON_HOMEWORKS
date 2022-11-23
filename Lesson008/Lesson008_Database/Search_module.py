# Search and Report module for SQL Database by Ilia Kozlov

import easygui
from easygui import *
from tabulate import tabulate

data = {12345: {'Name':'Козлов Илья Владимирович','sex':'М','birthdate':[15,12,1991],
              'phones':[123,456],'salary':100000,'prof':'директор','departament':'цех1'},
        12346: {'Name':'Петров Иван Иванович','sex':'М','birthdate':[4,8,1998],
              'phones':[123,456],'salary':30000,'prof':'слесарь','departament':'цех1'},
        12347: {'Name':'Сидоров Иван Иванович','sex':'М','birthdate':[22,1,1985],
              'phones':[123,456],'salary':30000,'prof':'слесарь','departament':'цех1'},
        12348: {'Name':'Красивая Татьяна Владимировна','sex':'Ж','birthdate':[13,5,1991],
              'phones':[123,456,789],'salary':50000,'prof':'бухгалтер','departament':'цех1'}}

choise = 1 # Command received from User

list1 = [] # List which will contain MAIN keys of the dictionary (i.e. employees IDs)

for var in data.keys():
    list1.append(var)

keys_numb = 0
for var in data.keys():
    keys_numb += 1

# print(tabulate(data, headers='keys', tablefmt='fancy_grid'))

def print_names(print_list, print_dict, n): # Print all employees
    inner_list1 = []
    inner_list2 = []
    inner_list3 = [['ID', 'Name', 'Position', 'Department']]
    for i in range(len(print_list)):
        inner_list1.append(print_list[i])
        inner_list1.append(print_dict[print_list[i]]['Name'])
        inner_list1.append(print_dict[print_list[i]]['prof'])
        inner_list1.append(print_dict[print_list[i]]['departament'])
        # inner_list1.append(print_dict[print_list[i]]['phones'])
    def cut_list(list1, list2, list3):
            for i in range(len(list3[0])):
                list1.append(list2[0])
                list2.pop(0)
    k = 1
    while k <= n:
        cut_list(inner_list2, inner_list1, inner_list3)
        inner_list3.append(inner_list2)
        inner_list2 = []
        k += 1
    return inner_list3
    

def prof_search(prof_list, prof_dict, prof_name): # Print certain positions (aka professions)
    int_count = 0
    inner_list = []
    for i in range(len(prof_list)):
        if prof_dict[prof_list[i]]['prof'] == prof_name:
            print(prof_list[i], prof_dict[prof_list[i]]['Name'])
            inner_list.append(prof_list[i])
            inner_list.append(prof_dict[prof_list[i]]['Name'])   
        else:
            int_count += 1
    if int_count == len(prof_list):
        inner_str = 'Not found'
        return inner_str
    else:
        return inner_list

def birth_year(birth_list, birth_dict, birth_year): # Print certain birth years
    int_count = 0
    inner_list = []
    for i in range(len(birth_list)):
        if birth_dict[birth_list[i]]['birthdate'][2] == birth_year:
            # print(birth_list[i], birth_dict[birth_list[i]]['Name'])
            inner_list.append(birth_list[i])
            inner_list.append(birth_dict[birth_list[i]]['Name'])
            inner_list.append(birth_dict[birth_list[i]]['prof'])
        else:
            int_count += 1
    if int_count == len(birth_list):
        inner_str = 'Not found'
        return inner_str
    else:
        return inner_list

def salary_range(sal_list, sal_dict, s_min, s_max): # Print certain salary range
    inner_list = []
    for i in range(len(sal_list)):
        if sal_dict[sal_list[i]]['salary'] in range(s_min, s_max):
            print(sal_list[i], sal_dict[sal_list[i]]['Name'])
            inner_list.append(sal_list[i])
            inner_list.append(sal_dict[sal_list[i]]['Name'])
            inner_list.append(sal_dict[sal_list[i]]['prof'])
    return inner_list

if choise == 1:
    msgbox(tabulate(print_names(list1, data, keys_numb), headers='firstrow', tablefmt='fancy_grid', stralign='center'), 'List of employees')
    if ccbox('Do you want to continue?', 'Confirm the next step'):
        pass
    else:
        exit
elif choise == 2:
    def input_position():
        global var_pos
        input_values1 = enterbox('Enter name of position:')
        var_pos = str(input_values1)
        return var_pos
    position = input_position()
    msgbox(prof_search(list1, data, position), f'Employees which are {position}')
    while True: # If User wants to check another position
            if ccbox('Do you want to continue?', 'Confirm the next step'):
                position = input_position()
                msgbox(prof_search(list1, data, position), f'Employees which are {position}')
            else:
                break
elif choise == 3:
    def input_year():
        global var_year
        input_values1 = enterbox('Enter yaer of birth:')
        var_year = int(input_values1)
        return var_year
    year = input_year()
    msgbox(birth_year(list1, data, year), f'Employees born in {year}')
    while True: # If User wants to check another year
            if ccbox('Do you want to continue?', 'Confirm the next step'):
                year = input_year()
                msgbox(birth_year(list1, data, year), f'Employees born in {year}')
            else:
                break
elif choise == 4:
    def input_salary():
        global var_min
        global var_max
        input_values1 = enterbox('Enter MIN salary')
        var_min = int(input_values1)
        input_values2 = enterbox('Enter MAX salary')
        var_max = int(input_values2)
        return var_min, var_max
    input_salary()
    min = var_min
    max = var_max
    msgbox(salary_range(list1, data, min, max), f'Salary in range from {min} to {max}')
    while True: # If User wants to check another range
            if ccbox('Do you want to continue?', 'Confirm the next step'):
                input_salary()
                min = var_min
                max = var_max
                msgbox(salary_range(list1, data, min, max), f'Salary in range from {min} to {max}')
            else:
                break