#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 20:02:13 2017

@author: batman
"""

import matplotlib.pyplot as plt
import numpy as np

#Importo ruta:
import os
os.chdir(r'/media/batman/Data/Facultad/Laboratorios/Labo V/Espect. de Rd/espectroscopia/Mediciones')

#%% Fluctuación de temperatura:
    
Tiempo0, Temp0 = np.load('medicion0.npy')
Fig0 = plt.figure()
plt.plot(Tiempo0, Temp0)
plt.show

#%% Modulación triangular en corriente:

Volt1A, Tiempo1A, Volt1B, Tiempo1B = np.load('medicion1.npy')
Fig1 = plt.figure()
plt.plot(Tiempo1A,Volt1A)
plt.plot(Tiempo1B,Volt1B)
plt.show


Resta2, Tiempo2R, Volt2, Tiempo2 = np.load('medicion2.npy')
Fig2 = plt.figure()
plt.plot(Tiempo2R,Resta2)
plt.plot(Tiempo2,Volt2)
plt.show

#Medición 3 y 4 son las mismas que 2, hay que ver cuál es la mejor o si 
#variamos algo

#Resta3, Tiempo3R, Volt3, Tiempo3 = np.load('medicion3.npy')
#plt.plot(Tiempo3R,Resta3)
#plt.plot(Tiempo3,Volt3)
#plt.show

#Resta4, Tiempo4R, Volt4, Tiempo4 = np.load('medicion4.npy')
#plt.plot(Tiempo4R,Resta4)
#plt.plot(Tiempo4,Volt4)
#plt.show

#%%Últimas mediciones: barrido en temperatura.

#Medición 5 y 6 son las mismas, ambas feas.
Temp5, Tiempo5 = np.load('medicion5.npy')
Fig5 = plt.figure()
plt.plot(Tiempo5[400:1000],Temp5[400:1000])
plt.show

Fig6 = plt.figure()
Temp6, Tiempo6 = np.load('medicion6.npy')
plt.plot(Tiempo6[150:2000],Temp6[150:2000])
plt.show

Fig7 = plt.figure()
Tiempo7, Temp7, Volt7 = np.load('medicion7.npy')
plt.plot(Temp7[160:300],Volt7[160:300])
plt.show
