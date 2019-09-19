from random import seed
import random
from random import randrange
from random import randint
from csv import reader
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("/home/viniciusdantz/Documentos/Repositório Github/Python/IALearning/Projeto/Aulas/entrada.txt", sep=" ", names=["comp", "larg", "flor"])

x = np.array(data.drop(["flor"], 1))

d = np.array(data["flor"])

bias = 1

x = np.insert(x, 2, bias, axis=1)

# x_train, x_test, y_train, y_test = np.spl

w = [random.randint(-1, 1), random.randint(-1, 1), random.randint(-1, 1)]

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
                w[coluna] = x[linha][coluna]*(d[linha] - sum)*taxaApr+w[coluna]
    print("-----------------")
    print("Epoca ({0}):".format(epoch))
    print(acertos, erros)
    if(acertos == len(x)):
        print("Finalizou - epocas: {0}".format(epoch))
        break


#PLOTAR GRAFICO

for t in range(len(x)):
    if d[t] == 1:
        plt.scatter(x[t][0], x[t][1], color='red')
    else:
        plt.scatter(x[t][0], x[t][1], color='blue')


xp1 = ((-1) * w[2]) / w[0]
xp2 = ((-1) * w[2]) / w[1]
print(str(xp1) + "," + str(xp2))

pontos = [[0, xp1], [xp2, 0]]

z = np.polyfit(pontos[0], pontos[1], 1)
p = np.poly1d(z)
print("equação: ", p)
aux= np.arange(10)
yaux = p(aux)
print('Pesos: w1: '+ str(w[0]) + 'w2: '+ str(w[1]) + 'w3: '+ str(w[2]))

# Generates plot
plt.plot(aux, yaux, '-', color='black')
plt.show()
