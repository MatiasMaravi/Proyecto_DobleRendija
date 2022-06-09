from math import atan2, cos, sin, pow, sqrt, pi
def suma_dos_senos(amplitudA,amplitudB,faseA,faseB):
    C = sqrt( pow((amplitudA*cos(faseA) + amplitudB*sin(faseB)),2) + pow((amplitudA*sin(faseA) + amplitudB*cos(faseB)),2)  )
    Fase = (pi/2) - atan2((amplitudA*cos(faseA) + amplitudB*sin(faseB))/(amplitudA*sin(faseA) + amplitudB*cos(faseB)))
    return (C, Fase)
