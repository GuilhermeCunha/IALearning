# Perceptron Algorithm on the Sonar Dataset
from random import seed
from random import randrange
from random import randint
from csv import reader
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Tratamento das entradas
data = pd.read_csv('F:\\Repositorios\\IALearning\\Projeto\\Aulas\\entrada.txt', sep=" ", header=None)
data.columns = ["comp", "larg", "flor"]
data = data[["comp", "larg", "flor"]]
predict = "flor"

x = np.array(data.drop([predict], 1))

d = np.array(data[predict])

learningRate = 0.05


y = 0

# BIAS
bias = 1

# Colocando o BIAS na ultima posicaoo de cada entrada
x = np.insert(x, 2, bias, axis=1)

print(x)
print(d)

# Weights
w = np.zeros(len(x[0]))

def iniciarPesos():
    for weight in range(0, len(w)):
        w[weight] = randint(-1,1)
    print("Initial Weights:")
    for weight in range(0, len(w)):
        print("   -", w[weight])
def recalcularPesos(dataIndex, expectedAnswer,sumObtained ):
    print("Changing the weights")
    # Realiza o calculo estocastico
    difference = expectedAnswer - sumObtained
    for weight in range(0, len(w)):
        w[weight] = w[weight] + learningRate * difference * x[dataIndex][weight]


def iniciarPerceptron(X, D, epochs):
    iniciarPesos()
    # Saida obtida
    Y = 0
    
    # X sao as entradas + BIAS
    # D eh a saida esperada
    # E eh o somatorio

    
    for epoch in range(0, epochs):
        print("Iniciando a epoca: ", epoch, "\n")
        # Numero de saidas certas
        hits = 0
        # Numero de saidas erradas
        errors = 0

        

        for data in range(0,len(X)):
            E = 0

            #Calcula o somatorio de todas as entradas multiplacas pelo seu peso
            for column in range(0, len(X[0])):
                E += X[data][column] * w[column]
            
            #Funcao de saida

            if(E >=0):
                Y = 1
            else:
                Y = 2

            # Guarda a resposta da saida esperada x saida obtida
            
            if(Y == D[data]):
                hits += 1
            else:
                print("This is a error")
                errors += 1
                recalcularPesos(dataIndex= data, expectedAnswer= D[data], sumObtained= E)

                # Recalcula os pesos utilizando o 
            print("Number of Hits: ", hits, "/",len(x))
            print("Number of Errors: ", errors,"/",len(x))

            print("Sum(E): ", E)
            print("Exit(Y): ", Y)
        
        if(hits == len(X)):
            print("All the answers are Hits!")
            print("Weights founds in the epoch ", epoch )
            for weight in range(0, len(w)):
                print("   -", w[weight])
            break
        else:
            print("Not learned yet")

iniciarPerceptron(x,d,100)
