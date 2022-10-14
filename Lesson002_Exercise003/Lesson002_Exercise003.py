# Write a programm which takes 2 (two) strings as inputs and checks how many times STR1 is found in STR2

str1 = input("Enter Your firts string (STR1): ")
str2 = input("Enter Your second string (STR2): ")
str3 = str2 # For good display of message in case if not present. Impossible to use str2, because it is processed at the moment of display

myList = [] # Filling of list
for i in range(len(str2)): # Operation while length os STR2
    myList.append(str2[:1]) # Adding of item to list by means of SLICING the STR2 from 0-ndex to 1-index (1 is not included) 
    str2 = str2[1:] # Slicing the STR2 from 1-index to exclude first item in the next cycle

counter = 0 # Counting how many times STR1 is present in STR2
for k in range(len(myList)):
    if myList[k] == str1:
        counter += 1

tempVar = counter # Definition of which message to display
if tempVar != 0:
    print("\nSTR1 is found in STR2:", tempVar, "times")
else:
    print("\nSTR1 is not found in STR2")