# Calculator of complex numbers

InList = [10, 4, '-', -7, 9] # Input numbers. N1 = el1 & el2; N2 = el4 & el5

def Complex_calculator(list):
    
    def find_operation(list): # Check for math operation to do and remove its symbol from input list
        string = ''
        for i in range(len(list) - 1):
            if list[i] == '*' or list[i] == '/' or list[i] == '+' or list[i] == '-':
                string = list[i]
                list.remove(list[i])
        return string

    Math = find_operation(InList) # Math symbol of operation to do

    def split_list(list): # Split list into two lists: each number - separate list
        x = len(list) // 2
        return list[:x], list[x:]

    In1 = split_list(InList) # Create a tuple consisting of two lists (numbers)

    n1 = In1[0] # N1 converted
    n2 = In1[1] # N2 converted

    def multiplication(n1, n2): # Multiplication formula used: (a + bj) * (c + dj) = (ac - bd) + (bc + ad)
        x1 = 0
        x2 = 0
        string = ''
        for i in range(len(n1) - 1):
            x1 = ((n1[i] * n2[i]) - (n1[i+1] * n2[i + 1]))
            x2 = ((n1[i+1] * n2[i]) + (n1[i] * n2[i + 1]))
        if x2 > 0:
            string = (f'\nResult = {round(x1, 3)} + {round(x2, 3)}j')
            return string
        else: # This is required if imaginary part of Result is negative
            string = (f'\nResult = {round(x1, 3)} - {round(abs(x2), 3)}j') # abs(x2) is required not to have Result = x1 + -x2j
            return string

    def division(n1, n2): # Division formula used: (a + bj) / (c + dj) = ((ac + bd) / (c^2 + d^2)) + ((bc - ad) / (c^2 + d^2)) 
        x1 = 0
        x2 = 0
        string = ''
        for i in range(len(n1) - 1):
            x1 = ((n1[i] * n2[i]) + (n1[i+1] * n2[i + 1])) / (n2[i]**2 + n2[i + 1]**2)
            x2 = ((n1[i+1] * n2[i]) - (n1[i] * n2[i + 1])) / (n2[i]**2 + n2[i + 1]**2)
        if x2 > 0:
            string = (f'\nResult = {round(x1, 3)} + {round(x2, 3)}j')
            return string
        else: # This is required if imaginary part of Result is negative
            string = (f'\nResult = {round(x1, 3)} - {round(abs(x2), 3)}j') # abs(x2) is required not to have Result = x1 + -x2j
            return string

    def addition(n1, n2):
        x1 = 0
        x2 = 0
        string = ''
        for i in range(len(n1) - 1):
            x1 = n1[i] + n2[i]
            x2 = n1[i+1] + n2[i + 1]
        if x2 > 0:
            string = (f'\nResult = {round(x1, 3)} + {round(x2, 3)}j')
            return string
        else: # This is required if imaginary part of Result is negative
            string = (f'\nResult = {round(x1, 3)} - {round(abs(x2), 3)}j') # abs(x2) is required not to have Result = x1 + -x2j
            return string

    def subtraction(n1, n2):
        x1 = 0
        x2 = 0
        string = ''
        for i in range(len(n1) - 1):
            x1 = n1[i] - n2[i]
            x2 = n1[i+1] - n2[i + 1]
        if x2 > 0:
            string = (f'\nResult = {round(x1, 3)} + {round(x2, 3)}j')
            return string
        else: # This is required if imaginary part of Result is negative
            string = (f'\nResult = {round(x1, 3)} - {round(abs(x2), 3)}j') # abs(x2) is required not to have Result = x1 + -x2j 
            return string

    if Math == '*':
        Result = multiplication(n1, n2)
    elif Math == '/':
        Result = division(n1, n2)
    elif Math == '+':
        Result = addition(n1, n2)
    elif Math == '-':
        Result = subtraction(n1, n2)
    
    return Result

CompResult = Complex_calculator(InList)
print(CompResult)
print()
