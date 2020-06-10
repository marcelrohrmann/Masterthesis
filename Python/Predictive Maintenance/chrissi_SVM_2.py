import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# labelled data OK=0; NOK=1
target = np.array([0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1])

# servo measurements
data = np.load('data.npy')
# support vector machine algorithm
classifier = svm.SVC()
# split the data in training data and test data randomly by 50%
X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.5, shuffle=True)
# e
classifier.fit(X_train,y_train)

print('Prediction', classifier.predict(X_test))

x_axis = np.arange(0,10, 0.05)


plt.plot(x_axis, X_test[0], 'b')
plt.plot(x_axis, X_test[1], 'g')
plt.plot(x_axis, X_test[2], 'r')
plt.axis([0,7,0,800])

plt.show()