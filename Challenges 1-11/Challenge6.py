'''
Ask how many slices
of pizza the user
started with and ask
how many slices
they have eaten.
Work out how many
slices they have left
and display the
answer in a userfriendly format. 
'''


numOfSlices = int(input("Dude sweet pizza how many slices did you get? "))
slicesEaten = int(input("How many did you eat? "))
numLeft = numOfSlices - slicesEaten
print("Oh so that means you have " + str(numLeft) + " for me!")