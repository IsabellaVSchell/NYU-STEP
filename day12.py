#Lists 
#Using a list is a way to store multiple values in a variable
#A list is one of the four built in data types. The others ar tuple, sets, and dictionaries 
#indexes  0  1  2
myList = [1, 2, 3]
print(myList)

#Adding multiple data types to a list 
var1 = "Hi"
var2 = True
var3 = 5

multiType = [var1, var2, var3]


#len
print(len(multiType))

#Prinitng specific indexes 
print(multiType[1])

#Printing with negative indexes
print(multiType[-2])

#Print multiple indexes at once
print(multiType[1:3])