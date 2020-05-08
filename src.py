import numpy
from random import seed
from random import random
import noise
import math
#             0   1   2   3   4   5   6   7   8   9  10
ASCCI = numpy.array([" ",".","-","~","o","O","G","%","&","@","|"])

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

def TestNoise(size = 5):
    x=0
    y=0
    while y<size :
        temp = ""
        while x<size:
            temp.join(temp + ASCCI[math.floor(noise.pnoise2(x,y))])
            #print(ASCCI[math.floor(noise.pnoise2(x,y))])
            print(math.floor(noise.pnoise2(x/size,y/size)))
            x=x+1
        #print(temp)
        y=y+1
        
#TestNoise(5)
