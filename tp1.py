#TP python
import numpy as np
import pandas as pd
import matplotlib as plt

Fs = 500
Ts = 1/Fs
S1 = pd.read_csv("./presion_tp1.csv")

L = len(S1)
print(S1.values.reshape([1,L]).tolist())
print ("L:{0}".format(L))
k = np.arange(0,L)
t = k * Ts

pf = abs(np.fft.fft((S1.values.reshape([1,L]).tolist())))

rf = Fs/(L-1)
f = k*rf

Vmax_sensor = 1
Vmin_sensor = -1

Vmax_adc = 3.3
Vmin_adc = 0

G= (Vmax_adc - Vmin_adc) / (Vmax_sensor - Vmin_sensor)
offset = (Vmax_adc - Vmin_adc) / 2

S2 = S1 * G + offset

#imprimo
plt.subplot(2,1,1)
plt.plot(t,S1)
plt.grid()
plt.xlabel("t[s]")

plt.subplot(2,1,2)
plt.plot(pf)
plt.grid()
plt.xlabel("f")

plt.show()

