#!/usr/bin/env python3

import json
import os
import shutil

NPEAKS = [1, 5, 10, 15, 20, 25, 30, 35, 50, 45, 50]
NOUT = [0]
NDIM = [2, 5, 10, 15, 20, 25, 35, 40, 45, 50]
#NPEAKS = [5]
#NOUT = [0]
#NDIM = [2, 5, 10, 25]
METRICS = ["dmid", "dpw", "dtd", "dmi", "dmst", "drad"]
parameters = {}
parameters["NRUNS"] = 3
parameters["NGEN"] = 100
parameters["NP"] = 100
parameters["GOUT"] = [25, 50, 75]
parameters["LD"] = [0, 100]
parameters["SEED"] =42
parameters["PLOT"] = 0

for peak in NPEAKS:
    for out in NOUT:
        for dim in NDIM:
            parameters["METRICS_TO_TEST"] = METRICS
            parameters["NPEAKS"] = peak
            parameters["NOUT"] = out
            parameters["NDIM"] = dim
            path = f"{peak}-{dim}"
            if(os.path.isdir(path) == False):
                os.mkdir(path)
            else:
                shutil.rmtree(path)
                os.mkdir(path)
            with open(f"{path}/config.ini", "w") as outfile: 
                json.dump(parameters, outfile)
            os.system(f"python3 benchmark/benchmark.py -p {path} &")