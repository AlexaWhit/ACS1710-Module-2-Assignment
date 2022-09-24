#-----------------------CREATE CHECKLIST-------------------------#
print()
checklist = list ()

#-----------------------DEFINE FUNCTIONS-------------------------#
# CREATE - add the item and add it to the end of the checklist
def create(item):
    checklist.append(item)


# READ - return the value of the specific index (ex. [0] = Blue Tie)
def read(index):
    return checklist[index]


# UPDATE - updating/writing over/reassigning the data at a specific index
def update(index, item):
    checklist[index] = item


# DESTROY - remove the input at the specific index
def destroy(index):
    checklist.pop(index)


# LIST ALL THE ITEMS - loop through the list and 
def list_all_items():
    index = 0
    for list_item in checklist:
        print(str(index) + list_item) #we need to change index from int to str
        index += 1

# MARK ITEM AS COMPLETED
#def mark_completed(index, item):
#    checklist[index] = item
#    print("√" + str(index) + item)

        
# SELECT
def select(function_code):
    if function_code == "A": #Create item in checklist
        input_item = user_input("Input item: ")
        create(input_item)
    elif function_code == "R": #Read item in checklist
        item_index = user_input("Index Number?")
        read(item_index)
    elif function_code == "L": #Display/Print all items
        list_all_items()
    elif function_code == "Q": #Quit here/stop our loop
        return False
    else: #Catch all - if user enters something else
        print("Unknown Option")
    return True
   


# USER INPUT
def user_input(prompt):
    #the input funtion will display a message to the user in the terminal and will wait for user to input response
    user_input = input(prompt)
    return user_input

# WHILE LOOPS
running = True
while running:
    selection = user_input(
        "Press A to add to list, R to Read from list and L to Display list")
    select(selection)

#TESTING
def test():
    create("Purple Sox")
    create("Red Cloak")

    print(read(0))
    print(read(1))

    update(0, "Purple Socks")

    destroy(1)

    print(read(0))

    list_all_items()

    user_input()

    user_value = user_input("Please enter a value: ")
    print(user_value)

#--------------------------TESTING AREA---------------------------#    

test()
