'''
Title: Code of the benchmark presented in 


Author: Alexandre Mascarenhas
Contact: https://mascarenhasav.github.io

Date: 2023/2
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import importlib
import datetime
import getopt
import sys
import csv
import shutil
import json
import os
from os import listdir
from os.path import isfile, join
from pathlib import Path

SMALL_SIZE = 8
MEDIUM_SIZE = 10
BIGGER_SIZE = 15
plt.rc('font', size=BIGGER_SIZE)          # controls default text sizes
plt.rcParams["figure.figsize"] = (7, 5)

colors_array = list(matplotlib.colors.cnames.keys())
markers_array = list(matplotlib.markers.MarkerStyle.markers.keys())
colors_array = ["red", "green", "blue", "orange", "black"]

def loadConfigFiles(pathConfig="."):
    #Read the parameters from the config file
    parametersFiles = ["config.ini"]
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

arg_help = "{0} -p <path>".format(sys.argv[0])
try:
    opts, args = getopt.getopt(sys.argv[1:], "hp:", ["help", "path="])
except:
    print(arg_help)
    sys.exit(2)

path = "./"
for opt, arg in opts:
    if opt in ("-h", "--help"):
        print(arg_help)  # print the help message
        sys.exit(2)
    elif opt in ("-p", "--path"):
        if arg != "./":
            path = arg

# Get a list of all items (files and directories) in the specified directory
all_items = os.listdir(path)

# Filter out directories
directories = [item for item in all_items if os.path.isdir(os.path.join(path, item))]

# Sort the list of directories alphabetically
directories = sorted(directories, key=lambda x: int(x))

METRICS = ["dpw", "dmst", "drad", "dmid"]
data = {"npeaks": [], "ndim": []}
data |= {metric: [] for metric in METRICS}
data |= {f"{metric}_std": [] for metric in METRICS}
print(directories)
#e()

for directory in directories:
    parameters = loadConfigFiles(f"{path}/{directory}")
    npeaks = directory
    data["npeaks"].append(int(npeaks))
    df = pd.read_csv(f"{path}/{directory}/results_average.csv")
    last_row = df.tail(1)
    print("----------")
    for metric in parameters["METRICS_TO_TEST"]:
        print(metric)
        value = last_row[metric].values[0]
        std = last_row[f"{metric}_std"].values[0]
        data[metric].append(value)
        data[f"{metric}_std"].append(std)
        print(f"{value:.4f}({std:.4f})")

#data["npeaks"].sort()
data["npeaks"] = np.asarray(data["npeaks"])

fig, ax = plt.subplots()
for i, metric in enumerate(METRICS):
    data[metric] = np.asarray(data[metric])
    data[f"{metric}_std"] = np.asarray(data[f"{metric}_std"])
    plt.plot(data["npeaks"], data[metric], fillstyle="none", markeredgewidth=1, linewidth=1, label=f"{metric}", marker=markers_array[i])
    ax.fill_between(data["npeaks"], data[metric] - data[f"{metric}_std"], data[metric] + data[f"{metric}_std"], alpha=0.1)

#plt.xlim(0, )
ax.set_yscale('log')
plt.ylim(0, 1)
plt.xlabel("Peaks")
plt.ylabel("Metric final value")
plt.grid(1)
plt.legend(loc='best')
plt.savefig("peaks.png")
plt.show()
