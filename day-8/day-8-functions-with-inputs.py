#simple function 
def greet():
    print("Hey Angela")
    print("How do you do Pete?")
greet()

#function that allows for input 
def greet_with_name(name): 
    print(f"Hello {name}")
    print(f"How do you do {name}?")

greet_with_name("Tim")
greet_with_name("Tom")
greet_with_name("Tam")

#functions with more than 1 input 
#positional artgument
def greet_with(name, location):
    print(f"Hello {name}!")
    print(f"What is it like in {location}?")
greet_with("Jenna", "Berlin")

