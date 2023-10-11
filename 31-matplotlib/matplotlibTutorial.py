'''
https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
'''
import numpy as np 
import matplotlib.pyplot as plt 

# normal plot 
fig = plt.figure()
x = np.arange(0,2*np.pi,.1)
y = np.sin(x)
y2 = np.cos(x) 
'''
    r*  - start 
    ro  - circle 
    r-- - dashed line 
    r-  - line 
    b - blue
    g - green
'''
plt.plot(x,y,'b--')
plt.plot(x,y2,'g--')
plt.xlabel('time')
plt.ylabel('amplitude')
plt.title('my cool plot')
plt.legend(['sin','cos'])
plt.grid() 
plt.show() 

fig = plt.figure()
'''
    function: subplot
    parameter: 
        settings: row,col,index
''' 
plt.subplot(211)
plt.plot(x,y)
plt.subplot(212)
plt.plot(x,y2)
plt.show() 