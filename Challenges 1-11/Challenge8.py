'''
Ask for the total price of the bill, then ask how
many diners there are. Divide the total bill by the
number of diners and show how much each
person must pay
'''

totalPrice = float(input("How much was the price of the dinner? "))
numOfDiners = float(input("How many diners were there? "))
pricePerDiner = totalPrice / numOfDiners
print("Each diner shoud pay " + str(pricePerDiner))