color = ["red", "white", "black"]
number = [ 0, 00, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]

import random

def spin():
    x = random.choice(color)
    y = random.choice(number)
    print("Your color is:", x, y)
    if x == "red":
        print("You won ", (wager * 2 + "dollars"))
    if x == "black":
        print("You lost, try again next time.")
    if x == "white":
        print("You won big", (wager * 10, "dollars"))
    if 
    
print("Would you like to spin the wheel?")
answer = input()
if answer == "yes":
    print("How much would you like to wager? ")
    wager = int(input())
    print("What color would you like to bet on? ")
    b = input()
    print("What number would you like to bet on? ")
    n = int(input())
    spin()
        
    

else:
    print("Maybe another time. Thanks for dropping by the casino. ")
