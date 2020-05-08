from src import *

def cockpit():
    print("You open the door and go out.")

def room1():
    print("You wake up to the sound of screaming in a dark room.")
    input()
    print("After careful consideration, you decide that it is not screaming, it is an engine.")
    input()
    door = input("You do not know how you got here, nor do you know where you are. But one thing that you do know is that there is a door in front of you. Do you open it and go out? (y or n)")
    if door == "n":
        print("You go back to sleep.")
        input()
        room1()
    if door == "y":
        cockpit()    

def preparation():    
    prep = input("Here are the game rules: At any time, press 'q' to quit the game, or 'h' to read this again. After I say a statement, click Enter. Write 'continue' to keep going.")
    if prep == "q":
        print("Goodbye")
    elif prep == "h":
        preparation()
    else:
        room1()

preparation()