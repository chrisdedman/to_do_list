# Import the packtage for refreshing the screen if needed
import os
import readline


# Create a file when launching the app for the first time
# if the file alread exist, append the new data to the end
# of the file.
def start():
    
    with open("to_do_list.txt", 'a') as output:
        output.write('')
        output.close()
        to_do_list()


# Create function to Quit, Add, Delete, Show or Clear the to-do list,
# and the option to refresh the screen
def to_do_list():
    
    user_option = input("\n\t[R]efresh Screen / [S]how / [A]dd / [D]elete / [C]lear / [Q]uit\n>").upper()
    
    # Clean the screen if the user enter R
    if user_option == "R":
        os.system("cls||clear")
        print("""
\t\t*********************************************
\t\t** Welcome to your To-Do List application! **
\t\t*********************************************
""")


# If the user enter S, the to-do list items will be print to the screen
    elif user_option == 'S':
        print("\nThis is your To-Do List:\n")

        with open("to_do_list.txt", 'r') as read_file:
            toDoList = read_file.readlines()
            if len(toDoList) == 0:
                print("\t- Your To-Do list is empty!")
            else:
                for index, value in enumerate(toDoList, start=1):
                    print(f"\t {index}. {value}")


# If the user enter A, he will have the choice to add some items to the list,
# and keep it save on the computer
    elif user_option == "A":
        
        add_to_list = input("Which task would you like to add?\n\t>").capitalize()
        if len(add_to_list) == 0:
            print("No task?")
        else:
            with open("to_do_list.txt", 'a') as toDo:
                toDo.write(f"{add_to_list[::]}\n")
            

# If the user enter D, he will have the choice to remove an item
    elif user_option == 'D':
        
        delete_request = int(input('Which task would you like to delete? [index #]\n\t>'))
        # open the text file with the to-do list
        try:
            with open("to_do_list.txt", 'r') as read_file:
                # read each lines from the text file
                toDoList = read_file.readlines()
                # close the text file
                read_file.close()
                # deleted the lines request by the user from the text file
                del toDoList[delete_request-1]

        # Create an exception if the user enter a index out of range
        except IndexError:
            print("Sorry, this element do not exist!")
            
        # re-open the text file with the to-do list 
        toDoList_update = open("to_do_list.txt", "w+")

        # update the text file with the new to-do list without the line deleted
        for line in toDoList:
            toDoList_update.write(line)
        toDoList_update.close()
    

# If the user enter C, he will have the choice to clear the to-do list 
    elif user_option == 'C':

        # --- Add the choice to cancel this action --- #
        cancel_clear_action = input("Are you sure you want to clear your to-do list? [Y]es/[N]o").lower()
        if 'n' in cancel_clear_action:
            pass

        else:
            erase_content = open('to_do_list.txt', 'w')
            erase_content.truncate(0)
        

# If the user enter Q, the program will be close
    elif user_option == 'Q':
        
        print("Thanks for using our program.\nGoodbye!")
        exit(0)


# If the user doesn't choose a user_option available, 
# the app will tell what is the user_option unavailable
    else:
        print(f"Sorry, '{user_option}' is not an user_option available.")
    
    
# Start the program with a welcome message, and start a while loop                               
if __name__ == "__main__":
    os.system("cls||clear")
    print("""
\t\t*********************************************
\t\t** Welcome to your To-Do List application! **
\t\t*********************************************
""")
    while 1:
        start()