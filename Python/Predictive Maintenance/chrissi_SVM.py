import pandas as pd
import numpy as np
from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

#ersten 10 werte OK=0; letzen 10 werte NOK=1
target = np.array([0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1])

#form [[messwerte],[messwerte],...]
data = np.load('data.npy')

# print the array
print(data.shape)
print(data)
print(target.shape)
print(len(data))

classifier = svm.SVC(gamma=0.001, C=100)

#train messwerte werte 0 bis 19
x,y = data[:-1], target[:-1]

classifier.fit(x,y)

#teste letzten messwert
# funktioniert nicht print('prediction', classifier.predict(data[-1]))
#nur mit [data[-1]??? array dimensionen falsch??
print('prediction', classifier.predict([data[-1]]))