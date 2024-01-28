'''
Title: Code to evaluate the True diversity metric (Dtd)*

* Mark Wineberg and Franz Oppacher. The underlying similarity of diversity measures used in
evolutionary computation. In Erick Cantú-Paz and Julian Miller, editors, Genetic and Evo-
lutionary Computation — GECCO 2003, pages 1493-1504, Berlin, Heidelberg, 2003. Springer
Berlin Heidelberg.

Author: Alexandre Mascarenhas
Contact: https://mascarenhasav.github.io

Date: 2023/2
'''
import numpy as np

# calculate the metric
def metric(var_metric, NMDF, population, gen):
    popsize = len(population)
    ndim = len(population[0])
    pd1 = [[] for i in range(ndim)]
    pd2 = [[] for i in range(ndim)]
    aux = 0    
    
    # Append the value of the dimension and its value squared in different lists
    for ind in population:
        for d_i, d in enumerate(ind):
            pd1[d_i].append(d)
            pd2[d_i].append(d**2)
            
    # Create a list of the avarage of the dimensions
    avr_pd1 = [np.average(pd1[d_i])**2 for d_i in range(ndim)]
    avr_pd2 = [np.average(pd2[d_i]) for d_i in range(ndim)]
    
    # Sum the difference
    for d_i in range(ndim):
        aux += avr_pd2[d_i] - avr_pd1[d_i]
    
    # Square root the sum
    aux = np.sqrt(aux) / ndim
    
   # Normalization
    if(gen == 1 or aux > NMDF[-1]):
        NMDF.append(aux)
    else:
        NMDF.append(NMDF[-1])
    var_metric.append(aux / NMDF[-1])   
    
    return var_metric, NMDF