# scope

# local scope within functions 

def drink_potion():
    potion_strength = 2
    print(potion_strength)

    #local scope, completely new variable printed
    #don't use same names for variables 

drink_potion()

# global scope 
player_health = 10

def drink_potion():
    potion_strength = 2
    print(player_health)

drink_potion()

# there is no block scope 
game_level = 3
def create_enemy():
    enemies = ["Skeleton", "Zombies", "Aliens"]
    if game_level < 5:
        new_enemy = enemies[0]
    print(new_enemy)

# modifying global scope

enemies = 1

def increase_enemies():
    # !!! to modify variable of global scope
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# but !!! try to avoid local scope within functions !
# make use of retrun 

enemies = 1

def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

# global constants 

PI = 3.14159
URL = "..."
# type constants uppercase :=)