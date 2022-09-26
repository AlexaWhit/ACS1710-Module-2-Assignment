#********      CAPTAIN RAINBOW'S COLOR CHECKLIST         *******#


#-----------------------CREATE CHECKLIST-------------------------#
from ast import If

from symbol import if_stmt


print()
checklist = list ()

#-----------------------DEFINE FUNCTIONS-------------------------#
# CREATE - add the item and add it to the end of the checklist
def create(item):
    checklist.append(item)


# READ - return the value of the specific index (ex. [0] = Blue Tie)
def read(index):
    if index <= len(checklist):
        print(checklist[index])


# UPDATE - updating/writing over/reassigning the data at a specific index
def update(index, item):
    checklist[index] = item


# DESTROY - remove the input at the specific index
def destroy(index):
    checklist.pop(index)


# LIST ALL THE ITEMS - loop through the list and 
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
def list_all_colors():
    index = 0
    for color in colors:
        print(f"{index} + {color}") #we need to change index from int to str
        index += 1

        
clothing = ["shirt", "pants", "cape", "hat", "sockone", "socktwo", "bowtie"]
def list_all_clothing():
    index = 0
    for clothing_item in clothing:
        print(str(index) + list_item) #we need to change index from int to str
        index += 1


# MARK ITEM AS COMPLETED
def mark_completed(index):
    if index <= len(checklist):
    completed_item = "√" + checklist[index]
    update(index, completed_item)
    


# USER INPUT
def user_input(prompt):
    #the input funtion will display a message to the user in the terminal and will wait for user to input response
    user_input = input(prompt)
    return user_input  


# WHILE LOOPS
running = True
while running:
    selection = user_input(
        "Press A to add to list, R to Read from list, L to Display list, and Q to Quit: ")
    select(selection)


# SELECT
def select(function_code):
    #Create item in checklist
    if function_code == "A": 
        input_item = user_input("Enter which item you are adding to the list: ")
        create(input_item)
    #Read item in checklist
    elif function_code == "R": 
        item_index = user_input("Which item would you like to view? Please enter the item number: ")
        read(item_index)
    elif function_code == "L": #Display/Print all items
        list_all_items()
    elif function_code == "Q": #Quit here/stop our loop
        return False
    else: #Catch all - if user enters something else
        print("Unknown Option")
    return True
   

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



 


#--------------------------TESTING AREA---------------------------#    

test()
