#TP python
import numpy as np
import pandas as pd
import matplotlib as plt

Fs = 500
Ts = 1/Fs
p = pd.read_csv("./presion_tp1.csv")

L = len(p)
print(p.values.reshape([1,L]).tolist())
print ("L:{0}".format(L))
k = np.arange(0,L)
t = k * Ts

pf = abs(np.fft.fft((p.values.reshape([1,L]).tolist())))

rf = Fs/(L-1)
f = k*rf

#imprimo
plt.subplot(2,1,1)
plt.plot(t,p)
plt.grid()
plt.xlabel("t[s]")

plt.subplot(2,1,2)
plt.plot(pf)
plt.grid()
plt.xlabel("f")

plt.show()

