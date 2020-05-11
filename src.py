import numpy as np
from random import seed
from random import random
import math
planetNames = ["Croid","Hyrusk","Atlasks","Liompa","Geh","Retd","Kring"]
planetNames2= ["223","w220","sdhu","sdh2o","1e9dj","2d89","1hdk","dsfkh","sndi"]
planetNamesCreated = []
RaceName1 = ["R","T","Ch","W","C","Z","L"]
RaceName2=["a","o","i","e","o"]
RaceName3 =["ch","ts","ls","ps","sh","x","d","kr"]
RaceName4 = ["","ex","s","y"]
RacesCreated = []
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

def GenerateRaceName():
    name = ""
    name +=RaceName1[RandRange(0,len(RaceName1)-1)]
    name +=RaceName2[RandRange(0,len(RaceName2)-1)]
    name +=RaceName3[RandRange(0,len(RaceName3)-1)]
    name +=RaceName4[RandRange(0,len(RaceName4)-1)]
    for i in RacesCreated:
        if name == i:
            name = "Race "
            name += str(RandRange(100000,999999))
    for t in RacesCreated:
        if name ==t:
            GenerateRaceName()
    RacesCreated.append(name)
    return name

def GeneratePlanetQualities():
    Quality1 = ["rocky","hilly","flat"]
    Quality2 =["hot", "temperate","cold","warm","freezing"]
    Quality3 = ["jungle","dessert","ocean","mountain","forest","snow"]
    return [Quality1[RandRange(0,len(Quality1)-1)],Quality2[RandRange(0,len(Quality2)-1)],Quality3[RandRange(0,len(Quality3)-1)]]

def DescribePlanet():
    q = GeneratePlanetQualities()
    n = GeneratePlanet()
    d = "The "+ q[2] +" planet, " + n + ", is " + q[1] + " and " + q[0]+ "."
    return d

