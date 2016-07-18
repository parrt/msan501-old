from runif import *
import math
import matplotlib.pyplot as plt
import numpy as np

N = 10 # sample size (i.e, array size len(X))
TRIALS = 15000 # how many samples we will take from the uniform distribution

# The CLT in a nutshell says that the sample mean, X_, of samples
# from many distributions follows the normal distribution.
# Specifically, N(m, sigma^2/N) for sample size N.
# Here, we are using the uniform distribution U(0,1)
# and verifying that taking lots of both samples and getting
# a histogram shows a normal distribution of N(0.5, ((1-0)^2/12)*N).

def unifvar(a, b):
	return ((b - a) ** 2) / 12.0

def normpdf(x, mu, sigma):
	u = - (x - mu)**2 / (abs(sigma)**2 * 2.0)
	y = (1.0 / (math.sqrt(2 * math.pi) * abs(sigma))) * math.e ** u
	return y

mu = 0.5 # theoretical population mean
X_ = []  # means of samples of size N from U(0,1)
for t in range(TRIALS):
	u = [runif01() for i in range(N)]
	X_.append(np.mean(u))

fig = plt.figure()
ax = fig.add_subplot(111)

# plot density of means (normalized histogram of means)
# WARNING: bins=60 is to show changes in resolution
# where normally it's best to let the hist() choose the
# bins for smoother view
plt.hist(X_, bins=60, normed=1)

# plot theoretical distribution: normal curve N(0.5, sigma^2 / N)
x = np.arange(min(X_), max(X_), 0.01)
sample_mean_var = unifvar(0, 1) / N
y = normpdf(x, mu, math.sqrt(sample_mean_var))
plt.plot(x, y, color='red')

plt.text(.02, .9, '$N = %d$' % N, transform=ax.transAxes)
plt.text(.02, .85, '$TRIALS = %d$' % TRIALS, transform=ax.transAxes)
plt.text(.02, .8, 'Obs. mean($\\overline{X}$) = %5.5f' % np.mean(X_), transform=ax.transAxes)
plt.text(.02, .75, 'Obs. var($\\overline{X}$) = %5.5f' % np.var(X_), transform=ax.transAxes)
plt.text(.02, .68, 'Obs. $\sqrt{var(\\overline{X})}$ = %3.3f' % np.sqrt(np.var(X_)), transform=ax.transAxes)
plt.text(.02, .63, 'stddev U($0,1$)/%d = %3.3f' % (N, np.sqrt(sample_mean_var)), transform=ax.transAxes)

plt.title("CLT Density Demo. sample mean of U(0,1) is $N(.5, \sigma^2/N)$")
plt.xlabel("$\\overline{X}$", fontsize=16)
plt.ylabel("Density", fontsize=16)
plt.savefig('clt-' + str(TRIALS) + '-' + str(N) + '-fancy.png', format="png",
			bbox_inches='tight', pad_inches=0.05)
plt.show()

