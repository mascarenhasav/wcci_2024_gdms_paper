#!/usr/bin/env python3

import json
import os
import shutil

def loadConfigFiles(pathConfig="."):
    #Read the parameters from the config file
    parametersFiles = ["parameters.ini"]
    parameters = {}
    for file in parametersFiles:
        if os.path.isfile(f"{pathConfig}/{file}"):
            with open(f"{pathConfig}/{file}") as f:
                p0 = list(json.loads(f.read()).items())
                for i in range(len(p0)):
                    parameters[f"{p0[i][0]}"] = p0[i][1]
        else:
            print(f"{file}", "FILE_NOT_FOUND", f"The {file} file is mandatory!")
    return parameters

parameters = loadConfigFiles()

path1 = parameters["PATH"]
#f"wcci_2024_experiments"

if(os.path.isdir(path1)):
    shutil.rmtree(path1)
os.mkdir(path1)

NPEAKS = parameters["NPEAKS"]
NOUT = parameters["NOUT"]
NDIM = parameters["NDIM"]

for peak in NPEAKS:
    for out in NOUT:
        for dim in NDIM :
            parameters["NPEAKS"] = peak
            parameters["NOUT"] = out
            parameters["NDIM"] = dim
            path = f"{path1}/{peak}-{dim}"
            os.mkdir(path)
            with open(f"{path}/config.ini", "w") as outfile:
                json.dump(parameters, outfile)
            os.system(f"python3 benchmark/benchmark.py -p {path} &")
