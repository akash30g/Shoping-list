
from operator import itemgetter,attrgetter,methodcaller
import csv

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
Q - Quit. \n\
>>>")
    return menuChoice

def readList(shopItem):
    count = 0
    output_info = "Required items:\n"
    totalPrice = 0
    shopItem = sorted(shopItem, key=itemgetter('Priority'))
    for every_product in shopItem:
        output_info += "{0:}. {1:22}$ {2:.2f} ({3})\n".format(count, every_product["Name"], every_product["Price"],
                                                       every_product["Priority"])
        count =count+1
        totalPrice += every_product["Price"]
    print(output_info + "Total expected price for {} items: $ {}".format(count, totalPrice))

    return shopItem

def writeList():
    file_write = open('list.txt', 'w')
    for each_line in file_write:
        datum = each_line.split(",")
        file_write.write("{:s}\t:${:s}\t({:s})".format(datum[0], datum[1], datum[2], datum[3]))
    file_write.close()


def main():  # main function of the program shopping list
    print("Shopping List 1.0 - by Akash Gupta")
    shopItem = []
    getUserName()
    print("Hi {} Let's go for shopping!!!".format(name))

    while True:
        Choice = Menu()
        if Choice == 'r' or Choice == 'R':
            numline = sum(1 for line in open("items.csv","r"))
            print("{} items loaded from items.csv".format(numline))
            file = open("items.csv", "r")
            for each_line in file:
                datum = each_line.split(",")
                Item = {"Name": datum[0], "Price": float(datum[1]), 'Priority': int(datum[2]), "Type": datum[3]}

                shopItem.append(Item)
            readList(shopItem)

        #elif Choice == 'c' or Choice == 'C':

        elif Choice == 'a' or Choice == 'A':
            writeList()
        #elif Choice == 'm' or Choice == 'M':

        #elif Choice == 'q' or Choice == 'Q':

           # break
        else:
            print("Invalid menu choice. Please try again.")


main()  # calls the main function
