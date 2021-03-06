"""
Repeating asking input
"""
def help_pb():
    print ("function for help")

def lookup_pb(dic_phonebook, name):
    if name in dic_phonebook:
        print ("the phonenumer of", name, "is:", dic_phonebook[name])
    else:
        print(">name is not in the phonebook")
def enter_pb(dic_phonebook, name, number):
    if name not in dic_phonebook:
        dic_phonebook[name] = number
    else:
        print(">name is already in the phonebook")
def remove_pb(dic_phonebook, name):
    dic_phonebook.pop(name)

def check_name(dic_phonebook, name):
    check = False
    if name in dic_phonebook:
        check = True
    return  check

def quit_pb():
    print("program terminated")

def user_prompt():
    print("Welcome, this is phonebook_v1")
    phonebook = {}
    print(phonebook)
    user_input = input("How can i help you?\n")
    while user_input != "quit":
        print("Request is processing")
        if user_input == "help":
            help_pb()
        elif user_input == "lookup":
                lookup_name = input("Please enter the name for lookup:\n")
                lookup_pb(phonebook, lookup_name)
        elif user_input == "enter":
            enter_name = input("Please enter the name for phonebook entree:\n")
            enter_number = input("Please enter the number for phonebook entree:\n")
            enter_pb(phonebook, enter_name, enter_number)
        elif user_input == "remove":
            remove_name = input("Please enter the name to remove from the phonebook:\n")
            remove_pb(phonebook, remove_name)
        else:
            print ("This is not an function for this program, please review help")
            help_pb()

        user_input = input("How can i help you?\n")

if __name__ == '__main__':
    user_prompt()