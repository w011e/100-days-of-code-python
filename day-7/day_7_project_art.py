import random
from day_7_project_art import logo

from day_7_word_list import word_list
end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

print(logo)
print(chosen_word)

display = []
for letter in chosen_word:
    display.append("_")

while not end_of_game:
    guess = input("Please guess a letter: ").lower()

    if guess in display: 
        print(f"You've already guessed the letter {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"The chosen letter {guess} is not part of the word. You lose a life.")
        
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

        from day_7_project_art import stages
    
    print(f"{' '.join(display)}")

    if "_" not in display: 
        end_of_game = True
        print("You win")
    
    from day_7_project_art import stages
    print(stages[lives]) # type: ignore