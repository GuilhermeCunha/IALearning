import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import random as rd 
import math

data = pd.read_csv("C:\\Users\\aluno\\Documents\\VDP\\IALearning\\Projeto\\Aulas\\entrada.txt", sep=" ", names=["comp", "larg", "flor", "dist1", "dist2"])

data = np.array(data)
# print(data)

centds = []
k = 2

for item in range(k):
    centds.append([rd.uniform(0, 10), rd.uniform(0, 10)])

for i in range(len(data)):
    for j in range(len(centds)):
        if(data[i][0] > centds[j][0]):
            deltax = data[i][0] - centds[j]
        else:
            deltax = centds[j] - data[i][0]

        if(data[i][1] > centds[j][1]):
            deltay = data[i][1] - centds[j][1]
        else:
            deltay = centds[j][1] - data[i][1]

    dist = math.sqrt((deltax**2) + (deltay**2))
    if(j == 0):
        data[i][3] = dist
    else:
        data[j][4] = dist

