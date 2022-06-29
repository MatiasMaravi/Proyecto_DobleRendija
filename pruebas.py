from math import atan2, cos, sin, pow, sqrt, pi, tan
import matplotlib.pyplot as plt
import numpy as np

LongitudOnda = 750*(10**-9)  # Rango rojo
DistanciaPantalla = 10 # metros
Angulo = np.pi/6 # radiane s
Puntos= 50  # Cantidad de puntos en la pantalla
PosicionesRendija=[10,8,6,4,2,0,-2,-4,-6,-8,-10] # 3 rendijas

def suma_dos_senos(amplitudA,amplitudB,faseA,faseB):
    amplitud_r = sqrt( pow((amplitudA*cos(faseA) + amplitudB*sin(faseB)),2) + pow((amplitudA*sin(faseA) + amplitudB*cos(faseB)),2)  )
    Fase = (pi/2) - atan2((amplitudA*cos(faseA) + amplitudB*sin(faseB)),(amplitudA*sin(faseA) + amplitudB*cos(faseB)))
    return (amplitud_r, Fase)

#E0 = 1 para simplificar el problema

def patron_de_intensidad(Lambda,distancia,angulo,numero,lista):
    amplitudes = []
    yps = []
    angulos  = np.linspace(-angulo,angulo,numero)
    razon = (2*angulo)/(numero-1)
    m = 0;
    for j in range(0,numero):
        Yp = distancia*tan(angulos[m])
        yps.append(Yp)
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
        m +=1

    return amplitudes,yps

amplitudes2,YPS = patron_de_intensidad(LongitudOnda,DistanciaPantalla,Angulo,Puntos,PosicionesRendija)

print(amplitudes2)
print(YPS)

matriz = []
t = 0
for i in range(0,len(amplitudes2)):
    temporal = []
    for j in range(0,200):
        temporal.append(amplitudes2[t])
    matriz.append(temporal)
    t+=1


plt.plot(YPS, amplitudes2)


pixel_plot = plt.figure()


plt.title("pixel_plot")
pixel_plot = plt.imshow(
    matriz,extent=[0, 200, 0, 800], cmap='binary', interpolation='nearest')

plt.show()

