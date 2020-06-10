import matplotlib.pyplot as plt
import numpy as np

x_axis = np.arange(0,10, 0.05)
data = np.load('data.npy')


plt.plot(x_axis, data[0],'b', label='OK')
#plt.plot(x_axis, data[1], 'g', label='ok')
plt.plot(x_axis, data[11], 'r', label='NOK')
#plt.plot(x_axis, data[11], 'm', label='NOK')
plt.xlabel('time (s)')
plt.ylabel('current (mA)')
plt.axis([0,10,0,800])
plt.legend()

plt.savefig('current_OK_vs_NOK.png')
plt.show()
