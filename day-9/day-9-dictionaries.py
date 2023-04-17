#Value = {"Key": "Value"} e.g.
programming_dictionary = {
    "Bug": "An error in a programm that prevents program from running as expected.",
    "Function": "A piece of code that you can easily call "
}

#Retrieing items from dictionary
print(programming_dictionary["Bug"], programming_dictionary["Function"])
print(len(programming_dictionary))

#Adding new items 
programming_dictionary["Loop"] = "Action of doing something over and over again."
print(programming_dictionary)
print(len(programming_dictionary))

#Create an empty dictionary
empty_dictionary = {}

#Wipe existing dictionary 
programming_dictionary = {}
print(programming_dictionary)
print(len(programming_dictionary))

#Edit an item in the dictionary 
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)

#Loop through a dictionary
for key in programming_dictionary: 
    #Print Key Only 
    print(key)
    #Print value of respective key
    print(programming_dictionary[key])