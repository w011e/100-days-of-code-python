#Calculator functions

from day_10_project_art import logo
from os import system

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

#Store the calculator functions in a dictionary
#Note that "add" is referring to the add() function formulated above
#calculator functions are stored as value 
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

#Recursion 
#technique where function calls itself repeatedly to solve a problem
#process continues until base case is reached, which stops the recursion
#powerful for solving complex problems, but it can also be tricky to use correctly
#Careful condition like if must be met in order to call the function within a function !

def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    
    #Setting a flag

    should_continue = True 

    while should_continue:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the second number?: "))

        #Make use of stored calculator function within dict by respective calling key (operation_symbol)
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        #Introcude condition to call the calculator() again 
        if input(f'Type "y" to continue calculating with number, or type "n" to start a new calculation: ').lower() == "y":
            num1 = answer
        else:
            should_continue = False
            system("clear") 
            calculator()

calculator()