from src import *

def goodbye(name):
    print(f"Goodbye, {name}")

def cockpit(name):
    print("You open the door and go out. It seems that you have walked into a tangle of arms. legs, and voices.")
    input()


def room1(name):
    print("You wake up to the sound of screaming in a dark room.")
    input()
    print("After careful consideration, you decide that it is not screaming, it is an engine.")
    input()
    door = input("You do not know how you got here, nor do you know where you are. But one thing that you do know is that there is a door in front of you. Do you open it and go out? (y or n)")
    if door.lower() == "h":
        preparation(name)
    elif door.lower == "q":
        goodbye(name)
    elif door.lower == "n":
        print("You go back to sleep.")
        input()
        room1(name)
    elif door.lower == "y":
        cockpit(name)
    else:
        print(f"Please write one of the given answers, {name}.")
        input()
        room1(name)        

def preparation(name):    
    prep = input(f"Hello, {name.title()}. Here are the game rules: At any time, press 'q' to quit the game, or 'h' to read this again. After I say a statement without asking you to answer, click Enter. Write 'continue' to keep going.")
    if prep.lower() == "q":
        goodbye(name)
    elif prep.lower() == "h":
        preparation(name)
    elif prep.lower() == "continue"
        room1(name)
    else:
        print("Please write one of the given answers.")
        input()
        preparation(name)    

name = input("What is your name?")
preparation(name)