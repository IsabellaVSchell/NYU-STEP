import math
#Question 1
def divisors(numInput):
    squareRoot = int(numInput ** 0.5)
    for i in range(1,numInput):
        if(numInput % i == 0):
            if(i <= squareRoot):
                print(i, end=" * ")
                print(int(numInput/i))
            else:
                pass
            

numInput = int(input("Enter a number and I will print out the divisors in pairs: "))
print("Here are all the divisors in pairs: ")
divisors(numInput)


#Question 2
def isPrime(numInput):
    squareRoot = int(numInput ** 0.5)
    answer = ""
    for i in range(2, squareRoot + 1):
        if(numInput % i == 0):
            answer = "This is not a prime number"
            break
        else:
            answer = "This is a prime number"
    print(answer)

numInput = int(input("Enter a number and I will tell you if it is a prime number or not: "))
isPrime(numInput)

#Question 3 
def rightTriangle(side1, side2, side3):
    squareSide1 = side1 * side1
    squareSide2 = side2 * side2
    squareHypotnuse = side3 * side3
    if(squareSide1 + squareSide2 == squareHypotnuse):
        print("These three sides form a right triangle")
    else:
        print("These three sides do not form a right triangle")

# numInput1 = int(input("Enter side 1: "))
# numInput2 = int(input("Enter side 2: "))
# numInput3 = int(input("Enter side 3: "))
# rightTriangle(numInput1, numInput2, numInput3)


#Question 4
def evenOrOdd(numInput):
    if(numInput % 2 == 0):
        print("The number is even")
    else:
        print("The number is odd")

# numInput = int(input("Enter a number and I will tell you if it is even or odd: "))
# evenOrOdd(numInput)