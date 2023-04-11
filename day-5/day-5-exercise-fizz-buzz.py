#write a program that automatically prints the solution to the FizzBuzz game
#print each number from 1 to 100 in turn
#divisible by 3? print "Fizz" instead
#divisible by 5? print "Buzz" instead
#divisible by both 3 and 5? print "FizzBuzz" 

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 5 == 0: 
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)
