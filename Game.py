import random # to generate random number

chances = 0 # checks for no. of chances

def Numbers_game(): # Function of game
    global chances # to access local variable chances
    target = random.randint(1,100) # from 1 to 100
    guessed_number = int(input(""" Guess the right Number from 1 to 100. You got only 3 chances.
 """))
    if guessed_number == target:
            print("You guessed the right number")
            chances = 3
    elif guessed_number < 1 or guessed_number > 100:
            print("Please Choose between 1 to 100 only")
            chances += 1
    elif guessed_number > target:
            print("Your number is greater than the target number")
            chances += 1
    elif guessed_number < target:
            print("Your number is less than the target number")
            chances += 1

while chances <= 3:
    
    if chances == 3:
        print("Game Over")
        ask = input("You wanna play again?? (Y/N): ")
        if ask == "Y" or ask == "y":
            chances = 0
            Numbers_game()
        else:
            print("Thanks for playing")
            break
    elif chances < 3:
        Numbers_game()