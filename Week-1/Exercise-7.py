"""
Have a look at the script called 'human-guess-a-number.py' (in the same folder as this one).

Your task is to invert it: You should think of a number between 1 and 100, and the computer 
should be programmed to keep guessing at it until it finds the number you are thinking of.

At every step, add comments reflecting the logic of what the particular line of code is (supposed 
to be) doing. 
"""

from random import randint

def check_int(s):
    """ Check if string 's' represents an integer. """
    # Convert s to string
    s = str(s) 

    # If first character of the string s is - or +, ignore it when checking
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    
    # Otherwise, check the entire string
    return s.isdigit()

def input_integer(prompt):
    """ Asks user for an integer input. If valid, the string input is returned as an integer. """
    my_number = input(prompt) # Ask the user for their guess
    while not check_int(my_number): # Repeat until the user inputs a valid integer
        print('My chosen integer number')
        my_number = input(prompt)  
    return int(my_number)

def guess_computer(last_guess,higher): # par dichotomie
    if higher :
        return int(last_guess*3/2)
    else :
        return int(last_guess*1/2)

my_number = input_integer("I choose a number (1-100): ")

guess = 50 

while guess != my_number: # Repeat until the user guesses.
    print ("computer guess: ")
    print (guess)
    if guess < my_number :
        print("Your guess is too low!")  
        guess = guess_computer(guess,True)
    else :
        print("Your guess is too high!\n")
        guess = guess_computer(guess,False)

print ("computer guess: ")
print (guess)
print("You win! The number was indeed " + str(my_number))