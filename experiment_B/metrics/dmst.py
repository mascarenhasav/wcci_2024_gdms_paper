'''
Title: Code to evaluate the Pairwise Distances metric (Dpw)*

* A.L. Barker and W.N. Martin. Dynamics of a distance-based population diversity measure. In
Proceedings of the 2000 Congress on Evolutionary Computation. CEC00 (Cat. No.00TH8512),
volume 2, pages 1002–1009 vol.2, 2000

Author: Alexandre Mascarenhas
Contact: https://mascarenhasav.github.io

Date: 2023/2
'''
import numpy as np
import pandas as pd
import networkx as nx
from scipy.spatial.distance import pdist, squareform
from scipy.spatial.distance import cdist
import numpy as np
import matplotlib.pyplot as plt

# calculate the metric
def metric(var_metric, NMDF, population, gen):
    popsize = len(population)
    aux = 0

    #data = np.unique(population, axis = 0)
    distances = squareform(pdist(population))
    G = nx.from_numpy_array(distances)
    mst = nx.minimum_spanning_tree(G)
    aux = sum(mst[e[0]][e[1]]['weight'] for e in mst.edges)
        
    # Normalization
    if(gen == 1 or aux > NMDF[-1]):
        NMDF.append(aux)
    else:
        NMDF.append(NMDF[-1])
    var_metric.append(aux / NMDF[-1])   
    
    return var_metric, NMDF