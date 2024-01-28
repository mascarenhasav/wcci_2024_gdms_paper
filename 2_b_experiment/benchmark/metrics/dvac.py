'''
Title: Code to evaluate the Variance Average Chromosomes metric (Dvac)*

* Francisco Herrera, E Herrera-Viedma, Manuel Lozano, and Jose Luis Verdegay. Fuzzy tools to
improve genetic algorithms. In Second European Congress on Intelligent Techniques and Soft
Computing, volume 3, pages 1532–1539, 1994

Author: Alexandre Mascarenhas
Contact: https://mascarenhasav.github.io

Date: 2023/2
'''
import numpy as np

params = [] # configuration parameters of the metric
vars = ["dvac", "NMDF"] # variables used in to calculate the metric
log = ["dvac"] # variable to be recorded on the log file
scope = ["GEN"] # scope of the metric, GEN

NMDF = 1

# calculate the metric
def metric(var_metric, NMDF, population, gen):
    popsize = len(population)
    ndim = len(population[0])
    pd1 = []
    pop = []
    aux = 0
    
    # Append the value of the dimensions in a list
    for ind in population:
        for d in ind:
            pd1.append(d)
                
    # Average the values of all dimensions
    avr_pd1 = np.average(pd1)
    pd1 = []
    
    # For each individual, sum the difference between the average of its dimensions values
    # and the average of all dimensions. Normalize with the population size
    for ind in population:
        for d in ind:
            pd1.append(d)
        aux += (np.average(pd1) - avr_pd1)**2
            
    aux = aux / popsize
        
    # Normalization
    if(gen == 1 or aux > NMDF[-1]):
        NMDF.append(aux)
    else:
        NMDF.append(NMDF[-1])
    var_metric.append(aux / NMDF[-1])   
    
    return var_metric, NMDF