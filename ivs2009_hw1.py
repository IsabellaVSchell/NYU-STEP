#Question 1 

# print("Please enter how much of each bill you have:")
# fiveHundred = int(input("# of $500 bills:"))
# oneHundred = int(input("# of $100 bills:"))
# fifty = int(input("# of $50 bills:"))
# twenty = int(input("# of $20 bills:"))
# ten = int(input("# of $10 bills:"))
# five = int(input("# of $5 bills:"))
# one = int(input("# of $1 bills:"))

# fiveHundredTotal = fiveHundred * 500
# oneHundredTotal = oneHundred * 100
# fiftyTotal = fifty * 50
# twentyTotal = twenty * 20
# tenTotal = ten * 10
# fiveTotal = five * 5
# oneTotal = one * 1

# total = fiveHundredTotal + oneHundredTotal + fiftyTotal + twentyTotal + tenTotal + fiveTotal + oneTotal

# print("Your Monopoly hand totals to $" + str(total))


#Question 2

# lastName,firstName = input("Enter your last name and then first name: ").split()
# print("Hi", firstName, lastName )

#Question 3

# xInput = int(input("Enter an integer:"))
# x = xInput
# multiplyX = xInput * xInput
# exponentX = 2
# for i in range(1,x):
#     exponentX *= 2
# total = multiplyX + xInput + exponentX
# print("x+x^2+2^x=", total)


#Question 4
# print("Enter the past seven temperatures separated by a comma:")
# firstDay,secondDay,thirdDay,fourthDay,fifthDay,sixthDay,seventhDay = input("").split(",")
# firstDay = float(firstDay)
# secondDay = float(secondDay)
# thirdDay = float(thirdDay)
# fourthDay = float(fourthDay)
# fifthDay = float(fifthDay)
# sixthDay = float(sixthDay)
# seventhDay = float(seventhDay)
# addDays = firstDay + secondDay + thirdDay + fourthDay + fifthDay + sixthDay + seventhDay
# average = addDays / 7
# average = int(average)
# print("The average temperature of the past seven days is", average, "degrees")