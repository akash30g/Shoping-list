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

def readList():                    #this function allows the user to view the score saved in the score.txt file
    file=open('list.txt','r')
    i=1
    for each_line in file:
        datum = each_line.split(",")

        print("{:s}\t:${:s}\t({:s})".format(datum[0], datum[1], datum[2]))

    fContents=file.read()
    print(fContents)
    file.close()
    return True

def writeList():
    file_write = open('list.txt', 'w')
    for each_line in file_write:
        datum = each_line.split(",")

        datum[0]= 2
        datum[1]= 3
        datum[2] = 4
        file_write.write("{:s}\t:${:s}\t({:s})".format(datum[0], datum[1], datum[2]))
    file_write.close()


def main():  # main function of the program shopping list
    print("Shopping List 1.0 - by Akash Gupta")
    getUserName()
    while True:
        Choice = Menu()
        if Choice == 'r' or Choice == 'R':
            readList()

        #elif Choice == 'c' or Choice == 'C':

        elif Choice == 'a' or Choice == 'A':
            writeList()
        #elif Choice == 'm' or Choice == 'M':

        #elif Choice == 'q' or Choice == 'Q':

           # break
        else:
            print("Invalid menu choice. Please try again.")


main()  # calls the main function
