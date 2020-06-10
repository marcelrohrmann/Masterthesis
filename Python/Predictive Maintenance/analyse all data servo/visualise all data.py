import pandas as pd
import numpy as np
from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

data = pd.read_csv('servo_data_all_0.csv')

print(data)

t = data['t'].to_numpy()
current = data['current'].to_numpy()
position = data['position'].to_numpy()
velocity = data['velocity'].to_numpy()
chip_temp = data['chip_temp'].to_numpy()

plt.plot(t, chip_temp)


plt.xlabel('Time (s)')
#plt.ylabel('Position (1/100°)')
#plt.ylabel('current (mA)')
plt.ylabel('chip_temp (°C)')
plt.savefig('servo_data_all_temp.png')
plt.show()
