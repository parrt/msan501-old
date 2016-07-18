# Scatter plots

## Goals

* Plot X vs Y as scatter plot
* More cool list comprehension use
* Fit a line to data with numpy
* Use of numpy's `arange()`

## Description

We often have several bits of data associated with the same entity. For example, here are some public transit statistics:
 
```python
# http://journalistsresource.org/wp-content/.../Sample-data-sets-for-linear-regression1.xlsx
income = [5800, 6200, 6400, 6500, 6550, 6580, 8200, 8600, 8800, 9200, 9630, 10570, 11330,
          11600, 11800, 11830, 12650, 13000, 13224, 13766, 14010, 14468, 15000, 15200,
          15600, 16000, 16200]
riders = [192000, 190400, 191200, 177600, 176800, 178400, 180800, 175200, 174400, 173920,
          172800, 163200, 161600, 161600, 160800, 159200, 148800, 115696, 147200, 150400,
          152000, 136000, 126240, 123888, 126080, 151680, 152800]
```

One of the things that we often look for is the relationship between related variables. Here is a plot of  monthly income versus the number of weekly riders on public transit:

<img src=figures/income-riders.png width=400>

Let's figure out how to create that graph:

```python
import matplotlib.pyplot as plt
... define data variables from above ...
plt.plot(income, riders, "ro")
plt.xlabel("Monthly income in dollars", fontsize=16)
plt.ylabel("Weekly public transit riders", fontsize=16, rotation='vertical')
plt.show()
```

Eyeballing it, it seems like there's a strong correlation but what we really need is to draw a best fit line through that data. We will use `numpy`, so import it and use the `np.polyfit()` function:

```python
import numpy as np
fit = np.polyfit(income, riders, deg=1)
m, b = fit[0], fit[1]
print "m = %5.2f, b = %8.1f" % (m, b) # gives "m = -5.44, b = 220217.6"
```

Now we have the slope and Y intercept but must plot the points along that line. To plot the elements along the line we need to define a function that is the equivalent of `y = mx + b`:

```
def line(m, b, x):
    return m * x + b
```

Now, let's get a bunch of X values that are within the range of the X axis, `income` variable.  Then we can get the Y values:

```python
LEFT = round(min(income))
RIGHT = round(max(income))
linex = np.arange(LEFT, RIGHT, 0.1)
liney = [line(m, b, x) for x in linex]
```

Now all we have to do is plot:

```python
plt.plot(linex, liney, '--')
plt.title("Fit $y = %2.3f x + %2.3f$"%(m,b), fontsize=16)
```

This should give you the following graph:

<img src=figures/income-riders-fit.png width=400>