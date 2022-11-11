# RLE algorythm

str1 = 'abcdefffghjkklmnooo'

counter = 1
var = ''
coef = ''
temp1 = ''
list1 = []
i = 0
str2 = ''
print(f'len(str1): {len(str1)}')
print(f'len(str1) - 1 {len(str1) - 1}')


for i in range (len(str1) - 1):
    var = str1[i]
    if var != str1[i - 1] and var != str1[i + 1]:
        print(f'if i: {i}')
        print(f'if counter: {counter}')
        # counter = 1
        coef = var
        list1.append(coef)
        print(f'if list1: {list1}')
    elif var == str1[i - 1]: 
        print(f'elif1 i: {i}')
        # var == str1[i - 1]
        counter +=1
        coef = f'{counter}{var}'
        temp1 = coef
        print(f'elif1 list1: {list1}')
        print(f'elif1 counter: {counter}')
    elif var != str1[i - 1] and counter > 1:
        print(f'elif2 i: {i}')
        list1.append(temp1)
        counter = 1
        print(f'elif2 list1: {list1}')
print(list1)

# def encode(message):
# 	encoded_message = ""
# 	i = 0

# 	while (i <= len(message)-1):
# 		count = 1
# 		ch = message[i]
# 		j = i
# 		while (j < len(message)-1):
# 			if (message[j] == message[j+1]):
# 				count = count+1
# 				j = j+1
# 			else:
# 				break
# 		encoded_message=encoded_message+str(count)+ch
# 		i = j+1
# 	return encoded_message

# #Provide different values for message and test your program
# encoded_message=encode("ABBBBCCCCCCCCAB")
# print(encoded_message)
