#Functions 
#Functions are repeatable lines of code within a program that can be called to perform certain tasks
#Functions must be defined befor you use them

def squareFunction():
    print ("##########")
    print ("#        #")
    print ("#        #")
    print ("#        #")
    print ("##########")

#Calling a function 
#You must do this for the function to return anything 
#You can cal a function as many times as you want 
squareFunction()

#Using functions in for loops
for i in range (10):
    squareFunction()


#Control of the program 
#The program is able to see a call to a function, loop back to the functions defintiion to run the code, and then pick up where it left off
def func():
    print("Inside function")

print("Line 1 outside function")
func()
print("Line 2 outside function")
func()
print("Line 3 outside function")


#Use variables within functions 
#1) Local variables 
#Local variables can only be accessed within the function 
def heightFunction():
    #This variable only exists within this function. Therefor it is a local variable
    height = int(input("Please enter your height in inches: "))
    print("Height in inches:", height)

#"print(height)" Would give me an error
heightFunction()


#2) Global variables
#Global variables are variables defined outside of a function 
#You can use the same name for local and global variables without encountering an error
height = 2


#Arguments 
#An argument is data that you pass through something else inside parentheses
#The print statement takes arguments 
print(height)


#Giving arguments to functions 
#The arguments can be nums or strings 
def argumentFunction(numArgument):
    print(numArgument)
    numArgument += 1
    print(numArgument)

argumentFunction(3)


#Passing more than one argument to a function 
def sumOfTwoNums(num1, num2):
    total = num1 + num2
    print(total)

sumOfTwoNums(3,5)


#Returning values with functions 
def multiplyTwoNums(num1, num2):
    total = num1 * num2
    return total

#The return statement doesn't show anything in the console
multiplyTwoNums(2,2)
#But we can store it's value in a variable
total = multiplyTwoNums(2,2)
print(total)

#Sep 
print("Hi", "Isabella", sep=" ")

#Time library 
import time
print("hi")
time.sleep(5)
print("hello")