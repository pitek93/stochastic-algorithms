import matplotlib.pyplot as plt
import numpy as np

mean, sigma = 0, 0.1 # mean and standard deviation
s = np.random.normal(mean, sigma, 1000)
count, bins, ignored = plt.hist(s, 30, normed=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mean)**2 / (2 * sigma**2) ), linewidth=9, color='r')
plt.show()