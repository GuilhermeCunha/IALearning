# Imports 
'''
Pips

pip install matplotlib; pip install pandas;pip install numpy
'''

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random
from sklearn import svm


# Tratamento das entradas
data = pd.read_csv('F:\\Repositorios\\IALearning\\Projeto\\Aulas\\entrada.txt', sep=" ", header=None)
data.columns = ["comp", "larg", "flor"]
data = data[["comp", "larg", "flor"]]
predict = "flor"




# Lista de entradas [Comprimento, Largura]
x = np.array(data.drop([predict], 1))

X = x



# Respostas desejadas
d = np.array(data[predict])

'''
x = [[0, 0, 1],
     [0, 1, 1],
     [1, 0, 1],
     [1, 1, 1]]


w = [0.5, 0.6, -0.3]
d = [0, 0, 0, 1]
'''
print('-------------')

# Quant de X
nEntradas = len(x)

# BIAS
bias = 1

# Colocando o BIAS na ultima posição de cada entrada
x = np.insert(x, 2, bias, axis=1)

print(x)


# Quant Colunas de X
nColunasX = len(x[0])


# Pesos Aletórios (Sinapses)
w = [1, -1, 0.5]

# Quant de W
nPesos = len(w)

# Taxa de aprendizado (n)
txAprendizado = 0.1

# Saida
y = 0

# Resposta
resp = ""

# Soma
soma = 0

# Numero de Epocas
nEpocas = 1000



#Funcoes 

print("Inicando Treinamento...")
nAcertos = 0
for epoca in range(0, nEpocas):
    acertos = 0
    alteracaoDePeso = 0

    print("Pesos atuais")

    for cont in range(0, nPesos):
        print("Peso ", cont, ": ", w[cont])

    print("++++++++++++++++++++++++++++++++++++++")
    print("Epoca ", str(epoca))

    for entrada in range(0, nEntradas):
        soma = 0

        for coluna in range(0, nColunasX):
            soma += x[entrada][coluna] * w[coluna]

        # Funcao de saida

        if(soma >= 0):
            y = 1
        else:
            y = 2

        print("Entrada contabilizada: [", x[entrada][0], ",", x[entrada][1], "].")

        if y == d[entrada]:
            resp = "Acerto"
            acertos += 1
        else:
            resp= "Erro"
            erro = d[entrada] - soma
            # Alterando os pesos para tentar atingir um acerto
            for alt in range(0, nPesos):
                if alt != alteracaoDePeso:
                    # Alteracao de Tiago
                    '''
                    
                    w[alt] = w[alt] + txAprendizado * erro * x[entrada][alt]
                    '''
                    #w[alt] = w[alt] + txAprendizado
                    w[alt] = w[alt] + txAprendizado * erro * x[entrada][alt]

            if alteracaoDePeso == 0:
                alteracaoDePeso = 1
            else:
                alteracaoDePeso = 0

        print(resp, "Soma ", soma, "e saida ", y)

    if acertos == nEntradas:
        print("Funcionalidade aprendida apos ", epoca, " epocas.")
        print("Os pesos encontrados foram:")
        nAcertos = acertos

        for p in range(0, nPesos):
            print(w[p], " ")
        break

    print("")

print("\n\n")
print(nAcertos, " de 100 certos")

print("Finalizado")