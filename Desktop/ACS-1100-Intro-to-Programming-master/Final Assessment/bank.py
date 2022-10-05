#FUNCTION: Load Data - Reads text file, loads user data, returns list
def load_data(filename):
    '''
    A function to load the data from data.txt

    Returns:
    List of the user profiles
    '''
    user_list = []
    infile = open(filename, "r")
    infile.readlines()
    for line in infile:
        info = line.split(',')
        user_list.append(info)
    infile.close()
    return user_list




def does_user_exist(user_list, username, password):
    '''
    A function to check if the user input (username and password) are in the userList

    Parameters:
    user_list (list): The list of users and their data
    username (string): The username that the user entered when prompted
    password (string): The password that the user entered when prompted

    Returns:
    bool: True if the username and password are BOTH in the secret_word, False otherwise
    '''
    for i in range(len(user_list)):
        user = user_list[i]
        if user[0] == username and user[1] == password:
            return True
        else:
            return False



# def get_user_info(user_list, username, password):
#     '''
#     A function to obtain the user of the matching username and password from userList

#     Parameters:
#     user_list (list): The list of users and their data
#     username (string): The username that the user entered when prompted
#     password (string): The password that the user entered when prompted

#     Returns:
#     string: The user in the list who matches the username and password
#     '''
#     for user in user_list:
#         if user[0] == username and user[1] == password:
#             return user
#     print(user)



def display_user_info(user_list, username, password):
    '''
    A function to display indexes 2 and 3 of the user_list

    Parameters:
    user_list (list): The list of users and their data
    username (string): The username that the user entered when prompted
    password (string): The password that the user entered when prompted

    Returns:
    Indexes 2 [name] and 3 [balance] of the user_list  
    '''
    for i in range(len(user_list)):
        user = user_list[i]
        if user[0] == username and user[1] == password:
            print('Name:', user[2])
            print('Balance:', user[3])



def clear_terminal():
    '''
    A function to clear the terminal for better readability

    Returns:
    a clear terminal
    '''
    print("\033[H\033[J")



def login():
    '''
    A function that runs the program. Will start login in the command line.
    
    Parameters:
    Takes in user input (username + password) 

    Returns:
    If valid, will return the user's full name and balance.
    If invalid, will return "Username and password not found". 

    '''
    filename = "data.txt"
    user_list = load_data(filename)
    clear_terminal()
    print("Welcome to Your Online Bank")
    #Prompt user for username and password
    username = input("Enter username: ")
    password = input("Enter password: ")

    #Check if username is valid
    if does_user_exist(user_list, username, password) is True:
        #get_user_info(user_list, username, password)
        display_user_info(user_list, username, password)
    else:
        print('Username and password not found.')
  
login()