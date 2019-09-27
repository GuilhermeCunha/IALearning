# -*- coding: utf-8 -*-
import random
import matplotlib.pyplot as plt
import numpy as np

data = [
    [0,0,0],
    [0,1,0],
    [1,0,0],
    [1,1,1]
]
x = []
'''
    [x1, x2, b]
x = [[0, 0, 1], 
    [0, 1, 1], 
    [1, 0, 1], 
    [1, 1, 1]]
'''
y = [] # y = [0, 0, 0, 1]
bias = 1
for i in data:
    d = i[:2] 
    d.append(bias)
    x.append(d)
    y.append(i[2])

# print(x)

epochs = 50

w = [random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)] # len(w) == 3 
#w = [0.5,0.6,-0.3]
tx_apr = 0.05
for epoch in range(epochs):
    erros = 0
    acertos = 0
    for linha in range(0, len(x)):
        sum = 0
        saida = 0
        for coluna in range(len(x[0])):
            sum += x[linha][coluna]*w[coluna]
        
        if(sum > 0):
            saida = 1
        else:
            saida = 0

        if saida == y[linha]:
            print("ACERTOU")
            acertos += 1
        else:
            erros += 1
            print("\n")
            print("ERROU")
            print("SAÍDA ESPERADA: ", y[linha])
            print("SOMA = ", sum)
            for coluna in range(0, len(w)):
                erro = y[linha] - saida
                print("{0} = {0} + ({1} * ({2} * {3}))".format(w[coluna], tx_apr, erro, x[linha][coluna]))
                w[coluna] = w[coluna] + (tx_apr * (erro * x[linha][coluna]))
            print("\n")
    print("Epoca: ", epoch)
    if(acertos == len(x)):
        print("Terminado - Acertou todas")
        break
    else:
        print("RN não perfeita\nAcertos: " , acertos)
        
print("w[0] = {0}\nw[1] = {1}\nw[2] = {2}".format(w[0], w[1], w[2]))

#PLOTAR GRAFICO

for t in range(len(x)):
    if y[t] == 1:
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
aux= np.arange(3)
yaux = p(aux)

# Generates plot
plt.plot(aux, yaux, '-', color='black')
plt.show()