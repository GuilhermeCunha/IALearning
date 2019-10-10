import numpy as np;
import pandas as pd;
import random as rd;
import math;

data = pd.read_csv("/home/viniciusdantz/Documentos/Repositório Github/Python/IALearning/Projeto/Aulas/entrada.txt", sep=" ", names=["comp", "larg", "flor", "dist"])

x = np.array(data.drop(["flor", "dist"], 1))

d = np.array(data["flor"])

data = np.array(data)

centr = [[rd.uniform(3, 8), rd.uniform(1, 5.5)], [rd.uniform(3, 8), rd.uniform(1, 5.5)]]

dist = math.sqrt((centr[0]**2)+(centr[1]**2))

for item in x:
    