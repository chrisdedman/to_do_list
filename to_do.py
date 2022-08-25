from os import system


def start():
    """
    Create a file when launching the app for the first time
    if the file alread exist, append the new data to the end
    of the file.
    """
    with open("to_do_list.txt", 'a') as output:
        output.write('')
        output.close()
        to_do_list_menu()

def clear_screen():
    system("cls||clear")
    print("""
    \t\t*********************************************
    \t\t** Welcome to your To-Do List application! **
    \t\t*********************************************
    """)

def show_to_do_list():
    """Print the to-do list"""
    
    print("\nThis is your To-Do List:\n")
    with open("to_do_list.txt", 'r') as read_file:
        toDoList = read_file.readlines()
        if len(toDoList) == 0:
            print("\t- Your To-Do list is empty!")
        else:
            for index, value in enumerate(toDoList, start=1):
                print(f"\t {index}. {value}")

def add_item():
    """Add element to the to-do list"""
    
    print("Which task would you like to add [done to end]?")
    while True:
        add_to_list = input("\t> ").capitalize()
        if len(add_to_list) == 0:
            print("No task?")

        elif add_to_list == "Done":
            break

        else:
            with open("to_do_list.txt", 'a') as toDo:
                toDo.write(f"{add_to_list}\n")
   
def remove_item():
    """Remove item from the to-do list"""
    
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

def clear_to_do_list():
    """Clear the whole to-do list"""
    
    # --- Add the choice to cancel this action --- #
    cancel_clear_action = input("Are you sure you want to clear your to-do list? [Y]es/[N]o ").lower()
    if 'n' in cancel_clear_action:
        pass

    else:
        erase_content = open('to_do_list.txt', 'w')
        erase_content.truncate(0)

def to_do_list_menu():
    """
    Create function to Quit, Add, Delete, Show or Clear the to-do list,
    and the option to refresh the screen
    """
    user_option = input("\n\t[R]efresh Screen / [S]how / [A]dd / [D]elete / [C]lear / [Q]uit\n> ").upper()
    
    if user_option == "R":
        clear_screen()

    elif user_option == 'S':
        show_to_do_list()

    elif user_option == "A":
        add_item()

    elif user_option == 'D':
        remove_item()
        
    elif user_option == 'C':
        clear_to_do_list()

    elif user_option == 'Q':
        print("Thanks for using our program.\nGoodbye!")
        exit(0)

    else:
        print(f"Sorry, '{user_option}' is not an user_option available.")

                           
if __name__ == "__main__":
    clear_screen()
    while True:
        start()
