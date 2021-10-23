#Practice Problem 
#Average finder 

def average():
    amountInput = int(input("How many numbers would you like to use in your calculation: "))
    add = 0 
    counter = 0
    while counter < amountInput:
        numInput = int(input("Enter a number you would like in your calculation: "))
        add += numInput
        counter += 1
    print("The avereage is", add/amountInput)

average()