import numpy as np
import pandas as pd

array1 = pd.read_csv('servo_current_OK_0.csv')
array1 = array1['current'].to_numpy()
array2 = pd.read_csv('servo_current_OK_1.csv')
array2 = array2['current'].to_numpy()

arr = []
arr.append([1,2,3])
arr.append([4,5,6])
arr.append([4,5,6])
np_arr = np.array(arr)
print(np_arr.shape)

# array3 = np.empty([2,10])
# print(array3)
# print(array3[0])