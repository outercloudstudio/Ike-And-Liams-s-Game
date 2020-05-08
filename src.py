import numpy as np
from random import seed
from random import random
import math
#             0   1   2   3   4   5   6   7   8   9  10
ASCCI = np.array([" ",".","-","~","o","O","G","%","&","@","|"])
WorldPlaces = np.array(["Forest","Dessert","Mountains","Ocean","Swamp","Plains"])
World = np.full((5,5),"")
#seed to prevent any errors that might happen
#if seed is the same them random numbers will be the same
#maybe use something to pick a seed maybe based on time?
seed(0)
#test function
def HOI ():
    print("Hoi")
#to set the seed
def SetSeed(s):
    seed(s)
#get a random int within a range
def RandRange(min,max):
    return (math.floor(random()*(max-min)+min))

def GenerateWorld (size):
    World =  np.full((size,size), "",dtype=str)
    for x in range (0,size-2) :
        for y in range (0,size-2) :
            World[(x,y)] = "a"
            #WorldPlaces[RandRange(0,WorldPlaces.size)]
            x+=1
        y+=1

GenerateWorld(5)

def PrintNPArray(array):
    for item in array:
        print(item)

    
