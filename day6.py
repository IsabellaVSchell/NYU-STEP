#Day 5 review:
#Range in for loops start at 0 automatically and are not inclusive. therefor if you had for i in range(10): print(i), this would print 0-9
#Pass is when you want to have a loop but don't want to run anything
#The break keyword is a good way to break out of a loop


#While loops 
#Create a program that will continuously ask the user for a postive input and stop when the user enters a negative number or 0. 
#After program ends, it will print final sum and how many numbers had been added
counter = 0
sum = 0 
isNegative = False 

while(isNegative == False):
    numInput = int(input("Enter a positive integer"))
    if(numInput <= 0):
        #Both of these will work
        break
        #isNegative = True
    else: 
        #+= adds something. someVar += 1 is the same as saying someVar = someVar + 1
        sum += numInput
        counter += 1

print("The final sum is", sum)
print("We added", counter, "numbers")

#Else in while loops
#The else will only run once once the program breaks out of the while loop
countVar = 0
while(countVar < 5):
    print("num is less than 5")
    countVar += 1
else:
    print("Num is 5 or more")

#Make a times table 
for i in range(1,13):
    for j in range(1,13):
        print(i*j, end="\t")
    print()