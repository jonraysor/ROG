import matplotlib.pyplot as plt
import getInput as gi
from itertools import cycle
import math

colors = "bgrcmykw"
color_index = 0
gi.getNumFn()

gi.getFn()

gi.getUpper()


for i in range(int(gi.numFN)):
    pntToPlot = []
    numTested = []
    for j in range (1,int(gi.upper)):
        pntToPlot.append(((eval(gi.fns[i]))))
        numTested.append(j)
    plt.plot(numTested, pntToPlot, linewidth = 2, c=colors[color_index])
    color_index +=1

    plt.xlabel('N')
    plt.ylabel('Operations')
    plt.title('Rate of Growth')

plt.show()