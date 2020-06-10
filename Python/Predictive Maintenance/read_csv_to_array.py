import pandas as pd
import numpy as np
from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

arr = []

for i in range(10):
    df = pd.read_csv('servo_current_OK_{}.csv'.format(i))
    df = df['current'].to_numpy()
    arr.append(df)

for i in range(10):
    df = pd.read_csv('servo_current_NOK_{}.csv'.format(i))
    df = df['current'].to_numpy()
    arr.append(df)
#0= OK ; 1= NOK


target = np.array([0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1])

data = np.array(arr)

data = np.load('data.npy')
# print the array
print(data)


print(target.shape)

classifier = svm.SVC(gamma=0.001, C=100)

print(len(data))

x,y = data[:-1], target[:-1]
classifier.fit(x,y)
print('prediction', classifier.predict([data[-1]]))



