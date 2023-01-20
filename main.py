from random import choice

picker = []

#to change how many inputs
max_length = int(input("Enter the number of how many items to choose from: "))


while len(picker) < max_length:
    thing = input('Suggested Movie/TV Show/Video Game/Task/Restaurant: ')
    if thing not in picker:
        picker.append(thing)
        continue

print('Suggested Movie/TV Show/Video Game/Task/Restaurant that we are going to do:\n'
+choice(picker))
