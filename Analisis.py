#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 20:02:13 2017

@author: batman
"""

import matplotlib.pyplot as plt
import numpy as np
from cycler import cycler

# Importo ruta:
import os
os.chdir(r'./Mediciones')

###############################################
# CONFIGURACIONES POR DEFECTO PARA LAS FIGURAS
###############################################

# Figura (tamaño)
plt.rc('figure', figsize=(8, 6))

# Figura (subplot)
plt.rc('figure.subplot', left=0.15)

# Ticks (tamaño de la fuente)
plt.rc(('xtick', 'ytick'), labelsize=14)

# Bordes de la figura (visibles o no)
plt.rc('axes.spines', left=True, bottom=True, top=False, right=False)

# Leyenda (tamaño de la fuenta y ubicación)
plt.rc('legend', fontsize=14, loc='best')


plt.rc('axes', titlesize=14)

# Ejes (tamaño de la fuente)
plt.rc('axes', labelsize=14)

# Errorbar
plt.rc('errorbar', capsize=2.0)

# Ejes (autoestilo para múltiples curvas)
lc_cycler = cycler('color', ['0.0', '0.5'])
lw_cycler = cycler('lw', [2, 1])
ls_cycler = cycler('ls', ['-', '--', ':', '-.'])
plt.rc('axes', prop_cycle=lw_cycler * ls_cycler)

# Modo interactivo

plt.ion()

#%% Fluctuación de temperatura:

Tiempo0, Temp0 = np.load('medicion0.npy')
Fig0 = plt.figure()
plt.plot(Tiempo0, Temp0)
#plt.title('Fluctuación de temperatura')
plt.grid()
plt.xlabel('Tiempo (s)')
plt.ylabel('Temperatura (ºC)')


#%% Modulación triangular en corriente:

t0 = 896

Volt1A, Tiempo1A, Volt1B, Tiempo1B = np.load('medicion1.npy')
Resta2, Tiempo2R, Volt2, Tiempo2 = np.load('medicion2.npy')
Dif = Volt1A[0] - Volt1B[0]
Tiempo1 = Tiempo1A - Tiempo1A[0]
TiempoR = Tiempo2R - Tiempo2R[t0]


Fig, ax = plt.subplots(2, sharex='all')
Fig.subplots_adjust(hspace=0.1)
ax[0].set_xlabel(' ')
ax[0].plot(Tiempo1, Volt1A)
ax[0].plot(Tiempo1, Volt1B + Dif)
ax[0].grid()
#ax[1].plot(Tiempo1,Volt1B + Dif - Volt1A, label='Resta')
ax[1].plot(TiempoR[t0:1896], Resta2[t0:1896], label='Resta')  # [896:1896]
# grafica 10mS
ax[1].grid()
plt.xlabel('Tiempo (s)')
plt.ylabel('Voltaje (mV)')

# Medición 3 y 4 son las mismas que 2, hay que ver cuál es la mejor o si
# variamos algo

#Resta3, Tiempo3R, Volt3, Tiempo3 = np.load('medicion3.npy')
# plt.plot(Tiempo3R,Resta3)
# plt.plot(Tiempo3,Volt3)

#Resta4, Tiempo4R, Volt4, Tiempo4 = np.load('medicion4.npy')
# plt.plot(Tiempo4R,Resta4)
# plt.plot(Tiempo4,Volt4)

#%%Últimas mediciones: barrido en temperatura.

# Medición 5 y 6 son las mismas, ambas feas.

# Tarda menos => a favor de la temperatura ambiente?
Volt5, Tiempo5 = np.load('medicion5.npy')
Fig5 = plt.figure()
plt.plot(Tiempo5[450:850] - Tiempo5[450], Volt5[450:850])
plt.title('Barrido en temperatura')
plt.grid()
plt.xlabel('Tiempo (s)')
plt.ylabel('Voltaje (mV)')

# Tarda más => en contra de la temperatura ambiente?
Fig6 = plt.figure()
Volt6, Tiempo6 = np.load('medicion6.npy')
plt.plot(Tiempo6[200:2050] - Tiempo6[200], Volt6[200:2050])
plt.title('Barrido en temperatura')
plt.grid()
plt.xlabel('Tiempo (s)')
plt.ylabel('Voltaje (mV)')

Fig7 = plt.figure()
Tiempo7, Temp7, Volt7 = np.load('medicion7.npy')
plt.plot(Temp7[160:300], Volt7[160:300])
#plt.title('Barrido en temperatura')
plt.grid()
plt.xlabel('Temperatura(ºC)')
plt.ylabel('Voltaje (mV)')
