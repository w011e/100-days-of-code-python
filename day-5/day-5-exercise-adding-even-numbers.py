#write program that calculates  sum of all the even numbers from 1 to 100

#Option1
total1 = 0 
for number in range(1, 101):
    if number % 2 == 0:
        total1 += number
print(total1)

#Option2
total2 = 0
for number in range(2, 101, 2):
    total2 += number
print(total2)