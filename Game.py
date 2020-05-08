import src
def preparation():    
    prep = input("Here are the game rules: At any time, press 'q' to quit the game, or 'h' to read this again.")
    if prep == "q":
        print("Goodbye")
    if prep == "h":
        preparation()    

preparation()