
from operator import itemgetter                                         # importing dictionarry operator to sort items

def getUserName():                                                      # declaring function to ask user name
    user_name = input("Please enter your name:")                        # asking user for hi/her name
    while user_name == '' or len(user_name) > 15:                       #validaion of the user input
        print("Your name cannot be blank and must be <= 15 characters") # error message
        user_name = input("Please enter your name:")                    # asking the user name again
    print("Hi {} Let's go for shopping!!!".format(user_name))           # printing user name and greeting to user

def Menu():                                                             # defining the function that displays the menu of choices user can make to run the software.
    menuChoice = input("Menu: \n\
R - List required items.   \n\
C - List completed items. \n\
A - Add new item. \n\
M - Mark an item as completed.\n\
Q - Quit. \n\
>>>")                                                                   # displaying menu and asking user for his choice
    return menuChoice                                                   # returning the choice

def readList_required(ItemList):                                        # defining the function to read the list required
    if len(ItemList)== 0:                                               # checking if there is items on the list or not
        print("No required Items")
        print("{} items loaded from items.csv".format(len(ItemList)))
    else:                                                               # if there there are items in the list
        count = 0                                                       # declaring integer variable to display output in numbering format
        output_info = "Required items:\n"                               # declaring string variable and will be used to display output
        totalPrice = 0                                                  # declaring integer variable to show total price of the list
        ItemList = sorted(ItemList, key=itemgetter('Priority'))         # sorting list based on priority
        for every_product in ItemList:                                  # loop for every item in list
            output_info += "{0:}. {1:22}$ {2:.2f} ({3})\n".format(count, every_product["Name"], every_product["Price"],
                                                       every_product["Priority"])  # formatting how to diaplay the output
            count =count+1                                              # increment in count for numbering
            totalPrice += every_product["Price"]                        # calculating total price of the list
        print("{} items loaded from items.csv".format(len(ItemList)))    # displaying total number of items in list
        print(output_info + "Total expected price for {} items: $ {}".format(count, totalPrice)) # displayinf the formatted output
    return ItemList                                                     # returning the list

def writelist(shopItem):                                                # defining function to add items to the list
    checkProductPrice= True                                             # declaring boolean variable to check and end error cheching while loop for price
    checkProductPriority = True                                         # declaring boolean variable to check and end error checking while loop for priority
    product_name = input("Please enter the product name:").capitalize() # asking the name of product and capitalizing tbe first letter
    while product_name == '' or len(product_name) > 15:                 # checking validity of product name.
        print("the item name cannot be blank and must be < 15 characters")
        product_name = input("Please enter the product name:").capitalize()
    while checkProductPrice:                                            # loop for asking user for product price and error checking
        try:
            product_price = float(input("Price: $"))                    # asking the user a float value price.
            if product_price < 0:                                       # price cannot be less than 0
                print("Price must be >= 0")
            else:
                checkProductPrice = False                               # valid iput will get out of the loop
        except ValueError:
            print("Invalid input; Please, enter a valid number")        # print error for any invalid value
    while checkProductPriority:                                         # loop for asking user for product priority and error checking
        try:
            product_priority = int(input("Priority:"))                  # asking the user an int value priority.
            if product_priority < 0 or product_priority > 3:            # priority can only be 1,2 or 3
                print("Priority must be 1, 2 or 3")
            else:
                checkProductPriority = False
        except ValueError:
            print("Invalid input; Please, enter a valid number")
    added_item= {"Name": product_name, "Price": product_price, "Priority": product_priority} # added iten in dictionary
    shopItem.append(added_item)                                         # adding item to main list
    return shopItem                                                     #return the updated required list

def markProduct(shopItem):                                              # defing function to mAerk item as completed
    checkflag = True                                                    # declaring boolean variable to
    if len(shopItem) == 0:                                              # checking if there is items on the list or not
        print("No  items in the list")
    else:                                                               # if there are items in list
        markedList = readList_required(shopItem)                        # calling function to read the list and stroring its return value
        while checkflag:                                                # loop top error check thr input value
            try:
                chooseItem = int(input("Enter the number of the item to mark as completed\n>>>"))   # ask the user for the item number to be deleted
                if chooseItem < 0 or chooseItem > len(shopItem) - 1:    # input should be either equal total items or greater than zero
                    print("Invalid item number", end="\n\n")
                else:
                    item_marked = markedList[chooseItem]                # storing the marked item
                    print("{} marked as completed".format(item_marked["Name"])) # displaying the marked item
                    checkflag = False                                   # exiting the loop
            except ValueError:
                print("Invalid input; enter a valid number", end="\n\n") # error message for invalid value
    return item_marked

def readList_completed(completedList):                                  # defing funtion to read completed list
    count = 0                                                           # declaring integer variable to display output in numbering format
    display = "Completed items:\n"                                      # decalring string variable and will be used to display output
    totalPrice = 0                                                      # declaring integer variable to show total price of the list
    if len(completedList) == 0:                                         # if statement to check whether there is item in list or not
        print("No completed items")
    else:
        completedList = sorted(completedList, key=itemgetter('Priority'))   # sorting list based on priority
        for eachItem in completedList:
            display += "{0:}. {1:18}$ {2:.2f} ({3})\n".format(count, eachItem["Name"], eachItem["Price"],
                                                           eachItem["Priority"])
            count = count+1
            totalPrice += eachItem["Price"]                             # calculating total price of thr list
        print(display + "Total expected price for {} items: $ {}".format(count, totalPrice)) # printing the required output

def addcsvList(listCompleted):                                          # defing function to write list in csv file
    file_writer = open("output.csv", "w")                               # opening the file to write output in csv file
    for each in listCompleted:                                          # for loop started to write in rows
        file_writer.write("{},{},{},c\n".format(each["Name"], each["Price"], each["Priority"])) # giving the format how to write the list
    file_writer.close()                                                 # closing the file

def main():                                                             # main function of the program shopping list
    print("Shopping List 1.0 - by Akash Gupta")
    shopItem = []                                                       # declaring the list variable for displaying rquired list
    listCompleted = []                                                  # declaring the list variable for displaying rquired list
    getUserName()                                                       # calling function to get user name
    file = open("items.csv", "r")                                       # opening the csv file
    for each_line in file:                                              # starting 'for' loop to get items from file into list
        datum = each_line.split(",")                                    # splitting the data to store by comas
        Item = {"Name": datum[0], "Price": float(datum[1]), 'Priority': int(datum[2]), "Type": datum[3]}  # declaring the type data to stored
        shopItem.append(Item)                                           # adding item to the main displaying list
    file.close()                                                        # closing the file
    while True:                                                         # while loop to keep displaying the menu
        Choice = Menu()                                                 # calling the menu function and asking for users choice
        if Choice == 'r' or Choice == 'R':                              # if else statements, based on customers choice,
            shopItem=readList_required(shopItem)                        # calling function to read list required as desired by the the user
        elif Choice == 'c' or Choice == 'C':
            listCompleted=readList_completed(listCompleted)             # calling function to read list completed as desired by the the user
        elif Choice == 'a' or Choice == 'A':
            writelist(shopItem)                                         # calling function to add items in the list as desired by the the user
        elif Choice == 'm' or Choice == 'M':
            deleteitem = markProduct(shopItem)                          # calling function to mark item complete as desired by the the user
            shopItem.remove(deleteitem)                                 # to delete item from required list
            listCompleted.append(deleteitem)                            # add completed item to completed list
        elif Choice == 'q' or Choice == 'Q':                            # asking customer choice to quit the program
            print("Thanks for shopping \nHave a nice day!! :)")         # printing fair well message
            break                                                       # beaking the loop
        else:                                                           # else statement to start loop again if choice is invalid
            print("Invalid menu choice. Please try again.")             # printing the error
    addcsvList(listCompleted)                                           # calling function to add items to the csv list

main()                                                                  # calls the main function


# sorry for this late submission, but my program was not working and i was extemely uncomfortable submitting incomplete program.
# i knew my marks will be deducted but i could not submit an incomplete file.

