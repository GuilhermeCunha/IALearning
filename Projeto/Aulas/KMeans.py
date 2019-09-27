from sklearn.datasets import load_iris
from sklearn.preprocessing import scale
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

# Keeping the Raw Data
#iris = load_iris()
#print(rawData)

# Entries
#X = rawData.data[:, :3]
# Loading the Target
#y = rawData.target

#print(X)
#print(y)
#X, y = iris.data[:, :4], iris.target


# Tratamento das entradas
data = pd.read_csv("Projeto\\Aulas\\entrada.txt", sep=" ", header=None)
data.columns = ["length", "width", "class"]
data = data[["length", "width", "class"]]

# X[2] is the predicted class
X = np.array(data.drop(["class"], 1))
y = np.array(data["class"])

scaler = MinMaxScaler()
X = scaler.fit_transform(X)

Centroids = []
Classifications = []
K = 2

def cleanClassifications():
    for i in range(K):
        Classifications[K] = []
def euclidianDistance(point, centroid):
    distance = (
        (
            (
                pow((point[0] - centroid[0]), 2))
            +
            (
                pow((point[1] - centroid[1]), 2))
        )
    ) ** (1/2)
    #print("Distance between POINT AND CENTROID : ", point, " x " , centroid, " is ", distance)
    return distance
def distanceForCentroid(point, centroid, distanceType):
    if(distanceType == "Euclidian"):
        return euclidianDistance(point, centroid)

def meanOfPoints(index):
    #print("PointsClassifiedsByIndex ", PointsClassifiedsByIndex)

    sumLength = 0
    sumWidth = 0

    for i in range(len(Classifications[index])):
        sumLength += Classifications[index][i][0]
        sumWidth += Classifications[index][i][1]
    meanOfLenght = sumLength/len(Classifications[index])
    meanOfWidth = sumWidth/len(Classifications[index])

    #print("sumLength = ", sumLength)
    #print("sumWidth = ", sumWidth)
    #print("Classification LEN", index, ": ", len(Classifications[index]))

    
    #print("meanOfLenght = ", meanOfLenght)
    #print("meanOfWidth = ", meanOfWidth)
    #print("Classification LEN", index, ": ", len(Classifications[index]))
    #print("Classification ", index, ": " , Classifications[index])
    #print("Mean of Classification ", index, " : [" , meanOfLenght, ",", meanOfWidth, "]")
    return [meanOfLenght, meanOfWidth]

def initCentroids():
    print("Initializing Centroids")
    #Centroids.append([ 0,1])
    #Centroids.append([ 0,0.5])
    for i in range(K):
        dimension = []
        Centroids.append([random.uniform(0,1),random.uniform(0,1)])
        Classifications.append(dimension)
    #print("Initializing Centroids: Classifications")
    #print(Classifications)
    plt.title("INITIAL INFORMATION")
    for i in range(len(X)):
        plt.scatter(X[i][0], X[i][1], color='black')
    for i in range(K):
        plt.scatter(Centroids[i][0], Centroids[i][1], color='yellow')
    plt.show()

def changeCentroid(points, centroids):
    for i in range(K):
        print("Changing Centroid: ", centroids[i])
        centroids[i] = meanOfPoints(i)
    return centroids

def defineClasses(points, centroids):
    print("Defining the Classes")
    for i in range(len(X)):
        distancesForCentroids = []

        for z in range(K):
            distancesForCentroids.append(distanceForCentroid(points[i], centroids[z], "Euclidian"))
        indexOfMinDistance = np.argmin(distancesForCentroids)
        #print("DISTANCES: ", distancesForCentroids)
        #print("indexOfMinDistance: ", indexOfMinDistance)
        Classifications[indexOfMinDistance].append(points[i])
    #print("CLASSIFICATIONS 0: ")
    #print(Classifications[0])
    #print("CLASSIFICATIONS 1: ")
    #print(Classifications[1])
        
"""
Passo a passo

1) Inicializar os centroids aleatoriamente(centros de um cluster). [initCentroids()] OK
2) Para cada ponto na base de dados, calcular a distância para cada centroid e associar ao que estiver mais perto.
3) Calcular a média de todos os pontos ligados a cada centroid e definir um novo centroid (Repetir a etapas 2 e 3).
"""


# Plotando grafico


def startClassification():
    global Centroids
    initCentroids()
    nChanges = 0
    while True:
        print("GLOBAL CENTROIDS: ", Centroids)
        defineClasses(X, Centroids)
        newCentroids = changeCentroid(X, Centroids)
        title = "NEW CENTROID ", nChanges
        plt.title(title)
        for i in range(len(Classifications[0])):
            plt.scatter(Classifications[0][i][0], Classifications[0][i][1], color='blue')
        for i in range(len(Classifications[1])):
            plt.scatter(Classifications[1][i][0], Classifications[1][i][1], color='red')
        for i in range(K):
            if i % 2 == 0:
                plt.scatter(newCentroids[i][0], newCentroids[i][1], color='yellow')
            else:
                plt.scatter(newCentroids[i][0], newCentroids[i][1], color='black')
        plt.show()
        for i in range(K):
            needChange = False
            for z in range(K):
                if(newCentroids[i][z] != Centroids[i][z]):
                    needChange = True
                    break
            if(needChange):
                break
        if(needChange == False):
            print("Centroids Found...")
            title = "FINAL CENTROID ", nChanges
            plt.title(title)
            for i in range(len(Classifications[0])):
                plt.scatter(Classifications[0][i][0], Classifications[0][i][1], color='blue')
            for i in range(len(Classifications[1])):
                plt.scatter(Classifications[1][i][0], Classifications[1][i][1], color='red')
            for i in range(K):
                if i % 2 == 0:
                    plt.scatter(newCentroids[i][0], newCentroids[i][1], color='blue', s=150)
                else:
                    plt.scatter(newCentroids[i][0], newCentroids[i][1], color='red', s=150)
            plt.show()
            Centroids = newCentroids
            break
        else:
            print("Changing Centroids...")
            nChanges += 1
            Centroids = newCentroids


startClassification()
