import numpy as np
import scipy.stats as sts
import matplotlib.pyplot as plt

def target_distribution(x):
    # distribution given in the prompt
    dist = sts.norm.pdf(x, loc=-4, scale=0.5) + sts.norm.pdf(x, loc=4, scale=1)
    return dist

dist_X = np.linspace(-7, 8, 1000)
dist_Y = target_distribution(dist_X)
plt.plot(dist_X, dist_Y)
plt.title('Unnormalized target distribution')
plt.show()