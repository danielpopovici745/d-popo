"""
Ask the user to enter three
numbers. Add together the first
two numbers and then multiply
this total by the third. Display the
answer as The answer is
[answer]. 
"""

numOne = int(input("Please enter your first integer "))
numTwo = int(input("Please enter your second integer "))
numThree = int(input("Please enter your third integer "))

equation = (numOne + numTwo) * numThree

print("Your answer is\n" + str(equation))