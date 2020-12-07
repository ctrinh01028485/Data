import numpy as np
from matplotlib import pyplot as plt

ys =9 * np.random.randn(50)

for i in range(len(ys)):
    for j in range(i):
        if ys[i] < ys[j]:
            tmp = ys[i]
            ys[i] = ys[j]
            ys[j] = tmp

ya = np.random.randn(50) * 15

for i in range(len(ya)):
    for j in range(i):
        if ya[i] < ya[j]:
            tmp = ya[i]
            ya[i] = ya[j]
            ya[j] = tmp

x = [x for x in range(1970, 2020)]




plt.plot(x, ys, label='cám heo')
plt.plot(x, ya, label='cám lợn')

#plt.fill_between(x, ys, 197, where=(ys > 195), facecolor='r', alpha=0)
plt.legend()

plt.title("heo")
plt.show()




