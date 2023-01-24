#import packages
import sys
import random

#assign the randomly generated number to correct_guess
correct_guess = random.randint(0,20)
print("Welcome!! mortal!! to survive you need to quess the right number else your demise is a mystery for the smartest men to tread on ")
your_guess = None
#code block for the game decisions
while your_guess != correct_guess:
    your_guess = input("what Number do you have in mind mortal:  ")
    print(your_guess)
    your_guess = int(your_guess)
    if your_guess > 20:
        your_guess = input("Invalid Guess you mortal!! try again")
        your_guess= int(your_guess)
    if your_guess > correct_guess:
        print("Dear Mortal your guess is too much")
    elif your_guess < correct_guess:
        print("Mortal your guess is rather small")
    else:
        print("mortal welcome to the league of the gods")
    break
print("thank you for playing")
input("Enter any key to quit.")  
sys.exit() 


