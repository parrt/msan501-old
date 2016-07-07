# Scatter plots

## Goals

* Plot X vs Y as scatter plot
* More cool list comprehension use
* Fit a line to data with numpy
* Use of numpy's `arange()`

## Description

We often have several bits of data associated with the same entity. For example, here are some crime statistics for 50 US cities:
 
```python
# https://web.stanford.edu/~hastie/StatLearnSparsity_files/DATA/crime.html
crime_rate = [478, 494, 643, 341, 773, 603, 484, 546, 424, 548, 506, 819, 541, 491, 514,
              371, 457, 437, 570, 432, 619, 357, 623, 547, 792, 799, 439, 867, 912, 462,
              859, 805, 652, 776, 919, 732, 657, 1419, 989, 821, 1740, 815, 760, 936, 863,
              783, 715, 1504, 1324, 940]
highschool = [74, 72, 70, 71, 72, 68, 68, 62, 69, 66, 60, 81, 66, 67, 65, 64, 64, 62, 59,
              56, 46, 54, 54, 45, 57, 57, 61, 52, 44, 43, 48, 57, 47, 50, 48, 49, 72, 59,
              49, 54, 62, 47, 45, 48, 69, 42, 49, 57, 72, 67]
```

One of the things that we often look for is the relationship between related variables. Here is a plot of crime rate versus high school education:

<img src=figures/crime-highschool.png width=300>

Let's figure out how to create that graph:

```python
import matplotlib.pyplot as plt
... define data variables from above ...
plt.plot(highschool, violent, "ro")
plt.xlabel("% of people 25 years+ with 4 yrs. of high school", fontsize=16)
plt.ylabel("Violent crime rate per 100,000 residents", fontsize=16, rotation='vertical')
plt.show()
```

Eyeballing it, it doesn't seem like there's a strong correlation but what we really need is to draw a best fit line through that data. We will use `numpy`, so import it and use the `np.polyfit()` function:

```python
import numpy as np
fit = np.polyfit(highschool, violent, deg=1)
print fit # gives [m b] = [-10.6161118 1240.42737361]
```

Now we have the slope and Y intercept but most plot the points along that line. To plot the elements along the line we need to define a function that is the equivalent of `y = mx + b`:

```
def line(m, b, x):
    return m * x + b
```

Now, let's get a bunch of X values that are within the range of the X axis, `highschool` variable.  Then we can get the Y values:

```python
LEFT = round(min(highschool))
RIGHT = round(max(highschool))
linex = np.arange(LEFT, RIGHT, 0.1)
liney = [line(m, b, x) for x in linex]
```

Now all we have to do is plot:

```python
plt.plot(linex, liney, '--')
plt.title("Fit $y = %2.3f x + %2.3f$"%(m,b), fontsize=16)
```

This should give you the following graph:

<img src=figures/crime-highschool-fit.png width=300>