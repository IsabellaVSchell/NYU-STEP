# #Question 1
# import random 
# num = random.randint(1,100)
# guessesLeft = 5
# counter = 0
# low = 1
# high = 100

# print("I thought of a number between 1 and 100! Try to guess it. ")

# while guessesLeft > 0:
#     low = str(low)
#     high = str(high)
#     print("Range ["+ low + "," + high+ "] Number of guesses left:", guessesLeft)
#     low = int(low)
#     high = int(high)
#     numInput = int(input("Your guess: "))
#     guessesLeft -= 1
#     counter += 1
#     if(numInput == num):
#         print("Correct! You guessed my number in", counter, "guesses")
#         break
#     elif(numInput < low):
#         print("I already told you it's bigger than that number!")
#         guessesLeft += 1
#         counter -= 1
#     elif(numInput > high):
#         print("I already told you it's smaller than that number!")
#         guessesLeft += 1
#         counter -= 1
#     elif(numInput > num):
#         print("Wrong! My number is smaller!")
#         high = numInput- 1
#     else:
#         print("Wrong! My number is bigger!")
#         low = numInput + 1
# else: 
#     num = str(num)
#     print("My number was", num+ "!")



#Question 2

# userInput = int(input("Enter the maximum number of rows you want printed: "))
# counter = 1
# while counter <= userInput:
#     for i in range(1, counter +1):
#         print(i, end=" ")
#     print("")
#     counter += 1



# #Question 3

# print("We're going to add all numbers from the lower limit to the upper limit.")
# lower = int(input("Enter your lower limit: "))
# upper = int(input("Enter your upper limit: "))
# total = 0
# for i in range(lower, upper + 1):
#     total += i
# print("The sum from", lower, "to", upper, "equals", total)