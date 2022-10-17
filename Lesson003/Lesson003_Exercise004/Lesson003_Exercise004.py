# Write a program which converts decimal number to binary

from random import randint

n = randint(10, 100)
m = n # For good display

a = n % 2 # Block to convert DEC to BIN
myString = str(a)
while n >= 2:
    n  = n // 2
    a = n % 2
    myString = myString + str(a)

myString = myString[::-1] # Reverse the string by means of slicing 
print(f'\nYour DEC number {m} -> to BIN {myString}\n')