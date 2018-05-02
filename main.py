import os
import image

def title_bar():
    """Return title bar
    """

    os.system('clear')

    print("--------------------------------------")
    print("  Big Computational Image Processing  ")
    print("--------------------------------------")

def user_menu():
    """Display user menu
    
    Returns:
        integer -- Return value to choose menu
    """

    print("1. Load Images")
    print("2. Basic Function")
    print("3. Filter")
    print("4. Exit")

    return int(input("Choose menu : "))


## MAIN PROGRAM ##
choice = 0
# Show title bar
title_bar()

while(choice != 4):
    choice = user_menu()

    # Respond user choice
    title_bar()
    if (choice == 1):
        print("Hello")
    elif (choice == 2):
        print("Hai")
    elif (choice == 3):
        print("Okeey")
    elif (choice == 4):
        print("Oops..")
    else:
        print("I didn't understand with that choice")