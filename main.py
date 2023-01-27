#Modules being imported
from random import choice

#Takes input from user to know how many items we will be wanting to randomly choose from
max_length = int(input("Enter the number of how many items to choose from: "))

picker = []

#Takes input from user for what they want to randomly choose and stores them in strings
while len(picker) < max_length:
    thing = input('Enter items to choose from: ')
    if thing not in picker:
        picker.append(thing)
        continue

print('The chooser has chosen for you:\n'
+choice(picker))

