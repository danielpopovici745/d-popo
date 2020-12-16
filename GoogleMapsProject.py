#! python3
# mapIt.py - Launches a map in the browser using an address from the
# command line
import webbrowser, sys, pyperclip

# Get address from user
while True: 
  address = input("Please enter your address! ")
  while True:
    try:
      answer = int(input("\nIs this address correct?" + "\n" + address + "\nEnter 1 for yes and 2 for no\n" ))
      break
    except ValueError:
      print("\n\033[1mPlease enter a 1 or 2!\033[0m")
  if answer ==2:
    continue
  else:
    webbrowser.open('https://www.google.com/maps/place/' + address)
    break
#hello is this working