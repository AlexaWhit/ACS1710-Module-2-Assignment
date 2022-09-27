#**********************      CAPTAIN RAINBOW'S COLOR CHECKLIST         *********************#


#-----------------------CREATE EMPTY CHECKLIST-------------------------#
checklist = list()

#-----------------------DEFINE FUNCTIONS-------------------------#
# CREATE(A) - add the item and add it to the end of the checklist
def create(item):
    checklist.append(item)


# READ(R) - return the value of the specific index (ex. [0] = Blue Tie)
def read(index):
   return checklist[index]


# LIST ALL THE ITEMS(D) - loop through the list and 
def list_all_items():
    index = 0
    for list_item in checklist:
        print("{}: {}".format(index,list_item)) #we need to change index from int to str
        index += 1


# UPDATE(U) - updating/writing over/reassigning the data at a specific index
def update(index, item):
    checklist[index] = item


# MARK ITEM AS COMPLETED(M)
def mark_completed(index):
    completed_item = "√" + checklist[index]
    update(index, completed_item)
    list_all_items()

# DELETE/DESTROY(X) - remove the input at the specific index
def destroy(index):
    checklist.pop(index)
    print("The item has been deleted.")
    


# USER INPUT
def user_input(prompt):
    #the input funtion will display a message to the user in the terminal and will wait for user to input response
    user_input = input(prompt).lower() #.lower will allow for lower-case too!
    return user_input  





#-----------------------USER SELECTIONS-------------------------#
def select(function_code):
    #Create item in checklist
    if function_code == "a": 
        input_item = user_input("Enter which item you would like to ADD to the list: ")
        create(input_item)
    #Read item in checklist
    elif function_code == "r": 
        item_index = user_input("Which item would you like to view? Please enter the item number: ")
        print(read(int(item_index)))
    #Display/Print all items
    elif function_code == "d": 
        list_all_items()
    #Update an item
    elif function_code == "u": 
        item_index = int(user_input("Please enter the index number of the item you would like to UPDATE: "))
        updated_item = user_input("Please enter your updated item: ")
        update(item_index, updated_item)
    #Mark item as completed
    elif function_code == "m": 
        item_index = int(user_input("Please enter the index number of the item you would like to MARK AS COMPLETED: "))
        mark_completed(item_index)
    #Delete item in checklist
    elif function_code == "x": 
        item_index = int(user_input("Please enter the index number of the item you would like to DELETE: "))
        destroy(item_index)
    #Quit here/stop our loop
    elif function_code == "q": 
        clearTerminal()
        return False
    #Catch all - if user enters something else
    else: 
        print("Unknown Option - Please Try Again")
    return True
    



#Stretch Goal - clear terminal
def clearTerminal():
    print("\033[H\033[J")


#-----------------------WHILE LOOP-------------------------#
#to run the checklist
running = True
while running:
    selection = user_input(
        "Welcome to Captain Rainbow's Colorful Checklist!\nPress A to Add to list\nPress R to Read from list\nPress D to Display list\nPress U to Update an item in the list\nPress M to Mark an item as complete\nPress X to Delete an item\nPress Q to Quit\nPlease enter your selection here: ")
    running = select(selection)

#TESTING
#def test():
#    create("Purple Sox")
#    create("Red Cloak")

#    print(read(0))
#    print(read(1))

#    update(0, "Purple Socks")

#    destroy(1)

#    print(read(0))

#    list_all_items()

#    user_input()

#    user_value = user_input("Please enter a value: ")
#    print(user_value)



#test()


 


