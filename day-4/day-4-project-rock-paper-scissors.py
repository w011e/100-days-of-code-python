import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]
human = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer = random.randint(0, 2)

# option
# if human == 0:
#     print(f"You chose {rock}")
# elif human == 1: 
#     print(f"You chose {paper}")
# else:
#     print(f"You chose {scissors}")
          
# if computer == 0:
#     print(f"Your mate chose {rock}")
# elif human == 1: 
#     print(f"Your mate chose {paper}")
# else:
#     print(f"Your mate chose {scissors}")

# if human == 0 and computer == 0: 
#     print("Repeat.")
# elif human == 0 and computer == 1:
#     print("Paper wraps Rock. You lose.")
# elif human == 0 and computer == 2: 
#     print("Rock beats scissors. You win.")
# elif human == 1 and computer == 0: 
#     print("Paper wraps Rock. You win.")
# elif human == 1 and computer == 1:
#     print("Repeat.")
# elif human == 1 and computer == 2: 
#     print("Scissors cut paper. You lose.")
# elif human == 2 and computer == 0: 
#     print("Rock beats scissors. You lose.")
# elif human == 2 and computer == 1: 
#     print("Scissors cut paper. You win.")
# elif human == 2 and computer == 2: 
#     print("Repeat.")
# else:
#     print("You typed and invalid number. You lose.")

if human >= 3 or human < 0: 
    print("You typed an invalid number. You lose.")
else:
    print(f"You chose: {game_images[human]}")
    print(f"Your mate chose: {game_images[computer]}")

    if human == 0 and computer == 2:
        print("You win.")
    elif human == 2 and computer == 0:
        print("You lose.")
    elif computer > human:
        print("You lose.")
    elif computer < human: 
        print("You win.")
    elif human == computer: 
        print("It's a draw.")