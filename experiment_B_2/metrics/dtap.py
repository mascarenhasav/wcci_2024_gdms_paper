'''
Title: Code to evaluate the Distance to Average Point metric (Ddtap)*

* Hussein A Abbass and Kalyanmoy Deb. Searching under multi-evolutionary pressures. In
International conference on evolutionary multi-criterion optimization, pages 391-404. Springer,
2003.

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
    aux = 0
    
    # Append the value of the dimensions in a list
    for ind in population:
        for d_i, d in enumerate(ind):
            pd1[d_i].append(d)
            
    # Avarage the the values of the dimension
    avr_pd1 = [np.average(pd1[d_i]) for d_i in range(ndim)]
    
    for ind in population:
        for d_i, d in enumerate(ind):
            aux += (d - avr_pd1[d_i])**2
    
    aux = np.sqrt(aux) / popsize
        
    # Normalization
    if(gen == 1 or aux > NMDF[-1]):
        NMDF.append(aux)
    else:
        NMDF.append(NMDF[-1])
    var_metric.append(aux / NMDF[-1])
    
    return var_metric, NMDF