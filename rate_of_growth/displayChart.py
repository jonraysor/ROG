import matplotlib.pyplot as plt
import math
import getInput as gi

gi.getNumFn()

gi.getFn()

gi.getUpper()
pntToPlot = []
numTested = []

for i in range(int(gi.numFN)):
    for j in range (int(gi.upper)):
        pntToPlot.append(eval(gi.fns[i]))
        numTested.append(j)

    plt.plot(numTested, pntToPlot, c='red')
    plt.xlabel('N')
    plt.ylabel('Operations')
    plt.title('Rate of Growth')

plt.show()