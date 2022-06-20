#TP python
import numpy as np
import pandas as pd
import matplotlib as plt

Fs = 500
Ts = 1/Fs
S1 = pd.read_csv("./presion_tp1.csv")
print(S1)

L = len(S1)
print(S1.values.reshape([1,L]).tolist())
print ("L:{0}".format(L))

k = np.arange(0,L)
t = k * Ts

pf = abs(np.fft.rfft((S1.values.reshape([1,L]).tolist())))  #en frecuencia

rf = Fs/(L-1) #resolución frecuencial
f = k*rf      #array de frecuencias

#grafico en tiempo 
plt.figure(1)
plt.plot(t,S1)
plt.grid(True)
plt.xlabel("t[s]")
plt.show()

Vmax_sensor = 1
Vmin_sensor = -1

Vmax_adc = 3.3
Vmin_adc = 0
#para obtener el rango dinámico

G= (Vmax_adc - Vmin_adc) / (Vmax_sensor - Vmin_sensor) #calculo la ganancia
offset = (Vmax_adc - Vmin_adc) / 2

S2 = S1 * G + offset         #señal escalada


S2_min = Vmin_adc
S2_max = Vmax_adc

#D1 (8bits)
N1 = 8
D1_min = 0
D1_max = 2**N1 - 1
D1 = round(S2* (D1_max / S2_max))       #señal para ADC
D1_float = S2* (D1_max/S2_max)          #señal con el valor flotante
E1 = D1 - D1_float                      #error
print ('D1: ', D1[0:10])
print ('\n D1 float: ', D1_float[0:10])
print ('\n Error: ', E1[0:10])

#D2 (12bits)
N2 = 12
D2_min = 0
D2_max = 2**N2 - 1
D2 = round(S2* (D2_max / S2_max))   #señal para ADC
D2_float = S2* (D2_max/S2_max)      #señal con el valor flotante
E2 = D2 - D2_float                  #error

#D3 (24bits)
N3 = 24
D3_min = 0
D3_max = 2**N3 - 1
D3 = round(S2* (D3_max / S2_max))   #señal para ADC
D3_float = S2* (D3_max/S2_max)      #señal con el valor flotante
error3 = D3 - D3_float              #error

N = D1.size
res_frec = float (Fs/(N-1))         #resolucion frecuencial
n = np.array(range(0,N))*res_frec

#espectros y módulos
esp1 = np.fft.rfft(D1)
esp2 = np.fft.rfft(D2)
esp3 = np.fft.rfft(D3)

mod1 = np.absolute(esp1)
mod2 = np.absolute(esp2)
mod3 = np.absolute(esp3)

#grafico en frecuencia
plt.figure(2)
g1 = plt.subplot (3,1,1)
plt.plot (n,mod1,'b')
plt.grid(True)
plt.xlabel('f[Hz]')

g2 = plt.subplot(3,1,2)
plt.plot (n,mod2,'b')
plt.grid(True)
plt.xlabel('f[Hz]')

g3 = plt.subplot(3,1,3)
plt.plot (n,mod3,'b')
plt.grid(True)
plt.xlabel('f[Hz]')
