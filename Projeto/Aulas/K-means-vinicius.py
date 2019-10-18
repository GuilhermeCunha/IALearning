import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import random as rd 
import math

data = pd.read_csv("C:\\Users\\aluno\\Documents\\VDP\\IALearning\\Projeto\\Aulas\\entrada.txt", sep=" ", names=["comp", "larg", "flor", "dist1", "dist2", "centr"])

data = np.array(data)
# print(data)

centds = []
k = 2
avg = []
lastcentr = []
distarray = np.zeros((len(data), k+3))

for item in range(k):
    centds.append([rd.uniform(0, 10), rd.uniform(0, 10)])
    avg.append([0, 0, 0])

while(centds != lastcentr):
    for i in range(len(data)):
        for j in range(len(centds)):
            if(data[i][0] > centds[j][0]):
                deltax = data[i][0] - centds[j][0]
            else:
                deltax = centds[j][0] - data[i][0]

            if(data[i][1] > centds[j][1]):
                deltay = data[i][1] - centds[j][1]
            else:
                deltay = centds[j][1] - data[i][1]

            dist = math.sqrt((deltax**2) + (deltay**2))
            distarray[i][0] = data[i][0]
            distarray[i][1] = data[i][1]
            distarray[i][j+2] = dist
        
        print(len(distarray[i]))
        #Se k == 2 então j == 1
        menor = 10000
        for m in range(len(distarray[i])):
            if(m < len(distarray[i]) - 1):
                if(m > 1 & distarray[i][m] < menor):
                    distarray[i][j+3] = m - 2
                    menor = distarray[i][m]
            
    for i in range(len(data)):
        for j in range(len(avg)):
            if(data[i][5] == 0):
                avg[j][0] += data[i][0]
                avg[j][1] += data[i][1]
                avg[j][2] += 1
            else:
                avg[j][0] += data[i][0]
                avg[j][1] += data[i][1]
                avg[j][2] += 1

    lastcentr = centds
    for i in range(len(avg)):
        centds[i][0] = avg[i][0]/avg[i][2]
        centds[i][1] = avg[i][1]/avg[i][2]

for i in range(len(data)):
    if(data[i][5]):
        plt.scatter(data[i][0], data[i][1], color='red')
    else:
        plt.scatter(data[i][0], data[i][1], color='blue')
        
plt.scatter(centds[0][0], centds[0][1], color='green')
plt.scatter(centds[1][0], centds[1][1], color='purple')
plt.show()