import matplotlib.pyplot as plt
import numpy as np
y = np.array([40,10,30,20])
mylabels = ["BHAUTIK","HITESH","DHARMESH","ALI"]
myexplod = [0.2,0,0,0]
plt.pie(y,labels=mylabels,explode=myexplod,shadow= True)
plt.show()

