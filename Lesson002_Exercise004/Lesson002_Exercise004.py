# Write programm which takes a number (N) and ccordinates of two points as input and find a distance between the points in ND space

from math import sqrt


n = int(input("Enter number N: "))

# Solution with enterring eqch coordinate one by one (CAN BE USED)
# myListA = []
# for i in range(n):
#     a = int(input("Enter coordinates of point A: "))
#     myListA.append(a)
# print(myListA)

# myListB = []
# for i in range(n):
#     b = int(input("Enter coordinates of point B: "))
#     myListB.append(b)
# print(myListB)

# dist = 0 # Block to find distances between each pare of coordinates
# interList = []
# for i in range(len(myListA)):
#     dist = (myListB[i] - myListA[i])**2
#     interList.append(dist)

# result = 0 # Final block to get final result
# for i in range(len(interList) - 1):
#     result = sqrt(interList[i] + interList[i + 1])
# print(round(result, 2))

pointA = input("Enter coordintaes of point A: ")
myListA = []

pointB = input("Enter coordintaes of point B: ")
myListB = []

def create_list(list, string): # Create and fill list with sliced input string
    for i in range(len(string)):
        list.append(string[:1])
        string = string[1:]
    print(list)
    return list

def first_filter(list): # Remove " " from list
    i = 0 
    while i <= len(list) - 1:
        if (list[i] == " "):
            list.remove(list[i])
        i +=1
    else:
        i +=1

def second_filter(list): # Remove "," from list
    i = 0 
    while i <= len(list) - 1:
        if (list[i] == ","):
            list.remove(list[i])
        i +=1
    else:
        i +=1

def conver_print_list(list):  # Convert list values from STR to INT
    for i in range(len(list)):
        list[i] = int(list[i])
    print(list)

create_list(myListA, pointA)
first_filter(myListA)
second_filter(myListA)
conver_print_list(myListA)

create_list(myListB, pointB)
first_filter(myListB)
second_filter(myListB)
conver_print_list(myListB)

# dist = 0 # Block to find distances between each pare of coordinates
# interList = []
# for i in range(len(myListA)):
#     dist = (myListB[i] - myListA[i])**2
#     interList.append(dist)

# result = 0 # Final block to get final result
# for i in range(len(interList) - 1):
#     result = sqrt(interList[i] + interList[i + 1])
# print(round(result, 2))