#import required packages
import random
import string
import sys
#generate alphabets both capital and lowercase letters using this string
letter = list(string.ascii_letters)

#for loop to convert generated alphabets to list
l = []
for b in letter:
    str(b)
    l.append(b)

#list of numbers 
number = ["1","2","3","4","5","6","7","8","9","0"]
print("The password Generator")

#request input from user on how many letters and numbers would be required in the password
k = input("How many letters would you like in your password: ")
k = int(k)
s = input("How many numbers would you like in your password: ")
s = int(s)

#generate random samples from the letters and numbers list
letters_select = random.sample(l, k)
numbers_select = random.sample(number, s)

#combine the result of generated random numbers to each other
letters_select.extend(numbers_select)

#shuffle them for maximum randomization
random.shuffle(letters_select)

#convert generated password to string and display to the user
password = ""
for x in letters_select:
    str(x)
    password += " " +(x)
print("Dear User your generated password is: " + password)
input("Enter any key to quit.") 
sys.exit() 
