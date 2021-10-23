#Placeholders
sentence = "This is a sentence {} with a placeholder".format("Example")
print(sentence)

#Setting placeholders to indexes
newSentence = "My name is {0} and I like to {1} and {2} with my dog {3}".format("Isabella", "read", "write", "Dori")
anotherSentence = "My name is {3} and I like to {2} and {1} with my dog {0}".format("Isabella", "read", "write", "Dori")
print(newSentence)
print(anotherSentence)

#Using variables with the placeholders
variableSentence = "My name is {myName} and I like to {hobby1} and {hobby2} with my dog {myDog}".format(myName = "Isabella", myDog = "Dori", hobby1 = "read", hobby2 = "write")
print(variableSentence)

#Print sentence with placeholders without establishing a variable
print("My name is {3} and I like to {2} and {1} with my dog {0}".format("Isabella", "read", "write", "Dori"))

#Printing with a return 
print("This line has \na return in it")

#Printing with a tab space 
print("This line has \ta tab space in it")

#Printing quotes
print("This sentence has single 'quotes'")
print('This sentence also has single \'quotes\'')
print('This sentence has double "quotes"')
print("This sentence also has double \"quotes\"")


#Comparison operators(evaluate to true or false)
#Equality operator -  ==
print(2==3)
#Inequality operator - !=
print(2 != 3)
#Greater than - >
print(2>3)
#Greater than or equal to - >=
print(2>=3)
#Less than - <
print(2<3)
#Less than or equal to - <=
print(2<=3)

#Evaluate multiple expressions at the same time
#And - &&
#Or - ||
#Not - !

#Order of operations still exist in coding

#Take multiple inputs at once 
input1,input2 = input("Enter two inputs seperated by a space: ").split()
print(input1)
print(input2)

#Have inputs inputed seperated by a comma(Or something else)
input3,input4 = input("Enter two inputs seperated by a comma: ").split(",")
print(input3)
print(input4)

input5,input6 = input("Enter two inputs seperated by a forward slash: ").split("/")
print(input5)
print(input6)