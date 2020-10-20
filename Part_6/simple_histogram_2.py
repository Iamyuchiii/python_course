import numpy as np
import matplotlib.pyplot as plt

data = [9,18,13,9,6,6,16,6,17,10,15,16,13,11,13,8,20,6,18,11]

min_data = min(data)
max_data = max(data)
total_value = max_data - min_data + 1
my_bin = np.linspace(min_data, max_data, total_value) # min value, max value, total value wanted
my_bin2 = np.arange(min_data, max_data+1, 1) # min value, max value, steps from min to max

plt.xlabel('numbers')
plt.ylabel('something')
plt.title('Histogram of random data')
# put in text inside the histogram
# plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.hist(data, bins = my_bin)
plt.show()


