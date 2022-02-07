import matplotlib.pyplot as plt
import numpy as np
y = np.array([35, 25, 25, 15])
mylabels = ["BMW", "TESLA", "KIA", "TOYOTA"]
plt.pie(y, labels = mylabels)
plt.legend(title = "CAR:")
plt.show()
