import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

UAV_data = np.loadtxt("UAV_data.txt")
t, NO2_conc, x_coord, y_coord = UAV_data.T
plt.subplot(2,1,1)
plt.title("flight path of UAV")
plt.ylabel("y_coord")
plt.xlabel("x_coord")
plt.plot(x_coord, y_coord)
plt.subplot(2,1,2)
plt.title("NO2 conc over time")
plt.ylabel("NO2_conc")
plt.xlabel("t")
plt.plot(t, NO2_conc, color = "red")
plt.show()