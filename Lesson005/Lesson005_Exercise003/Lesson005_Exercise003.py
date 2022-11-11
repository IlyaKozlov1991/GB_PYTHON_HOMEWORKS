# Write a program which removes all words containing "абв" from text

str1 = 'Write a program which removes all words containing "абв" from text. Write a program which removes all words containing абвfrom text; Write a program which removes all words containing"абв" from text'
str2 = 'абв' # Marker
str3 = ''

print(f'\nYour original string:\n')
print(f'{str1}')

myList1 = str1.split(' ') # Split original string with separator (' ') and add each word to list

myList2 = []

for char in myList1:
    if str2 not in char: # If marker is NOT present in word from list1, this word is added to list2
        myList2.append(char)

for char in myList2: # Assemble an output string
    str3 = str3 + char + ' '

print(f'\nYour formated string:\n')
print(f'{str3}\n')