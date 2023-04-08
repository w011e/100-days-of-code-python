#random integer module 
import random

#range of .randint(from, to)
random_integer = random.randint(1, 100)
print(random_integer)

#0.0000 - 0.99999 ...
random_float = random.random()
print(random_float)

#create random_float between 0.000... and 4.9999 ...
random_float = random_float * 5
print(random_float)