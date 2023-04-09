import random 

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# number_of_people = len(names)

# random_choice = random.randint(0, number_of_people-1)
# person_to_pay = names[random_choice]

#option also to use random.choice()
person_to_pay = random.choice(names)
print(f"{person_to_pay} is going to buy the meal today!")