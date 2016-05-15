import matplotlib.pyplot as plt

F=[32,313]
C=[0,100]

plt.title('Convert Centigrade / Fahrenheit')
plt.ylabel('degrees Centigrade')
plt.xlabel('degrees Fahrenheit')
plt.xlim(32,212)                # try commenting this out...
plt.grid(True)
 
plt.plot(F,C)
plt.show()
