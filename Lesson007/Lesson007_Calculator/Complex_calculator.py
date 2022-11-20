# Calculator of complex numbers by Ilia Kozlov for GB

InList = [2, '+', '(', 96, '-', 6, 'j', ')', '-', '(', 45, '+', 5, 'j', ')', '*', 4, '/', '(', -45, '+', 19, 'j', ')'] # Input data

def Complex_calculator(inlist):
    
    for i in range(len(inlist)): # Remove "()" and include complex numbers into sub-lists
        intl = []
        temp = 0
        if inlist[i] == '(':
            for k in range(i + 1, i + 4):
                temp = inlist[k]
                intl.append(temp)
                inlist[i] = intl

    # print(f'\nInput list after first filter: {inlist}')

    def filter_list(mylist): # Remove "trash": elements remained after first filter (like: 45, '-', 6, 'j', ')')
        i = 0
        while i < len(mylist):
                if type(mylist[i]) == list:
                    mylist.pop(i + 1)
                i += 1
        return mylist

    for count in range(5):
        inlist = filter_list(inlist)

    # print(f'\nInput list after second filter: {inlist}')

    for i in range(len(inlist)): # Remove "+" and "-" in sub-lists
        if type(inlist[i]) == list:
            for k in range(len(inlist[i]) - 1):
                if inlist[i][k] == '+':
                    inlist[i].remove(inlist[i][k])
                elif inlist[i][k] == '-':
                    inlist[i][k + 1] = 0 - inlist[i][k + 1]
                    inlist[i].remove(inlist[i][k])
    
    # print(f'\nInput list after third filter: {inlist}')

    for i in range(len(inlist)): # Transform real number into complex one based on statement: a = a + 0j
        inner = []
        if type(inlist[i]) != list and type(inlist[i]) != str:
            inner.append(inlist[i])
            inner.append(0)
            inlist[i] = inner
    
    # print(f'\nInput list after fourth filter: {inlist}')

    def multiplication(list1, list2): # Multiplication formula used: (a + bj) * (c + dj) = (ac - bd) + (bc + ad)
        x1 = 0
        x2 = 0
        mult_list = []
        for i in range(len(list1) - 1):
            x1 = ((list1[i] * list2[i]) - (list1[i+1] * list2[i + 1]))
            x2 = ((list1[i+1] * list2[i]) + (list1[i] * list2[i + 1]))
            mult_list.append(round(x1, 3))
            mult_list.append(round(x2, 3))
            return mult_list

    def division(list1, list2): # Division formula used: (a + bj) / (c + dj) = ((ac + bd) / (c^2 + d^2)) + ((bc - ad) / (c^2 + d^2)) 
        x1 = 0
        x2 = 0
        div_list = []
        for i in range(len(list1) - 1):
            x1 = ((list1[i] * list2[i]) + (list1[i+1] * list2[i + 1])) / (list2[i]**2 + list2[i + 1]**2)
            x2 = ((list1[i+1] * list2[i]) - (list1[i] * list2[i + 1])) / (list2[i]**2 + list2[i + 1]**2)
            div_list.append(round(x1, 3))
            div_list.append(round(x2, 3))
            return div_list

    def addition(list1, list2):
        x1 = 0
        x2 = 0
        add_list = []
        for i in range(len(list1) - 1):
            x1 = list1[i] + list2[i]
            x2 = list1[i+1] + list2[i + 1]
            add_list.append(round(x1, 3))
            add_list.append(round(x2, 3))
            return add_list

    def subtraction(list1, list2):
        x1 = 0
        x2 = 0
        sub_list = []
        for i in range(len(list1) - 1):
            x1 = list1[i] - list2[i]
            x2 = list1[i+1] - list2[i + 1]
            sub_list.append(round(x1, 3))
            sub_list.append(round(x2, 3))
            return sub_list

    count_add = count_mult = 0
    for i in inlist:
        if i == '*' or i == '/':
            count_mult = count_mult + 1
        elif i == '+' or i == '-':
            count_add = count_add + 1

        for j in range(count_mult+1):

            for i in range(len(inlist) - 1):
                if inlist[i] == '*':
                    inlist[i] = multiplication(inlist[i - 1], inlist[i + 1])
                    inlist.pop(i - 1)
                    inlist.pop(i)
                    # print(inlist)
                    break

                elif inlist[i] == '/':
                    inlist[i] = division(inlist[i - 1], inlist[i + 1])
                    inlist.pop(i - 1)
                    inlist.pop(i)
                    # print(inlist)
                    break

    for j in range(count_add+1):

        for i in range(len(inlist) - 1):
            if inlist[i] == '+':
                inlist[i] = addition(inlist[i - 1], inlist[i + 1])
                inlist.pop(i - 1)
                inlist.pop(i)
                # print(inlist)
                break

            elif inlist[i] == '-':
                inlist[i] = subtraction(inlist[i - 1], inlist[i + 1])
                inlist.pop(i - 1)
                inlist.pop(i)
                # print(inlist)
                break
    
    out_string = ''
    if inlist[0][1] > 0:
        out_string = f'{inlist[0][0]} + {inlist[0][1]}j'
        return out_string
    else:
        out_string = f'{inlist[0][0]} - {abs(inlist[0][1])}j'
        return out_string

CompResult = Complex_calculator(InList)
print(f'\nYour result: {CompResult}\n')
