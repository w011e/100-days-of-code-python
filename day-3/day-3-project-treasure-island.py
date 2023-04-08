print('''
__
                      /` ,\__
                     |    ).-'
                    / .--'
                   / /
     ,      _.==''`  \
   .'(  _.='         |
  {   ``  _.='       |
   {    \`     ;    /
    `.   `'=..'  .='
      `=._    .='
          '-`\\`__
            `-._{    ''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

choice1 = input('You\'re at a crossroad. Where do you want to got? Type "Left" or "Right".').lower()

if choice1 == "left": 
    print("Fall into a hole.\nGame over.")
elif choice1 == "right": 
    choice2 = input("Swim or Wait? ").lower()
    if choice2 == "swim":
        print("Attacked by trout.\nGame over.")
    elif choice2 == "wait":
        choice3 = input("Which door: Red, Blue, Yellow? ").lower()
        if choice3 == "red":
            print("Burned by fire.\nGame over.")
        elif choice3 == "blue":
            print("Eaten by beasts.\nGame over.")
        elif choice3 == "yellow":
            print("You win!")
        else:
            print("Game over.")
    else: 
        print("Attacked by trout.\nGame over.")    
else:
    print("Fall into a hole.\nGame over.")