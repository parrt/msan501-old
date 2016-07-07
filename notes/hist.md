# Generating histograms

## Goals

* Learn the basics of using `matplotlib` to display probability density functions, which we approximate with *histograms*
* Use a *list comprehension* to collect values
* Slice a list

The end result is file `hist.py`.

## Description

We previously learned how to generate pseudorandom numbers. More specifically, these random numbers follow the uniform distribution. If we ask for 1000 pseudorandom numbers in U(2,8) using our `runif(2,8)` function, we should see a distribution that looks like the following.

<img src=figures/unif-2-8-density.png width=300>

The question is how do we get this display. First, let's figure out how to get 1000 random numbers using our old code:

```
from runif import *
N = 1000
X = [runif(2,8) for i in range(N)]
print X[0:4] # print elements 0, 1, 2, and 3
```

That last `X[0:4]` is called a slice operator. You can do lots of things like: `X[5:]` elements five through the end, `X[0:-1]` gives all but the last element.

In order to get a histogram, we need some boilerplate code:

```python
import matplotlib.pyplot as plt

fig = plt.figure() # get a handle on the figure object itself
... plotting stuff ...
plt.show()
```

To plot the histogram, we just use:

```python
plt.hist(X, normed=1)
```

If we want to say that image, we insert this before they `show()`:

```python
plt.savefig('unif-2-8-density.png', format="png")
```

which is what I did to get that image above.

Graphs should always have the axes labeled. Let’s do that as well as add a title and set the range of the graph. Put this code right before the `savefig()` or `show()`:

```python
plt.title("U(2,8) Density Demo")
plt.xlabel("X", fontsize=16)
plt.ylabel("Density", fontsize=16)
plt.axis([1, 9, 0, .25])
plt.text(2,.22, 'N = %d' % N, fontsize=16)
```

Now set N=30000 and try again. You should get a much more even distribution:

<img src=figures/unif-2-8-density-fancy.png width=300>

