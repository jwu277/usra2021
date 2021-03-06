## Util for plotting data


import numpy as np
import matplotlib.pyplot as plt


# Histogram of nonnegative integer data
def int_hist(data):
    hist = np.bincount(data)
    plt.bar(np.arange(len(hist)), hist, width=1.0)


# Plot time response
def tr(x, dt):
    plt.plot(np.arange(0, dt * (len(x) + 1), dt)[:len(x)], x)


# Plot smooth phase portrait
# x = [x1(t), x2(t)]
def pp(x, ax=plt, **kwargs):
    ax.plot(x[:,0], x[:,1], **kwargs)


# Plot scattered phase portrait
# x = [x1(t), x2(t)]
def pp_scatter(x, step=1, s=12, c='k'):
    if c == 'heatmap':
        plt.scatter(x[::step,0], x[::step,1], s=s, c=np.linalg.norm(np.diff(x, axis=0, prepend=np.broadcast_to(x[0], (1, 2))), axis=1), zorder=2.5)
    else:
        plt.scatter(x[::step,0], x[::step,1], s=s, c=c, zorder=2.5)

