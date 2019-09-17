# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 18:24:00 2018

@author: jmarcos
"""
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

# Define o número de épocas da simulação e o número de atributos
numEpocas = 10000 #70000
numAmostras = 6

# Atributos
peso = np.array([113, 122, 107, 98, 115, 120])
pH = np.array([6.8, 4.7, 5.2, 3.6, 2.9, 4.2])

# For debugging purposes.
normaliza = False
if normaliza:
    peso = peso/np.linalg.norm(peso)
    pH = pH/np.linalg.norm(peso)


# bias
bias = 1

data = pd.read_csv('F:\\Repositorios\\IALearning\\Projeto\\Aulas\\entrada.txt', sep=" ", header=None)
data.columns = ["comp", "larg", "flor"]
data = data[["comp", "larg", "flor"]]
predict = "flor"

X = np.array(data.drop([predict], 1))

Y = np.array(data[predict])

# Entrada do Perceptron.
#X = np.vstack((peso, pH))   # Ou X = np.asarray([peso, pH])
print(X)
#Y = np.array([-1, 1, -1, -1, 1, 1])


# Taxa de aprendizado.
eta = 0.1

# Array para amazernar os erros.
e = np.zeros(6)

# Define a matriz de pesos.
W = np.ones([1,3])           # Duas entradas e o bias !

for j in range(numEpocas):
    for k in range(numAmostras):
     # Insere o bias no vetor de entrada.
     Xb = np.hstack((bias, X[:,k]))
     
     # Calcula o vetor campo induzido.
     V = np.dot(W, Xb)
     
     # Calcula a saída do perceptron.
     Yr = np.sign(V)
     
     # Calcula o erro: e = (Y - Yr)
     e[k] = Y[k] - Yr
     
     # Treinando a rede.
     W = W + eta*e[k]*Xb
     
#print(W)
print("Vetor de errors (e) = " + str(e))
