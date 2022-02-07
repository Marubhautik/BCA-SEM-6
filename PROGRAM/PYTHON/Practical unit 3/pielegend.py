import matplotlib.pyplot as plt
import numpy as np
y = np.array([18,30,20,22])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
plt.pie(y, labels = mylabels)
plt.legend(loc='upper left')
plt.show()
