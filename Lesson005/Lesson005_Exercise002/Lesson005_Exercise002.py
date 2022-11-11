# RLE algorythm

str1 = 'abcdefffghjkklmnooo'
str2 = ''
var = ''
counter = 1
coef = ''
list1 = []

for i in range (len(str1)):
    var = str1[i]
    if var != str1[i - 1]: # Does current value match previous one?
        if var == str1[i + 1]: # And does it match next one?
            counter += 1
            coef = f'{counter}{var}'
            list1.append(coef)
            # print(f'if i: {i}')
            # print(f'if counter: {counter}')
            # print(f'if list1: {list1}')
        else:
            counter = 1
            coef = var
            list1.append(coef)
            # print(f'else i: {i}')
            # print(f'else counter: {counter}')
            # print(f'else list1: {list1}')

for var in list1:
    str2 = str2 + var
print(f'\nOriginal string:\n{str1}')
print(f'\nFormated string:\n{str2}\n')