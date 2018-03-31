import networkx as nx
from networkx import Graph
from matplotlib import use
use('qt4agg')
import matplotlib.pyplot as plt
import random as rn
import numpy as np
from math import log
from math import floor
import powerlaw as pl
from datetime import datetime

# FONCTION FITNESS
alpha = 2.4
gama = 1
mutation = 0.1
crossing_over = 0.2

def turn_to_power(liste, power): 
    return [number**power for number in liste]

def Timepassed(t0,t1):
    t0 = t0.split(".")[0].split(":")
    t1 = t1.split(".")[0].split(":")
    T0 = 0
    T1 = 0
    for i in range (3):
        T0 += int(t0[i])*60**(2-i)
        T1 += int(t1[i])*60**(2-i)
    difsec = T1-T0
    heure = 0
    minute = 0
    seconde = difsec%60
    minute = int(difsec/60)
    heure = int(minute/60)
    minute = minute%60
    return(str(heure)+":"+str(minute)+":"+str(seconde))
