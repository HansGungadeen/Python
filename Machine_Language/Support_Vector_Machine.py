import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns; sns.set()


from sklearn.datasets.samples_generator import make_blobs
x, y = make_blobs(n_samples=100, centers=2, random_state=0, cluster_std=0.50)
plt.scatter(x[:, 0], x[:, 1], c=y, s=50, cmap='summer')
plt.show()

