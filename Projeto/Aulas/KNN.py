import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# Assign colum names to the dataset
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']

# Read dataset to pandas dataframe
dataset = pd.read_csv(url, names=names)

print(dataset.head())

# Defines the entries
X = dataset.iloc[:, :-1].values
# Defines the  correct answer
y = dataset.iloc[:, 4].values


# Divide the Train/Test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)



# Catching the standad scaler
scaler = StandardScaler()
print("Scaler: ", scaler)

# Scale the features so that all of them can be uniformly evaluated
scaler.fit(X_train)
print("Scaler Fit: ", scaler.fit(X_train))

# Saving the x_train before scaler transformation
X_train_before = X_train
#print("X_train before the scaler transform: ", X_train)

# Putting the entries within scale
X_train = scaler.transform(X_train)


# Printing the Previous Entry X Later Entry
print('BEFORE| AFTER')
for i in range(len(X_train)):
    print(X_train_before[i][0], "|", X_train[i][0])

#print("X_train after the scaler transform: ", X_train)
X_test = scaler.transform(X_test)

# Define the number of K's 
classifier = KNeighborsClassifier(n_neighbors=5)

# Scale the features so that all of them can be uniformly evaluated
classifier.fit(X_train, y_train)

# Make predictions on the test data
y_pred = classifier.predict(X_test)
print(y_pred)


# Print the confusion matrix
print(confusion_matrix(y_test, y_pred))

# Print the scores
print(classification_report(y_test, y_pred))