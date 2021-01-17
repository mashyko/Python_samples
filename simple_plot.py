
#an example of matplotlib usage 
 
import numpy as np 
import matplotlib.pyplot as plt  
 
t = np.arange(0.0, 2.0, 0.01) 
s = np.sin(2*np.pi*t)
 
plt.plot(t, s)
plt.title('sin(s)') 
plt.xlabel('time (s)')  
plt.ylabel('volts (mV)')         
plt.grid(True) 
plt.show()

# an example of pylab 
from pylab import *

t = np.arange(0.0, 2.0, 0.01)
s = np.sin(2*np.pi*t)
plot(t, s)

xlabel('time (s)')
ylabel('voltage (mV)')
title('About as simple as it gets, folks')
grid(True)
savefig("test.png")
show()
