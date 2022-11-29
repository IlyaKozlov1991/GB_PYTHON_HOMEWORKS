# Write a program to calculate an arithmetic expression given by a string. Use the +,-,/,* operations. operation priority is standard.

user_str = input('\nEnter your expression: ')

my_list = []

for char in user_str: # Remove space between symbols, if User put some, and append values to list
    if char != ' ':
        my_list.append(char) 

for i in range(len(my_list)): # Convert items of the list into INT, if items are numbers
    try:
        my_list[i] = int(my_list[i])
    except ValueError:
        my_list[i] = my_list[i]

count_add = 0
count_mult = 0
for i in my_list:
    if i == '*' or i == '/':
        count_mult = count_mult + 1
    elif i == '+' or i == '-':
        count_add = count_add + 1

for j in range(count_mult + 1):
    for i in range(len(my_list) - 1):
                if my_list[i] == '*':
                    my_list[i] = my_list[i-1] * my_list[i+1]
                    my_list.pop(i - 1)
                    my_list.pop(i)
                    break
                elif my_list[i] == '/':
                    my_list[i] = my_list[i-1] / my_list[i+1]
                    my_list.pop(i - 1)
                    my_list.pop(i)
                    break
for j in range(count_add + 1):
    for i in range(len(my_list) - 1):
                if my_list[i] == '+':
                    my_list[i] = my_list[i-1] + my_list[i+1]
                    my_list.pop(i - 1)
                    my_list.pop(i)
                    break
                elif my_list[i] == '-':
                    my_list[i] = my_list[i-1] - my_list[i+1]
                    my_list.pop(i - 1)
                    my_list.pop(i)
                    break
result = int(my_list[0])
print(f'\nResult:\n{user_str} = {result}\n')