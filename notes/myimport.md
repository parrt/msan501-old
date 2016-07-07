# Importing your own code

## Goals

* treat your own existing code like a library
* learn more about testing
* learn about the string `%` operator
* learn rules for when Python allows newlines
* learn not to compare floating-point numbers with `==`
* learn import aliases
* use numpy's `isclose()` function

The end result is file `test_stats.py`.

## Description

Let's say we have the following data for player heights of 40 randomly-selected US pro players:

```python
football = [
    6.329999924, 6.5, 6.5, 6.25, 6.5, 6.329999924, 6.25, 6.170000076,
    6.420000076, 6.329999924, 6.420000076, 6.579999924, 6.079999924,
    6.579999924, 6.5, 6.420000076, 6.25, 6.670000076, 5.909999847, 6, 5.829999924,
    6, 5.829999924, 5.079999924, 6.75, 5.829999924, 6.170000076, 5.75, 6, 5.75,
    6.5, 5.829999924, 5.909999847, 5.670000076, 6, 6.079999924, 6.170000076,
    6.579999924, 6.5, 6.25]

basketball = [
    6.079999924, 6.579999924, 6.25, 6.579999924, 6.25, 5.920000076, 7,
    6.409999847, 6.75, 6.25, 6, 6.920000076, 6.829999924, 6.579999924,
    6.409999847, 6.670000076, 6.670000076, 5.75, 6.25, 6.25, 6.5, 6,
    6.920000076, 6.25, 6.420000076, 6.579999924, 6.579999924, 6.079999924, 6.75,
    6.5, 6.829999924, 6.079999924, 6.920000076, 6, 6.329999924, 6.5,
    6.579999924, 6.829999924, 6.5, 6.579999924]
```

To compute the average height, we want to use our existing code but we don't want to cut-and-paste, which is a great sin. All we have to do is use the `import` statement like we did before with `math`:

```python
import stats
```

The only difference is that `stats.py` must be in the same directory as the `test_stats.py` file we are currently building. (Whereas `math.py` is off in some standard location of the disk Python knows to look for.)

```python
import stats

... define football and basketball ...
print "football mean is %f" % stats.mean(football)
print "basketball mean is %f" % stats.mean(basketball)
```

The `%` operator lets you create strings with "holes" in them where values get placed. I get output:

```
football mean is 6.186750
basketball mean is 6.453250
```

To test, we can use `assert` rather than `print` and eyeballing it:

```python
import stats
... define football and basketball ...
assert stats.mean(football)==6.186750
assert stats.mean(basketball)==6.453250
```

Whoops. It fails! Try this instead of asserts:

```python
print stats.mean(football)-6.186750
print stats.mean(basketball)-6.453250
```

It will tell you the difference is very very small but nonzero, which is why we can't test for equality:

```
-1.71500005308e-08
-2.09500017334e-08
```

Instead, we need to check if the difference is less than some small epsilon. Try this out:
 
```python
import stats
... define football and basketball ...
epsilon = 0.000000001
assert stats.mean(football)-6.186750 < epsilon
assert stats.mean(basketball)-6.453250 < epsilon
```

Another, more sophisticated way to check our work is to check it against an existing library that we know works.  Let's import our friend `numpy` that you will get very familiar with overtime. It has some built-in functions just like ours but also has `isclose()` which is a shorthand for `stats.mean(football)-6.186750 < epsilon` that we used previously. Try this out:
 
```python
import numpy as np  # lets us use np not numpy as a shorthand
from stats import * # lets us use mean,var,etc... w/o stats prefix

... define football and basketball ...

print "football mean is %f" % mean(football)
print "basketball mean is %f" % mean(basketball)

assert np.isclose(mean(football),   np.mean(football))
assert np.isclose(mean(basketball), np.mean(basketball))

assert np.isclose(var(football),    np.var(football,ddof=1))
assert np.isclose(var(basketball),  np.var(basketball,ddof=1))
```

The `ddof=1` is basically telling the variance function to use `N-1` not `N` as the denominator when computing the variance.

## Student exercise

Inline above.