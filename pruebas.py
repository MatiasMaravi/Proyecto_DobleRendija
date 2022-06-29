import numpy as np, matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.colors import LogNorm

a = 0.055
d = 7*a
b = 6.0
lam = 550
L = 1.20
pointsa =10
pointsb = 401
h = 20*a
c = b/7
pointsh = int(h/a*pointsa)
pointsc = int(pointsb*c/b)

pi = np.pi
k = 2*pi/lam*10**9

def r(x,y,xp,yp):
  r = np.sqrt((x*10**-2-xp*10**-3)**2+(y*10**-2-yp*10**-3)**2+L**2)
  return r

def fi(x,y,xp,yp):
  return k*r(x,y,xp,yp)

x = np.linspace(-b/2,b/2,pointsb)
y = np.linspace(-c/2,c/2,pointsc)
X,Y = np.meshgrid(x,y)

xp1 = np.linspace(-d/2-a/2,-d/2+a/2,pointsa)
xp2 = np.linspace(d/2-a/2,d/2+a/2,pointsa)

xp = np.concatenate((xp1,xp2))
yp = np.linspace(-h/2,h/2,pointsh)
sgridx,sgridy = np.meshgrid(xp,yp)
sgridx = sgridx.flatten()
sgridy = sgridy.flatten()

def intensity(x,y):
  Ex = np.sum(np.cos(fi(x,y,sgridx,sgridy)))
  Ey = np.sum(np.sin(fi(x,y,sgridx,sgridy)))
  return Ex**2 +Ey**2


intensities = np.zeros((pointsc,pointsb))
for i in range(pointsc):
  for j in range(pointsb):
    intensities[i,j] = intensity(X[i,j],Y[i,j])


x_pos = np.array([0,pointsb-1,(pointsb-1)/2])
xlabels = np.array(["0 cm", "{:} cm".format(b)])
plt.xticks(x_pos,xlabels,color='black',rotation=-90, \
fontsize='12',horizontalalignment='center')

y_pos = np.array([0,pointsc-1])
ylabels = np.array(["{:.2f} cm".format(c),"0 cm"])
plt.yticks(y_pos,ylabels,color='black',rotation=0, \
fontsize='12',horizontalalignment='right')

ax=plt.gca()
labels = [item.get_text() for item in ax.get_xticklabels()]
plt.xlabel("Double Slit Interference Pattern", fontsize='14', fontweight='bold')

plt.imshow(intensities,cmap=cm.gray,norm=LogNorm())