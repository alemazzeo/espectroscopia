# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 18:29:43 2017

@author: ??
"""
import numpy as np
import matplotlib.pyplot as plt

#==============================================================================
# Arreglar esto
# from instrumentosProvisorios import Osciloscopio
#==============================================================================
from instruments import Instrument, Oscilloscope
import time


tec = Instrument(resource='USB0::0x1313::0x804A::M00404166::0::INSTR',
                 backend='', path='D:/ALUMNOS/Grupo 1/Espectro Rb')
osci = Oscilloscope(resource='USB0::0x0699::0x0363::C102220::0::INSTR',
                    backend='', path='D:/ALUMNOS/Grupo 1/Espectro Rb')

#==============================================================================
# Ejemplos:
# tec.write('SOUR:CURR 0.0015')
# tec.write('SOUR2:TEMP 25C')
#==============================================================================

#%%%
# Adquisición de temperatura:
def medir(cantidad='TEMP', n=10000, ax=None, **kwargs):
    Temp = np.zeros(n, dtype=float)
    Tiempo = np.zeros(n, dtype=float)
    for i in range(n):
        Tiempo[i] = time.time()    
        Temp[i] = tec.query('MEAS:%4s?' % cantidad, log=False)
        
    Tiempo = Tiempo - Tiempo[0]
    
    if ax is None:
        fig, ax = plt.subplots(1)
        
    ax.plot(Tiempo, Temp, **kwargs)
    return Tiempo, Temp
    