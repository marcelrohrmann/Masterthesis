import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score

from sklearn import svm
from sklearn.model_selection import train_test_split
# labelled data OK=0; NOK=1
target = np.array([0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1])
# import servo measurements
data = np.load('data.npy')
# define support vector machine algorithm
classifier = svm.SVC()
# split the data in training data and test data randomly by 50%
X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.5, shuffle=True)
# learn measurement on the first half of the measurement
classifier.fit(X_train, y_train)
# predict the value for second half of the measurement
prediction = classifier.predict(X_test)
# show the prediction
print('Prediction', prediction)
print(accuracy_score(y_test, prediction))
# label prediction with OK and NOK
prediction = np.where(prediction == 0, 'OK', prediction)
prediction = np.where(prediction == '1', 'NOK', prediction)
print(prediction)
# visualize the first 3 predictions
x_axis = np.arange(0,10, 0.05)
plt.xlabel('time (s)')
plt.ylabel('current (mA)')
plt.axis([0,10,0,800])
plt.plot(x_axis, X_test[0], 'b', label=prediction[0])
plt.plot(x_axis, X_test[1], 'g', label=prediction[1])
plt.plot(x_axis, X_test[2], 'r', label=prediction[2])
plt.axis([0,7,0,800])
plt.legend()
plt.show()


