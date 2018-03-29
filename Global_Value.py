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

# FONCTION FITNESS
alpha = 2.4
gama = 1
mutation = 0.01
crossing_over = 0.1

def turn_to_power(liste, power): 
    return [number**power for number in liste]
