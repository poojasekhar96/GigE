from __future__ import division
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

#focal lengths 
f1 = 125
f2 = 125

a=np.zeros((71,7))

m_actual = 1/4

print("%10s" % "u %12s" % "d %13s" % "m_diff %2s" % "v")

#d=distance between lenses
d=10

for i  in range (71):
	u = 325
	for j in range (7):

#calculating v and magnification m using ABCD ray optics formalism
#m=magnification
#v=distance from image to second lens


		v = (-1*(1-d/f2)*u - d) / ((d/(f1*f2)-1/f1-1/f2)*u+1-d/f1)
		
		m = 1 / ((d/(f1*f2)-1/f1-1/f2)*u+1-d/f1)

		a[i][j] = (abs(m)-m_actual) * 100/m_actual

		print("%7d %6d %8.3f %10.3f" % (u,d,a[i][j],v))

		u+=25
		j+=1
	print("***************************************")

	d+=1
	i+=1

ob = np.linspace(325,475,7)
t = np.linspace(10,80,71)
uu,dd = np.meshgrid(ob,t)

#plotting for various values of u & d
fig,ax = plt.subplots()
n = ax.pcolormesh(uu,dd,a,cmap='inferno')
cbar = fig.colorbar(n, ax=ax)

fig.tight_layout()
plt.xlabel('u (mm)',fontsize=18)
plt.ylabel('d (mm)',fontsize=18)
plt.title('125mm-125mm combination to image 1" beam spot', fontsize=20)

zed = [tick.label.set_fontsize(16) for tick in ax.yaxis.get_major_ticks()]
zed = [tick.label.set_fontsize(16) for tick in ax.xaxis.get_major_ticks()]
cbar.ax.tick_params(labelsize=16) 
cbar.set_label('magnification error(%)',fontsize=18)
plt.show()

