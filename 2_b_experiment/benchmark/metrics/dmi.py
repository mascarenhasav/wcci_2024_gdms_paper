'''
Title: Code to evaluate the Moment of Inertia metric (Dmi)*

* De Jong K.A. Morrison, R.W. Measurement of population diversity. In Artificial Evolution.
EA 2001. Lecture Notes in Computer Science, vol 2310. Springer, Berlin, Heidelberg, volume
2310, pages 1128–1134, 2002.

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
    
    # For each dimension value, calculate the difference of the avarage and sum
    for ind in population:
        for d_i, d in enumerate(ind):
            aux += (d - avr_pd1[d_i])**2
            
    # Normalization
    if(gen == 1 or aux > NMDF[-1]):
        NMDF.append(aux)
    else:
        NMDF.append(NMDF[-1])
    var_metric.append(aux / NMDF[-1])   
    
    return var_metric, NMDF