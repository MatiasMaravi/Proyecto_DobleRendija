from math import atan2, cos, sin, pow, sqrt, pi, tan

def suma_dos_senos(amplitudA,amplitudB,faseA,faseB):
    amplitud_r = sqrt( pow((amplitudA*cos(faseA) + amplitudB*sin(faseB)),2) + pow((amplitudA*sin(faseA) + amplitudB*cos(faseB)),2)  )
    Fase = (pi/2) - atan2((amplitudA*cos(faseA) + amplitudB*sin(faseB)),(amplitudA*sin(faseA) + amplitudB*cos(faseB)))
    return (amplitud_r, Fase)



def patron_de_intensidad(Lambda,distancia,angulo,numero,lista):
    amplitudes = []
    Yp = distancia*tan(angulo)
    k = (2*pi)/Lambda
    for i in range(len(lista)-1):
        r1 = sqrt(pow(distancia,2)+pow((Yp-lista[i]),2))
        fase1 = k*r1
        r2 = sqrt(pow(distancia,2)+pow((Yp-lista[i+1]),2))
        fase2 = k*r2
        (A,f) = suma_dos_senos(lista[i],lista[i+1],fase1,fase2)
        amplitudes.append(pow(A,2))
    

    return amplitudes

