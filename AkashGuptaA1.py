
from operator import itemgetter,attrgetter,methodcaller
import csv

def getUserName():  # Asks the name from the user and saves it.
    global name
    name = input("Please enter your name:")
    while name == '' or len(name) > 15:
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

def readList_required(shopItem,numline):
    count = 0
    output_info = "Required items:\n"
    totalPrice = 0
    shopItem = sorted(shopItem, key=itemgetter('Priority'))
    for every_product in shopItem:
        output_info += "{0:}. {1:22}$ {2:.2f} ({3})\n".format(count, every_product["Name"], every_product["Price"],
                                                       every_product["Priority"])
        count =count+1
        totalPrice += every_product["Price"]
    print("{} items loaded from items.csv".format(len(shopItem)))
    print(output_info + "Total expected price for {} items: $ {}".format(count, totalPrice))

    return shopItem


def writelist(shopItem):
    checkProductPrice= True
    checkProductPriority = True
    product_name = input("Please enter the product name:").capitalize()
    while product_name == '' or len(product_name) > 15:
        print("the item name cannot be blank and must be < 15 characters")
        product_name = input("Please enter the product name:").capitalize()
    while checkProductPrice:

        try:
            product_price = int(input("Price: $"))
            if product_price < 0:
                print("Price must be >= 0")
            else:
                checkProductPrice = False
        except ValueError:
            print("Invalid input; Please, enter a valid number")


    while checkProductPriority:

        try:
            product_priority = int(input("Priority:"))
            if product_priority < 0 or product_priority > 3:
                print("Priority must be 1, 2 or 3")
            else:
                checkProductPriority = False


        except ValueError:
            print("Invalid input; Please, enter a valid number")
    added_item= {"Name": product_name, "Price": product_price, "Priority": product_priority}
    shopItem.append(added_item)

    return shopItem

def markProduct(shopItem):
    checkflag = True
    if len(shopItem) == 0:
        print("No  items in the list")
    else:
        readList_required(shopItem)
        while checkflag:
            try:
                chooseItem = int(input("Enter the number of the item to mark as completed\n>>>"))
                if chooseItem < 0 or chooseItem > len(shopItem) - 1:
                    print("Invalid item number", end="\n\n")
                else:
                    item_marked = shopItem[chooseItem-1]
                    print("{} marked as completed".format(item_marked["Name"]))
                    checkflag = False
            except ValueError:
                print("Invalid input; enter a valid number", end="\n\n")

    return item_marked

def main():  # main function of the program shopping list
    print("Shopping List 1.0 - by Akash Gupta")
    shopItem = []
    listCompleted = []
    getUserName()
    print("Hi {} Let's go for shopping!!!".format(name))
    numline = sum(1 for line in open("items.csv", "r"))
    file = open("items.csv", "r")
    for each_line in file:
        datum = each_line.split(",")
        Item = {"Name": datum[0], "Price": float(datum[1]), 'Priority': int(datum[2]), "Type": datum[3]}
        shopItem.append(Item)
    while True:
        Choice = Menu()
        if Choice == 'r' or Choice == 'R':

            readList_required(shopItem,numline)

        elif Choice == 'c' or Choice == 'C':
            readList_completed(listCompleted)

        elif Choice == 'a' or Choice == 'A':
            writelist(shopItem)
        elif Choice == 'm' or Choice == 'M':
            deleteitem = markProduct(shopItem)
            shopItem.remove(deleteitem)
            listCompleted.append(deleteitem)
        elif Choice == 'q' or Choice == 'Q':
            print("Thanks for shopping \nHave a nice day!! :)")
            break
        else:
            print("Invalid menu choice. Please try again.")
    addcsvList(shopItem)

main()  # calls the main function





