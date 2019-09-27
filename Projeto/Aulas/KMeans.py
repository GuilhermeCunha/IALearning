from sklearn.datasets import load_iris
from sklearn.preprocessing import scale
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
X = np.array(data)
y = np.array(data["class"])


Centroids = []
Classifications = []
K = 2


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
    return distance
def distanceForCentroid(point, centroid, distanceType):
    if(distanceType == "Euclidian"):
        return euclidianDistance(point, centroid)

def meanOfPoints(index):
    PointsClassifiedsByIndex = Classifications[index]

    sumLength = 0
    sumWidth = 0

    for i in range(K):
        sumLength += PointsClassifiedsByIndex[0][i]
        sumWidth += PointsClassifiedsByIndex[1][i]
    meanOfLenght = sumLength/len(PointsClassifiedsByIndex)
    meanOfWidth = sumWidth/len(PointsClassifiedsByIndex)
    return [meanOfLenght, meanOfWidth]

def initCentroids():
    print("Initializing Centroids")
    for i in range(K):
        Centroids.append([random.uniform(0,1),random.uniform(0,1)])
    Classifications.append(np.empty((0,2)))
    

def changeCentroid(points, centroids):
    for i in range(K):

        print("Changing Centroid: ", centroids[i])
        centroids[i] = meanOfPoints(i)
    return centroids

def defineClasses(points, centroids):
    print("Defining the Classes")
    for i in range(K):
        distancesForCentroids = []

        for z in range(K):
            distancesForCentroids.append(distanceForCentroid(points[i], centroids[z], "Euclidian"))
        indexOfMinDistance = np.argmin(distancesForCentroids)
        for z in range(K):
            if(indexOfMinDistance == z):
                Classifications[z] = points[i]
    print("CLASSIFICATIONS: ")
    print(Classifications)
        


def startClassification():
    initCentroids()
    nChanges = 0
    changed = True

    while(changed):
        global Centroids
        defineClasses(X, Centroids)
        newCentroids = changeCentroid(X, Centroids)
        
        for i in range(K):
            needChange = False
            for z in range(K):
                if(newCentroids[i][y] != Centroids[i][y]):
                    needChange = True
                    break
            if(needChange):
                break
        if(needChange == False):
            print("Centroids Found...")
            break
        else:
            print("Changing Centroids...")
            nChanges += 1
            Centroids = newCentroids


startClassification()
