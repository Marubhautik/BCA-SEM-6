import matplotlib.pyplot as plt
import numpy as np
y = np.array([20,30,22,28])
mylabels= ["FLUTTER","ANDROID","PYTHON","JAVASCRIT"]
mycolor = ["blue","black","yellow","cyan"]
plt.pie(y,labels = mylabels,colors = mycolor)
plt.show()
