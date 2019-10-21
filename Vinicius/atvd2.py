import warnings
warnings.filterwarnings('ignore')
from sklearn.datasets import load_iris
import tensorflow as tf
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import keras
from keras import backend as k
from keras.models import Sequential
from keras.layers import Dense, Activation
import matplotlib.pyplot as plt

iris = pd.read_csv("/home/viniciusdantz/Documentos/Repositório Github/Python/entrada.txt", sep=" ",names=["comp", "larg", "target"])
# print(iris)
x ,y = np.array(iris[["comp", "larg"]]), np.array(iris['target'])
# print(x, y)

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, random_state=0)

x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, test_size=0.5)

print('Shape de x_train', x_train.shape)
print('Shape de x_val', x_val.shape)
print('Shape de x_test', x_test.shape)

print('Shape de y_train', y_train.shape)
print('Shape de y_val', y_val.shape)
print('Shape de y_test', y_test.shape)

fig, ax = plt.subplots(2, 2, figsize=(15,15))

for i in range(1):
    for j in range(1):
        # print(x_train.shape)
        ax[i,j].scatter(x_train[:, j], x_train[:, i+1], s=60, c=y_train)
        ax[i,j].set_xticks(())
        ax[i,j].set_yticks(())
        
        if i == 1:
            ax[i,j].set_xlabel(iris['comp'][j])
        if j == 0:
            ax[i,j].set_ylabel(iris['larg'][i + 1])
        if j > i:
            ax[i,j].set_visible(False)
model = Sequential()

# Layer de tamanho 16 e 2 atributos de flor (sepal x and y, petal x and y)
model.add(Dense(16, input_shape=(2,), activation=k.softmax))
model.add(Dense(8, activation=k.relu))
# 3 espécies de flor
model.add(Dense(3, activation='softmax'))
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

batch_size = 16
epochs = 400

# print(x_train, y_train)

history = model.fit(x=x_train, y=y_train,
                    batch_size=batch_size,
                    epochs=epochs,
                    verbose=1,
                    validation_data=(x_val, y_val))

# Plotando o historico do processo de treinamento
plt.figure(figsize=(20, 5))
plt.plot(history.history['loss'], color='blue')
plt.plot(history.history['val_loss'], color='red')
plt.title('Model loss', fontsize=20)
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['Treinamento', 'Validação'], loc='upper right', fontsize=14)
plt.show()

# 
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])
'''
x_new = np.array([[5, 2.9, 1, 0.2]])
prediction = model.predict(x_new)
print(prediction)
print(iris['target_names'][prediction.argmax()])
'''