import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mpl
import numpy as np
import scipy.stats as stats

a = np.linspace(0, 4, 100)
expo = stats.expon
lambda_ = [0.5, 1]
colours = ["#348ABD", "#A60628"]

for l, c in zip(lambda_, colours):
    plt.plot(a, expo.pdf(a, scale=1./l), lw=3,
             color=c, label="$\lambda = %.1f$" % l)
    plt.fill_between(a, expo.pdf(a, scale=1./l), color=c, alpha=.33)

plt.legend()
plt.ylabel("PDF at $z$")
plt.xlabel("$z$")
plt.ylim(0,1.2)
plt.title("PDF of an Exponential random variable; differing $\lambda$")
plt.show()