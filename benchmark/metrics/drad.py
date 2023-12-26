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

    data = np.copy(population)
    dist_matrix = cdist(data, data)
    selected_flag = np.zeros(len(data))
    original_indices = np.arange(len(data))
    sigma = np.max(dist_matrix)
    max_indices = np.array(np.where(dist_matrix == sigma))[:, 0]
    x0 = data[max_indices[0]]
    x1 = data[max_indices[1]]
    selected_flag[max_indices] = 1
    selected_indices = []
    selected_indices.append(max_indices[0])
    selected_indices.append(max_indices[1])
    sigma_list = []
    sigma_list.append(0)
    sigma_list.append(sigma)
    while len(selected_indices) < len(population):
        shortest_distances_list = np.min(dist_matrix[np.ix_(selected_flag == 0, selected_flag == 1)], axis = 1)
        max_index = np.argmax(shortest_distances_list)
        max_original_index = original_indices[selected_flag == 0][max_index]
        selected_flag[max_original_index] = 1
        selected_indices.append(max_original_index)
        sigma = shortest_distances_list[max_index]
        sigma_list.append(sigma)
    aux = np.sum(sigma_list)#(selected_indices, sigma_list)
    
    # Normalization
    if(gen == 1 or aux > NMDF[-1]):
        NMDF.append(aux)
    else:
        NMDF.append(NMDF[-1])
    var_metric.append(aux / NMDF[-1])   
    
    return var_metric, NMDF