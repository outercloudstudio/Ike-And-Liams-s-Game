import src


chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['1','2','3','4','5','6','7','8','9','0','1','2','3','4','5','6','7','8','9','0','1','2','3','4','5','6']


def ini (n):
    nam = n.lower()
    seedjoin = ""
    for i in nam:   
        seedjoin +=numbers[chars.index(i)]
    src.SetSeed(int(seedjoin))

print("What is your name?\t")
name = input()
ini(name)

PlanetDestination = src.GeneratePlanet()
PlanetDestRight = src.GeneratePlanet()
PlanetDestRightQualities = src.DescribePlanet()
PlanetDestLeft = src.GeneratePlanet()
PlanetDestLeftQualities = src.DescribePlanet()

def planetright():
    print(f"After you tell her that you would like to go to planet {PlanetDestRight}, she says, 'Are you sure? {PlanetDestRightQualities}'")
    planetDecision = input()


def planetleft():
    print(f"After you tell her that you would like to go to planet {PlanetDestLeft}, she says, 'Are you sure? {PlanetDestLeftQualities}'")
    planetDecision = input()

def goodbye(name):
    print(f"Goodbye, {name.title()}")

def cockpit(name):
    print("You open the door and go out. It seems that you have walked into a tangle of arms. legs, and voices.")
    input()
    print(f"You overhear someone one say we are going to the planet {PlanetDestination}")
    input()
    print(f"A woman runs up to you and salues. 'Captain {name.title()} There has been an error in our piloting system! We have flown into a meteor shower! It is impossible to go forward, so we will not be going to the planet {PlanetDestination}! Left is the planet {PlanetDestLeft}, and right is the planet {PlanetDestRight} It's your call, sir!' Will you go left, or right? (l or r)\t")
    crewmember = input()    
    if crewmember == "l":
        planetleft()
    if crewmember == "r":
        planetright()
    if crewmember == "q":
        goodbye()

def room1(name):
    print("You wake up to the sound of screaming in a dark room.")
    input()
    print("After careful consideration, you decide that it is not screaming, it is an engine.")
    input()
    print("You do not know how you got here, nor do you know where you are. But one thing that you do know is that there is a door in front of you. Do you open it and go out? (y or n)\t")
    door = input()
    if door.lower() == "q":
        goodbye(name)
    elif door.lower() == "n":
        print("You go back to sleep.")
        input()
        room1(name)
    elif door.lower() == "y":
        cockpit(name)
    else:
        print(f"Please write one of the given answers, {name.title()}.")
        input()
        room1(name)        

def preparation(name):
    print(f"Hello, {name.title()}. Here are the game rules: At any time, press 'q' to quit the game. After I say a statement without asking you to answer, click Enter. Write 'continue' to keep going.\t")    
    prep = input()
    if prep.lower() == "q":
        goodbye(name)
    elif prep.lower() == "continue":
        room1(name)
    else:
        print("Please write one of the given answers.")
        input()
        preparation(name)    

preparation(name)