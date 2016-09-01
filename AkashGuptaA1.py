def getUserName():  # Asks the name from the user and saves it.
    global name
    name = input("Please enter your name:")
    while name == '' or len(name) > 27:
        print("Your name cannot be blank and must be <= 15 characters")
        name = input("Please enter your name:")
    return name


def Menu():  # The function displays the menu of choices user can make to run the software.
    menuChoice = input("Menu: \n\
R - List required items.   \n\
C - List completed items. \n\
A - Add new item. \n\
M - Mark an item as completed.\n\
Q - Quit. \n")
    return menuChoice


def main():  # main function of the program shopping list
    print("Shopping List 1.0 - by Akash Gupta")
    getUserName()
    while True:
        Choice = Menu()
        if Choice == 'r' or Choice == 'R':


        elif Choice == 'c' or Choice == 'C':

        elif Choice == 'a' or Choice == 'A':

        elif Choice == 'm' or Choice == 'M':

        elif Choice == 'q' or Choice == 'Q':

            break
        else:
            print("Invalid menu choice. Please try again.")


main()  # calls the main function
