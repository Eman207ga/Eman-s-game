file=open("Game.Assignment.txt","a")
file.write ("**************** Game Starting ****************\n")
print ("\nWelcome to the Adventure of Items in IBTE. There is a challenge that if you win, "
       "\nyou will be accepted into the university. The place has 10 rooms. "
       "\nIn some of these rooms there are 4 items that you must "
       "\ncollect and put in the bag and you will win the challenge! "
       "\nBut you must be careful because there are some puzzles you will encounter!")
player_name = input ("Enter your name: ")# Player name is entered to start the game.
print (f"Hello {player_name}, on your first day at university")
# Describe the game.
print ("Be careful, as there are puzzles to solve! Good Luck!")

locations = {"class 1" : "subject book",
             "class 2" : None,
             "class 3" : "student ID card",
             "auditorium" : None,
             "lab" : None,
             "finance office" : "financial document",
             "admission office" : "mouse",
             "students affairs office" : None,
             "meeting room" : None,
             "reception" : "class schedule"
             }  # Map of the campus. The player must follow it.
# Contains campus locations and items that can be found or will be used in
# these locations in each location.

print ("\n================================")
print (locations)
print ("================================")
print ("This is the map you must follow it to win the game.")
print ("\n*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")
print ("You are now at the starting point. In meeting room.")

firstLocation = "meeting room"    # Is the first place the player starts.
player_bag = []                   # The bag in which the player will collect items.
items = ["subject book", "student ID card", "financial office", "mouse", "class schedule"]

def collect_items (item):
    if (len(player_bag) < 4):          # If the items in the bag are less than 4,
        # the player is allowed to add items to the bag
        if (item not in player_bag):   # Because the item is not repeated in the bag.
            player_bag.append (item)   # Add items to the bag.
            print("Good job! You have collected: {}".format(item))
        else:
            print (f"You already have {item} in your bag.")
    else:
        print ("")

def remove_item(item_to_remove):
    if (len(player_bag)==4):
        print ("\nYour bag is full. To add a new item, you need to remove one.")
        choice = input ("\nEnter 'add' to replace an item in your bag."
                        "\nEnter 'skip' to skip the item: ").strip().lower()
        if (choice == "add"):
            print("\nCurrent items in your bag:", player_bag)
            new_item = input("\nEnter the name of the item you want to add: ").strip().lower()
            if (new_item in items):
                if (new_item not in player_bag):
                    item_to_remove = input("which item you want to remove?: ").strip().lower()
                    if (item_to_remove in items):
                        if (item_to_remove in player_bag):
                            player_bag.remove(item_to_remove)  # Remove item
                            print(f"{item_to_remove} has been removed from your bag.")
                            player_bag.append(new_item)  # add new item
                            print(f"{new_item} has been added to your bag.")
                        else:
                           print(f"{item_to_remove} is not in your bag.")
                    else:
                        print ("Error")
                else:
                    print ("The item is already in your bag")
            else:
                print ("Error")
        elif (choice == "skip"):
            print("Ok, good luck!")
        else:
            print("Invalid choice.")
    else:
        print ("")


def check_bag ():
        if player_bag:# If there are items inside the bag
            # that are allowed to be shown to the player.
            choice = input ("Do you want to see your bag? (yes/no)?? ").strip().lower()
            if (choice == "yes"):
                print (player_bag)
            elif (choice == "no"):
                print ("")
            else:
                print ("Error")
        else:
            print ("Empty bag") # The bag is empty


def move_to_location (newlocation):
    global firstLocation     # To change the value of 'firstLocation' inside the function.
    # Use global variable
    if (newlocation not in locations):
        print("\nsorry, this location is not available ")
    elif (newlocation == firstLocation):  # Checks if the player is already at the new location.
        print ("\nYou are already there!")
    else:
        print(f"\nYou have moved from the {firstLocation} to the {newlocation}")
        firstLocation = newlocation    # Because 'firstLocation' takes
        # the stored 'newlocation' value.



class OtherCh:
    #   A class representing side characters who provide hints to the player.
    def __init__(self, name, hint):
        self.name = name
        self.hint = hint

    def sentence (self):
        return (f"Hi, I'm {self.name}. I'm here to give you a hint "
                f"\nto help you finding one of your itmes. the hint is: {self.hint}.")

Side_character1 = OtherCh ("Academic Mentor", f"Start by checking Class 1. "
                                              f"\n{player_name} Welcome back to the meeting room.")
Side_character2 = OtherCh ("Omar", "Be polite to the receptionist, "
                             "\nand they will give you the class schedule")
Side_character3 = OtherCh ("Huda", "Look in the cabinet for a financial document")
Side_character4 = OtherCh ("Yazan", "Check the table for your student ID card")
# name and hint will be replaced with the values stored in each variable.


while True:
    print("\n<*>,<*>,<*>,<*>,<*>,<*>,<*>,<*>,<*>,<*>,<*>,<*>,<*>,<*>,<*>,<*>,")
    print(locations)
    print("<*>,<*>,<*>,<*>,<*>,<*>,<*>,<*>,<*>,<*>,<*>,<*>,<*>,<*>,<*>,<*>,")
    newlocation = input("\nChoose the location where you want to go?: ").strip().lower()
    move_to_location(newlocation)    # Call the function to move between places.
    # 'newlocation' is the place where the player want to go.

    if (newlocation  == "class 1"):
        print ("\nThere is a subject book, you should take it to continue your campus tour")
        print("Check if the book inside the drawer.")
        choice = input ("Do you want to take it? (yes/no)??? ").strip().lower()
        if (choice == "yes"):
            print("\n#*#*#*#*#*#*#*#*#*#*#*#*")
            remove_item("subject book")    # Call the function to replace the item to the bag.
            collect_items("subject book")  # Call the function to add the item to the bag.
            check_bag()     # Call the function to check if the bag is having 5 itmes.
            print("#*#*#*#*#*#*#*#*#*#*#*#*")
        elif (choice == "no"):
            print ("\nOk. Good luck finding the items.")
        else:
            print ("Error")

    elif (newlocation == "class 2"):
        print ("\nThis door is closed. The door must be opened through the subject book.")
        if ("subject book" in player_bag):    # If the player have subject book
            # he will open the door.
            print("The door code is 1234. The door is now unlocked!")
            print("\nYou have successfully entered Class 2!")
        else:
            print ("\nYou don't have the book! Look for it in the class 1 "
                   "to find the secret code.")

    elif (newlocation == "class 3"):
        print(Side_character4.sentence())    # Call the function to show the side character.
        print("^/*^/*^/*^/*^/*^/*^/*^/*^/*^/*")
        print("You found your student ID card!")
        choice = input("Do you want to take it? (yes/no)??? ").strip().lower()   # player choice.
        if (choice == "yes"):
            print("\n#*#*#*#*#*#*#*#*#*#*#*#*")
            remove_item("student ID card")      # Call the function to replace the item to the bag.
            collect_items("student ID card")    # Call the function to add the item to the bag.
            check_bag()     # Call the function to check if the bag is having 5 itmes.
            print("#*#*#*#*#*#*#*#*#*#*#*#*")
        elif (choice == "no"):
            print("\nOk. Good luck finding the items.")
        else:
            print ("Error")


    elif newlocation == "auditorium":
        print ("There is a a class schedule on the board, but it's missing some details!")
        print("To complete the schedule, You must have the class schedule")
        if ("class schedule" in player_bag):
            question = input("What subject is scheduled on Monday? "
                             "(Options: Science, Mathematics): ").strip().lower()
            if question == "science":
                print("Correct!")
            else:
                print("Wrong answer. Try again.")
        else:
            print ("You do not have the class schedule. Go to find it")

    elif (newlocation == "lab"):
        print ("\nThere is a computer that needs a mouse to operate. ")
        if ("mouse" in player_bag):    # if the player have mouse he will operate the device.
            print("\nYou have successfully operate the device!")   # If he has a mouse,
            # the device is turned on.
        else:    # If he does not have a mouse, he is instructed to look for it.
            print ("\nYou don't have the mouse! Find a mouse to operate the device.")

    elif (newlocation == "finance office"):
        print(Side_character3.sentence())    # Call the function to show the side character.
        print("^/*^/*^/*^/*^/*^/*^/*^/*^/*^/*")
        print("\nYou found a financial document.")
        choice = input("Do you want to take it? (yes/no)??? ").strip().lower()
        if (choice == "yes"):
            print("\n#*#*#*#*#*#*#*#*#*#*#*#*")
            remove_item("financial document")     # Call the function to replace the item to the bag.
            collect_items("financial document")   # Call the function to add the item to the bag.
            check_bag()     # Call the function to check if the bag is having 5 itmes.
            print("#*#*#*#*#*#*#*#*#*#*#*#*")
        elif (choice == "no"):
            print("\nOk. Good luck finding the items.")
        else:
            print ("Error")


    elif (newlocation == "admission office"):
        print("\nWelcome to the admission office. there is a mouse, it might be useful.")
        choice = input("Do you want to take it? (yes/no)??? ").strip().lower()
        if (choice == "yes"):
            print("\n#*#*#*#*#*#*#*#*#*#*#*#*")
            remove_item("mouse")      # Call the function to replace the item to the bag.
            collect_items("mouse")    # Call the function to add the item to the bag.
            check_bag()     # Call the function to check if the bag is having 5 itmes.
            print("#*#*#*#*#*#*#*#*#*#*#*#*")
        elif (choice == "no"):
            print("\nOk. Good luck finding the items.")
        else:
            print ("Error")

    elif (newlocation == "students affairs office"):
        print ("\nThe employee asks you to show your ID card to complete your registration.")
        if ("student ID card" in player_bag):    # if the player have student ID card
            # he will complete his registration.
            print("\nYou have successfully complete your registration!")
        else:
            print ("\nFind your ID card to complete registration")

    elif (newlocation == "reception"):
        print(Side_character2.sentence())    # Call the function to show the side character.
        print("^/*^/*^/*^/*^/*^/*^/*^/*^/*^/*")
        print (f"{player_name}, you've found a class schedule. Well done!")
        choice = input("Do you want to take it? (yes/no)??? ").strip().lower()
        if (choice == "yes"):
            print("\n#*#*#*#*#*#*#*#*#*#*#*#*")
            remove_item("class schedule")     # Call the function to replace the item to the bag.
            collect_items("class schedule")   # Call the function to add the item to the bag.
            check_bag()     # Call the function to check if the bag is having 5 itmes.
            print("#*#*#*#*#*#*#*#*#*#*#*#*")
        elif (choice == "no"):
            print("\nOk. Good luck finding the items.")
        else:
            print ("Error")

    elif (newlocation == "meeting room"):
        print(Side_character1.sentence())    # Call the function to show the side character.
        if len(player_bag) == 4:
            if ("financial document" in player_bag):
                print("\n******/******/******/******/******/******/******/******/")
                print("Congratulations {}! You collected all items and won the game!"
                      .format(player_name))
                print("******/******/******/******/******/******/******/******/")
                break  # if the player collect 5 items in his bag he will win the game!
            else:
                print ("You must have the financial document to complete the payment")
        else:
            print ("\nYou still need to collect all 4 items. Keep exploring and good luck!."
                   "When you finish collecting the 4 items come back")
        print("^/*^/*^/*^/*^/*^/*^/*^/*^/*^/*")

file.close()
