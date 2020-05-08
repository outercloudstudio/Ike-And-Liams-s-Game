import src

def room1():
    room = input("You wake up in a dark room. It is filled with the sound of screaming.")

def preparation():    
    prep = input("Here are the game rules: At any time, press 'q' to quit the game, or 'h' to read this again. Write 'continue' to keep going.")
    if prep == "q":
        print("Goodbye")
    elif prep == "h":
        preparation()
    else:
        room1()

preparation()