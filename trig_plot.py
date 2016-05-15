import matplotlib.pyplot as plt
from math import sin, cos, pi
 
npoints=50
x = [x*2*pi/npoints for x in range(npoints+1)]
y1 = [sin(t) for t in x]
y2 = [cos(t) for t in x]
 
plt.figure(figsize=(10, 5))
plt.title('Sine & Cosine')
plt.xlabel('t (radians)')
plt.ylabel('red: sin (t), blue: cos (t)')
plt.grid(True)
plt.xlim(0,2*pi)
plt.ylim(-1.1,1.1)
 
plt.plot(x, y1, color="red", label="sine")
plt.plot(x, y2, color="blue", label="cosine")
plt.legend()
 
plt.show()
