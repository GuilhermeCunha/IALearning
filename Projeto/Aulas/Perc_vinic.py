from random import seed
import random
from random import randrange
from random import randint
from csv import reader
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("C:\\Users\\aluno\\Documents\\VDP\\Projeto\\Aulas\\entrada.txt", sep=" ", header=None)
data.columns = ["comp", "larg", "flor"]
data = data[["comp", "larg", "flor"]]
predict = "flor"

x = np.array(data.drop([predict], 1))

d = np.array(data[predict])

bias = 1

x = np.insert(x, 2, bias, axis=1)

# x_train, x_test, y_train, y_test = np.spl

w = [random.randint(-1, 1), random.randint(-1, 1), random.randint(-1, 1)]

taxaApr = 0.05

saida = 0

epochs = 100000

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

fig, ax = plt.subplots()
for t in range(0,len(x)):
    plt.scatter(x[t][0], x[t][1])

plt.show()
