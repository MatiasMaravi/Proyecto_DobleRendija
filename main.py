from math import atan2, cos, sin, pow, sqrt, pi, tan
import matplotlib.pyplot as plt
import numpy as np
def suma_dos_senos(amplitudA,amplitudB,faseA,faseB):
    amplitud_r = sqrt( pow((amplitudA*cos(faseA) + amplitudB*sin(faseB)),2) + pow((amplitudA*sin(faseA) + amplitudB*cos(faseB)),2)  )
    Fase = (pi/2) - atan2((amplitudA*cos(faseA) + amplitudB*sin(faseB)),(amplitudA*sin(faseA) + amplitudB*cos(faseB)))
    return (amplitud_r, Fase)

#E0 = 1 para simplificar el problema

def patron_de_intensidad(Lambda,distancia,angulo,numero,lista):
    amplitudes = []
    lista_posiciones = []
    razon = (2*angulo)/(numero-1)
    for j in range(0,numero):
        Yp = distancia*tan(angulo)
        lista_posiciones.append(Yp)
        k = (2*pi)/Lambda
        r1 = sqrt(pow(distancia,2)+pow((Yp-lista[0]),2))
        fase1 = k*r1
        AMPLITUD_TOTAL = 1/r1
        FASE_TOTAL = fase1
        for i in range(1,len(lista)):
            r2 = sqrt(pow(distancia,2)+pow((Yp-lista[i]),2))
            fase2 = k*r2
            amplitud2 = 1/r2
            (A,f) = suma_dos_senos(AMPLITUD_TOTAL,amplitud2,FASE_TOTAL,fase2)
            AMPLITUD_TOTAL = A
            FASE_TOTAL = f
        amplitudes.append(pow(AMPLITUD_TOTAL,2))
        angulo-=razon
    x1 = np.linspace(0, numero,numero, endpoint=True)
    x2 = np.linspace(0, numero,numero, endpoint=True)
    plt.xlim(lista_posiciones)
    plt.ylim(amplitudes)
    plt.plot(x1,amplitudes,'o')
    plt.show()
    return amplitudes
    