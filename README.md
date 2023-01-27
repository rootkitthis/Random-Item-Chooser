# Random Item Chooser
This is a simple project that I have been working to kinda kick start my python development experience. 

When I was dating my now wife during the Christmas time we were struggling to figure out what Christmas movie to watch.  I decided to build something to automate that selection.   It has now morphed into more of a what are we doing, where are we eating, what show, movie or video game am I playing tool. It is fun project that I have redone several times as I have been learning and growing my python knowledge and experience.   

## Requirements / Modules needed
in the current state of the script no external modules are needed to be imported.  Currently I am using just the built in Random Module as seen in this line of code

    from random import choice

More detailed information about the imported modules can be found here: 

[Random Module Documentation](https://docs.python.org/3/library/random.html#module-random)




## Executing the script
When the script is downloaded it can be triggered via many IDEs or via terminal. 

For me personally I have been executing the command either in terminal or in various IDEs (mostly Pycharm) 

For running it in Terminal I use the command: 

    python3 <path to script> 
example: 

    python3 /Users/mac/desktop/Random

## Explanation of how the script works

When you run the script it will ask the for user input for how many items we want to randomly choose from and stores the value in the variable *max_length*. 
As seen in this part of the code: 

    max_length = int(input("Enter the number of how many items to choose from: "))

After the value of how many items we want to randomly choose from the script takes user input of what items we want to choose from and stores those values in the variable called *thing* and repeats the process as long for however many times we choose and stored in *max_length* as long as the item is not already entered from the user.   The script then takes the items from the user and adds them to an empty variable called *picker*.
As seen in this part of the code: 

    picker = []
    
    while len(picker) < max_length:  
    thing = input('Enter items to choose from: ')  
    if thing not in picker:  
        picker.append(thing)  
        continue
After all of this is done the script then randomly chooses an item from the *picker* variable and prints out the information. 
As seen in the last part of the code: 

    print('The chooser has chosen for you:\n' + choice(picker))

