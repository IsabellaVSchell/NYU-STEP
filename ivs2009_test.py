# Question 1
# for i in range(1, 100):
#     if i % 4 == 0: 
#         if i % 5 == 0:
#             print("SoftBall")
#         else:
#             print("Soft")
#     elif i % 5 == 0:
#         print("Ball")
#     else:
#         print(i)


#Question 2
def Fibonacci(numInput):
    newNum = 0
    prevNum1 = 0
    prevNum2 = 0
    sequence = [1, 1]
    if numInput == 1:
        print(1)
    elif numInput == 2:
        print(1)
    else:
        for i in range(3, numInput + 1):
            prevNum1 = sequence[i - 2]
            prevNum2 = sequence[i - 3]
            newNum = prevNum1 + prevNum2
            sequence.append(newNum)
        print(sequence[i - 1])
numInput = int(input("Enter a number and I will tell you that number in the Fibonacci numbers sequence: "))    
Fibonacci(numInput)