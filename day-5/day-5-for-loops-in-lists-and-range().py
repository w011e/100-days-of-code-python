#for item in list_of_items 
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
#identation matters! here print(fruit) is not possible, since variable is only assigned within for loop 
print(fruits)

#for number in range(start, not included end, step)
total = 0 
for number in range(1, 101):
    total += number
print(total)