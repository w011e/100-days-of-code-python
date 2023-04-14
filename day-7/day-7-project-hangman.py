import random
from hangman_art import logo, stages
# from word_list import word_list
end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

print(chosen_word)

display = []
for letter in chosen_word:
    display.append("_")

print(logo)

while not end_of_game:
    guess = input("Please guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display) 

    if lives == 0:
        end_of_game = True
        print("You lose.")
    elif "_" not in display: 
        end_of_game = True
        print("You win")
    elif guess not in chosen_word:
        lives -= 1
        print(stages[lives])