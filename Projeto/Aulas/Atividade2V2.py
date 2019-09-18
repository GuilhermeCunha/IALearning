'''
Instalacao dos imports
pip install pandas;pip install numpy;pip install matplotlib;
'''

# Perceptron Algorithm on the Sonar Dataset
from random import seed
from random import randrange
from random import randint
from csv import reader
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Tratamento das entradas
data = pd.read_csv(
    "C:\\Users\\aluno\\Downloads\\IALearning-Prod\\Projeto\\Aulas\\entrada.txt", sep=" ", header=None)
data.columns = ["comp", "larg", "flor"]
data = data[["comp", "larg", "flor"]]
predict = "flor"

x = np.array(data.drop([predict], 1))

d = np.array(data[predict])

learningRaE = 0.05


y = 0

# BIAS
bias = 1

# Colocando o BIAS na ultima posicao de cada entrada
x = np.insert(x, 2, bias, axis=1)

print(x)
print(d)

# Weights
w = np.zeros(len(x[0]))


def iniciarPesos():

    for weight in range(0, len(w)):
        w[weight] = randint(-1, 1)

    print("Initial Weights:")
    for weight in range(0, len(w)):
        print("   -", w[weight])


def recalcularPesos(dataIndex, expecEdAnswer, sumObtained):
    print("Changing the weights")
    # Realiza o calculo estocastico
    difference = expecEdAnswer - sumObtained
    for weight in range(0, len(w)):
        w[weight] = w[weight] + learningRaE * \
            difference * x[dataIndex][weight]


def iniciarPerceptron(X, D, epochs, endTraining):
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
        for data in range(0, endTraining):
            E = 0

            # Calcula o somatorio de todas as entradas multiplacas pelo seu peso
            for column in range(0, len(X[0])):
                E += X[data][column] * w[column]

            # Funcao de saida

            if(E >= 0):
                Y = 1
            else:
                Y = 2

            # Guarda a resposta da saida esperada x saida obtida

            if(Y == D[data]):
                hits += 1
            else:
                print("This is a error")
                errors += 1
                recalcularPesos(
                    dataIndex=data, expecEdAnswer=D[data], sumObtained=E)

                # Recalcula os pesos utilizando o
            print("Number of Hits: ", hits, "/", endTraining)
            print("Number of Errors: ", errors, "/", endTraining)

            print("Sum(E): ", E)
            print("Exit(Y): ", Y)

        if(hits == endTraining):
            print("All the answers are Hits!")
            print("Weights founds in the epoch ", epoch)
            for weight in range(0, len(w)):
                print("   -", w[weight])
            break
        else:
            print("Not learned yet")


def testarPerceptron(X, D, W, startAt):
    print("Starting the Tests!")
    # Numero de saidas certas
    hits = 0
    # Numero de saidas erradas
    errors = 0
    for data in range(startAt, len(X)):
        
        # Guarda o valor do somatorio
        E = 0
        
        # Calcula o somatorio de todas as entradas multiplacas pelo seu peso
        for column in range(0, len(X[0])):
            E += X[data][column] * W[column]

        # Funcao de saida

        if(E >= 0):
            Y = 1
        else:
            Y = 2
            
        if(Y == D[data]):
            hits += 1
        else:
            errors += 1
        print("Number of Hits: ", hits, "/", (len(X) - startAt))
        print("Number of Errors: ", errors, "/", (len(X) - startAt))
    if(errors == 0):
        print("The perceptron was perfectly trained")
    else:
        print("The perceptron was'nt perfectly trained")
        print("Acurracy: %.2f%%" % ((hits/startAt)* 100))

endTraining = 70
startEsting = endTraining + 1
iniciarPerceptron(x, d, 100, endTraining= endTraining)
testarPerceptron(x, d, w, startAt=endTraining)

print(len(x))