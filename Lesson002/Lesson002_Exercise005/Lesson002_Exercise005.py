# Write a code which will check either statement ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z is TRUE or FALSE. Number of predicates is randomly generated from 5 to 25, values of predicates are random. Check the statement 100 times and show how many time was spend

from random import randint, random
import time

start = time.time() # START program timestamp
n1 = randint(5, 25) # Set-up a number of variables
myList = []

for i in range(n1): # Sill a list with random numbers
    internal_list = []
    internal_list.insert(0, int(randint(0, 10))) # random INT numbers from 0 to 10
    myList.insert(0, internal_list[0])

#c = ~(x + y + z) == ~(x) * ~(y) * ~(z)

start_cyle = time.time() #START cycle timestamp
k = 0
c = 0
while k < 100:
    sum = myList[0]
    prod = ~myList[0]
    for i in range(len(myList) - 1):
        sum = ~(sum + myList[i + 1])
    for j in range(len(myList) - 1):
        prod = prod * ~myList[i + 1]
    c = sum == prod
    k += 1
finish_cycle = time.time() #FINISH cycle timestamp
print(f'\nTime spent to check statement: {finish_cycle - start_cyle} sec')

finish = time.time() #FINISH program timestamp
print(f'\nTotal time spent: {finish - start} sec\n')