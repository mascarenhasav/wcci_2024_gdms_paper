#!/usr/bin/env python3

import json
import os
import shutil

NPEAKS = [1, 10, 35]
NOUT = [0]
NDIM = [2, 5, 10, 15, 20, 25, 35, 40, 45, 50]
#NPEAKS = [5]
#NOUT = [0]
#NDIM = [2]
METRICS = ["dmid", "dpw", "dtd", "dmi", "dmst", "drad"]
parameters = {}
parameters["NRUNS"] = 50
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
            path = f"wcci_2024_experiments"
            if(os.path.isdir(path)):
                shutil.rmtree(path)
            os.mkdir(path)
            path += f"/{peak}-{dim}"
            os.mkdir(path)
            with open(f"{path}/config.ini", "w") as outfile:
                json.dump(parameters, outfile)
            os.system(f"python3 benchmark/benchmark.py -p {path} &")
