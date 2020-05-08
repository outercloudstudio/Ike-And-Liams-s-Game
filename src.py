import numpy
from random import seed
from random import random
import noise
import math
#             0   1   2   3   4   5   6   7   8   9  10
numpy.array([" ",".","-","~","o","O","G","%","&","@","|"])

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

def TestNois():
    pass

