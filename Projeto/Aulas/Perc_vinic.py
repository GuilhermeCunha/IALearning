from random import seed
import random
from random import randrange
from random import randint
from csv import reader
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

data = pd.read_csv("/home/viniciusdantz/Documentos/Repositório Github/Python/IALearning/Projeto/Aulas/entrada.txt", sep=" ", names=["comp", "larg", "flor", "dist"])

x = np.array(data.drop(["flor", "dist"], 1))

d = np.array(data["flor"])

data = np.array(data)

bias = 1

x = np.insert(x, 2, bias, axis=1)

# x_train, x_test, y_train, y_test = np.spl

w = [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)]


taxaApr = 0.05

saida = 0

epochs = 1000

erro = False

for epoch in range(0, epochs):
    acertos = 0
    erros = 0
    for linha in range(0, len(x)):
        sum = 0
        for coluna in range(0, len(x[0])):
            sum += x[linha][coluna]*w[coluna]
        if sum < 0:
            saida = 2
        else:
            saida = 1
        if(saida == d[linha]):
            erro = False
            acertos += 1
        else:
            erro = True
            erros += 1
        if erro:
            for coluna in range(0, len(x[0])):
                w[coluna] = x[linha][coluna]*(d[linha] - sum)*taxaApr + w[coluna]
    print("--- Epoca ({0}): {1} {2} ---".format(epoch, acertos, erros))
    if(acertos == len(x)):
        print("--- Finalizou --- \n--- Epocas: {0} ---".format(epoch))
        break


#PLOTAR GRAFICO

for t in range(len(x)):
    if d[t] == 1:
        plt.scatter(x[t][0], x[t][1], color='red')
    else:
        plt.scatter(x[t][0], x[t][1], color='blue')


xp1 = ((-1) * w[2]) / w[0]
xp2 = ((-1) * w[2]) / w[1]
# print(str(xp1) + "," + str(xp2))

pontos = [[0, xp1], [xp2, 0]]

z = np.polyfit(pontos[0], pontos[1], 1)
p = np.poly1d(z)
# print("equação: ", p)
aux= np.arange(8)
yaux = p(aux)
print("--- Pesos ---\n--- w1 = {:.2f} ---".format(w[0]) + "\n--- w2 = {:.2f} ---".format(w[1]) + "\n--- w3 = {:.2f} ---".format(w[2]))

# Generates plot
plt.plot(aux, yaux, '-', color='black')
# plt.show()

""" predict = [6.4, 3.2]
sum = 0
for coluna in range(0, len(predict)):
    sum += predict[coluna]*w[coluna]
print(sum)
if sum < 0:
    print("\nSaida = 2")
else:
    print("\nSaida = 1") """
    
# print("Larg: \nMax = {0}\nMin = {1}\nComp:\nMax = {2}\nMin = {3}".format(max(data["larg"]), min(data["larg"]), max(data["comp"]), min(data["comp"])))
'''
Comp:
Max = 7.0
Min = 4.3
Larg: 
Max = 4.4
Min = 2.0
'''

predict = [random.uniform(0, 10), random.uniform(0, 10)]
# print(predict)

k = 3 #vizinhos

minors = []

for i in range(len(data)):
    if(data[i][0] > predict[0]):
        deltax = data[i][0] - predict[0]
    else:
        deltax = predict[0] - data[i][0]
        
    if(data[i][1] > predict[1]):
        deltay = data[i][1] - predict[1]
    else:
        deltay = predict[1] - data[i][1]
    
    dist = math.sqrt((deltax**2) + (deltay**2))
    data[i][3] = dist
    for j in range(k): # parei aqui - parte de colorar os vizinhos mais próximos em um array
        if(i == 0) minors = [data]
        if(minors[j] < data):