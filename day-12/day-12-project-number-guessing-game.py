from random import randint
from os import system

system("clear")
difficulty_level = input("Welcome to the number guessing game!\n I'm thinking of a number between 1 and 100.\n Choose a difficulty. Type 'easy' or 'hard': ").lower()

random_number = randint(1,101)
# print(random_number)

def compare_numbers():
    guessing_ongoing = True
    global number_of_attempts
    while guessing_ongoing:
        if number_of_attempts > 0:
            print(f"You have {number_of_attempts} attempts remaining to guess the number.") 
            guessed_number = input("Guess a number: ")
            try:
                guessed_number = int(guessed_number)
            except ValueError:
                print("Invalid input! Please enter a number.")
                continue
            if guessed_number == random_number:
                print(f"Congratulations. You guessed the correct number!")
                guessing_ongoing = False
            elif guessed_number > random_number:
                print("Too high.\n Guess again.")
            elif guessed_number < random_number:
                print("Too low.\n Guess again.")    
            number_of_attempts -= 1
        else:    
            guessing_ongoing = False
            print("You loose.")

if difficulty_level == "easy":
    number_of_attempts = 10
    compare_numbers()
elif difficulty_level == "hard":
    number_of_attempts = 5
    compare_numbers()
else:
    print("You've inserted the wrong text. Please try again.")