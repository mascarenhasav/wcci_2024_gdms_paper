import json
import os
import shutil

#NPEAKS = [1, 5, 25]
#NOUT = [0, 5 ,25]
#NDIM = [2, 10, 25]
NPEAKS = [1]
NOUT = [0, 5, 25]
NDIM = [2]
METRICS = ["dmd", "dpw", "dtd", "dmi"]
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
            path = f"{peak}-{out}-{dim}"
            if(os.path.isdir(path) == False):
                os.mkdir(path)
            else:
                shutil.rmtree(path)
                os.mkdir(path)
            with open(f"{path}/config.ini", "w") as outfile: 
                json.dump(parameters, outfile)
            os.system(f"python3 benchmark/benchmark.py -p {path} &")