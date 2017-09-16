import matplotlib.pyplot as plt
import numpy as np
from cycler import cycler

from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset

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

# Grid (color, estilo, espesor y transparencia)
plt.rc('grid', color='b0b0b0', linestyle='--', linewidth=0.8, alpha=1.0)

# Ejes (tamaño de la fuente)
plt.rc('axes', labelsize=14, titlesize=14)

# Errorbar
plt.rc('errorbar', capsize=2.0)

# Ejes (autoestilo para múltiples curvas)
lc_cycler = cycler('color', ['0.0', '0.5'])
lw_cycler = cycler('lw', [2, 1])
ls_cycler = cycler('ls', ['-', '--', ':', '-.'])
plt.rc('axes', prop_cycle=lw_cycler * ls_cycler)

# Modo interactivo

plt.ion()

###############################################
# FIGURAS PARA EL INFORME
###############################################


def plot_T_vs_t(t0=14200, tf=-1):
    tiempo, temp = np.load('medicion0.npy')
    tiempo = tiempo - tiempo[t0]

    fig, ax = plt.subplots()
    ax.plot(tiempo[t0:tf], temp[t0:tf])
    ax.grid()
    ax.set_xlabel('Tiempo (s)')
    ax.set_ylabel('Temperatura (ºC)')

    te = 46000
    te2 = -1
    mean = np.mean(temp[te:te2])
    std = np.std(temp[te:te2])

    axins = zoomed_inset_axes(ax, 6, loc=1, borderpad=2)
    axins.plot(tiempo[te:tf], temp[te:tf], ls='', alpha=0.7,
               marker='o', markersize=4, mfc='white')

    x1, x2, y1, y2 = tiempo[te], tiempo[te2], 24.999, 25.001
    axins.set_xlim(x1, x2)
    axins.set_ylim(y1, y2)

    axins.spines['right'].set_visible(True)
    axins.spines['top'].set_visible(True)

    axins.set_yticks([])
    axins.set_xticks([])

    mark_inset(ax, axins, loc1=1, loc2=3, fc="none", ec="0.5")

    axins.annotate('', xy=(tiempo[te + 600], mean + 2 * std),
                   xytext=(tiempo[te + 600], mean + 2 * std + 0.0005),
                   arrowprops={'arrowstyle': '->'})

    axins.annotate('', xy=(tiempo[te + 600], mean - 2 * std - 0.00008),
                   xytext=(tiempo[te + 600], mean - 2 * std - 0.0008),
                   arrowprops={'arrowstyle': '->'})

    error = '{:.2e}'.format(2 * std)

    axins.annotate(error, xy=(tiempo[te + 600], mean - 2 * std - 0.00075),
                   xytext=(tiempo[te + 640], mean - 2 * std - 0.00075),
                   verticalalignment='bottom',
                   horizontalalignment='left',
                   fontsize=13)

    print(tiempo[45000])
    print(mean)
    print(std)


def plot_espectro_temp():
    tiempo, temp, volt = np.load('medicion7.npy')

    volt = 0.11 - volt
    volt = volt / max(volt)

    picos = [177, 196, 234, 267]
    tp = [temp[i] for i in picos]
    vp = [volt[i] for i in picos]
    isotopos = ['87', '85', '85', '87']

    fig, ax = plt.subplots()
    ax.plot(temp[165:280], volt[165:280])
    ax.set_ylim(0, 1.25)
    ax.set_xlabel('Temperatura (ºC)')
    ax.set_ylabel('Absorción relativa')

    for i, isotopo in enumerate(isotopos):
        ax.annotate(r' ${}^{' + isotopo + r'}\mathbf{Rb}$',
                    xy=(tp[i], vp[i]),
                    xytext=(tp[i], vp[i] + 0.025),
                    fontsize=13,
                    horizontalalignment='left')

    ax.axvline(tp[0], ls='--', color='0.5')
    ax.axvline(tp[3], ls='--', color='0.5')

    ax.axvline(tp[1], ls=':', color='0.5', ymax=0.9)
    ax.axvline(tp[2], ls=':', color='0.5', ymax=0.9)

    ax.set_xticks(tp)
    ax.set_xticklabels(['{:.3f}'.format(t) for t in tp],
                       fontsize=13)

    ax.annotate('', xy=(tp[0], 1.18), xycoords='data',
                xytext=(tp[3], 1.18), textcoords='data',
                arrowprops={'arrowstyle': '<->'})

    ax.annotate('', xy=(tp[1], 1.05), xycoords='data',
                xytext=(tp[2], 1.05), textcoords='data',
                arrowprops={'arrowstyle': '<->'})

    xy1 = ((tp[3] + tp[0]) / 2, 1.20)
    xy2 = ((tp[2] + tp[1]) / 2, 1.07)

    f1 = r'$6,834 \, \mathrm{GHz}$'
    f2 = r'$3,035 \, \mathrm{GHz}$'

    ax.annotate(f1, xy=xy1, xytext=xy1,
                fontsize=12, horizontalalignment='center')
    ax.annotate(f2, xy=xy2, xytext=xy2,
                fontsize=12, horizontalalignment='center')


def plot_espectro(t0=350, tf=-1150):
    voltA, tiempoA, voltB, tiempoB = np.load('medicion4.npy')
    tiempo = tiempoA - tiempoA[t0]
    corriente = 140 * tiempo

    picos = [583, 807, 1067, 1188]
    xp = [corriente[i] for i in picos]
    yp = [voltB[i] for i in picos]
    isotopos = ['87', '85', '85', '87']

    fig, ax = plt.subplots(1)

    ax.plot(corriente[t0:tf], voltB[t0:tf])

    ax.set_xlabel(r'Var. de corriente ($\mu$A)')
    ax.set_ylabel('Respuesta del fotodiodo\n')
    ax.set_yticks([])

    for i, isotopo in enumerate(isotopos):
        ax.annotate(r' ${}^{' + isotopo + r'}\mathbf{Rb}$',
                    xy=(xp[i], yp[i]),
                    xytext=(xp[i], yp[i] - 0.004),
                    fontsize=13,
                    horizontalalignment='left')

    ax.axvline(xp[0], ls='--', color='0.5')
    ax.axvline(xp[3], ls='--', color='0.5')

    ax.axvline(xp[1], ls=':', color='0.5', ymax=0.9)
    ax.axvline(xp[2], ls=':', color='0.5', ymax=0.9)

    ax.set_xticks(xp)
    ax.set_xticklabels(['{:.3f}'.format(t - xp[2]) for t in xp],
                       fontsize=13)

    ax.annotate('', xy=(xp[0], 0.037), xycoords='data',
                xytext=(xp[3], 0.037), textcoords='data',
                arrowprops={'arrowstyle': '<->'})

    ax.annotate('', xy=(xp[1], 0.030), xycoords='data',
                xytext=(xp[2], 0.030), textcoords='data',
                arrowprops={'arrowstyle': '<->'})

    xy1 = ((xp[3] + xp[0]) / 2, 0.038)
    xy2 = ((xp[2] + xp[1]) / 2, 0.031)

    f1 = r'$6,834 \, \mathrm{GHz}$'
    f2 = r'$3,035 \, \mathrm{GHz}$'

    ax.annotate(f1, xy=xy1, xytext=xy1,
                fontsize=12, horizontalalignment='center')
    ax.annotate(f2, xy=xy2, xytext=xy2,
                fontsize=12, horizontalalignment='center')


def plot_diferencia(t0=1200, tf=1700):
    voltA, tiempoA, voltB, tiempoB = np.load('medicion1.npy')
    dif = voltA[0] - voltB[0]
    tiempo = tiempoA - tiempoA[0]
    corriente = 140 * tiempo - 0.08136
    frecuencia = corriente * 80400

    fig, ax = plt.subplots(2, sharex='all')
    fig.subplots_adjust(hspace=0.1)

    ax[0].plot(frecuencia[t0:tf], voltA[t0:tf],
               ls='-', lw=2.5)

    ax[0].plot(frecuencia[t0:tf], voltB[t0:tf] + dif,
               ls='-', lw=1)

    ax[1].plot(frecuencia[t0:tf], voltB[t0:tf] + dif - voltA[t0:tf],
               label='Resta', ls='-')

    ax[0].set_yticklabels([])
    ax[0].set_xlabel(' ')
    ax[0].set_ylabel('Fotodiodos')
    ax[0].grid()

    ax[1].set_yticklabels([])
    ax[1].set_xlabel('Var. de frecuencia ($MHz$)')
    ax[1].set_ylabel('Resta')
    ax[1].grid()
