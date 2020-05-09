import numpy as np
from random import seed
from random import random
import math
planetNames = ["Croid","Hyrusk","Atlasks","Liompa","Geh","Retd","Kring"]
planetNames2= ["223","w220","sdhu","sdh2o","1e9dj","2d89","1hdk","dsfkh","sndi"]
planetNamesCreated = []
#seed to prevent any errors that might happen
#if seed is the same them random numbers will be the same
#maybe use something to pick a seed maybe based on time?
seed(0)
#to set the seed
def SetSeed(s):
    seed(s)
#get a random int within a range
def RandRange(min,max):
    return (math.floor(random()*(max-min)+min))

def GeneratePlanet() :
    name = ""
    name += planetNames[RandRange(0,len(planetNames)-1)]
    name+="_"
    name += planetNames2[RandRange(0,len(planetNames2)-1)]
    for i in planetNamesCreated:
        if name == i:
            name = "Planet_"
            name += str(RandRange(100000,999999))
    for t in planetNamesCreated:
        if name ==t:
            GeneratePlanet()
    planetNamesCreated.append(name)
    return name


    
