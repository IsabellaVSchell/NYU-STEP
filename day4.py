#Conditional statements 
somevalue = 1

#First part of conditional 
if (somevalue == True) :
    print("The condition was true")

#To test for more than one condition 
elif (somevalue == False):
    print("The condition was false")

#If the if statment doesn't evaluate to true(This particular example will never reach this else statement)
else:
    print("The condition was not true or false")


#Nested conditionals 
var1 = 0

if(var1 > 0):
    #This is the nested conditional: a conditional inside a conditional
    if(var1 % 2 == 0):
        print("The number is postitive and even")
    else:
        print("The number is positive and odd")
elif(var1 < 0):
    if(var1 % 2 == 0):
        print("The number is negative and even")
    else:
        print("The number is negative and odd")
else:
    print("The number is 0")
    

#Sample program 
temp = float(input("What is the temperature today?"))
wind = float(input("What is the wind spead today?"))

if(temp > 30 and temp < 60):
    print("Wear a sweater")

elif(temp < 30):
    if(wind > 20):
        print("Wear a jacket")
        print("Also wear a scarf ")
    else:
        print("Wear a jacket")
        print("But don't wear a scarf")
else:
    print("It's warm out. No need to wear anything additional!")