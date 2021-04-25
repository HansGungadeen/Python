import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns; sns.set()

from sklearn.datasets.samples_generator import make_blobs
x, y = make_blobs(n_samples=100, centers=2, random_state=0, cluster_std=0.50)
plt.scatter(x[:, 0], x[:, 1], c=y, s=50, cmap='summer')

xfit = np.linspace(-1, 3.5)
plt.scatter(x[:, 0], x[:, 1], c=y, s=50, cmap='summer')
plt.plot([0.6], [2.1], 'x', color = 'black', markeredgewidth = 4, markersize = 12)

for m, b in [(1, 0.65),(0.5, 1.6), (-0.2, 2.9)]:
    plt.plot(xfit,m*xfit + b, '-k')
plt.xlim(-1,3.5);
plt.show()