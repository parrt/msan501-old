# Vectors

## Goals

* represent vectors as lists of numbers
* iterate with counter variable and `while`
* iterate with `for` loop
* use `print` variations

The end result is file `vectors.py`.

## Description

A vector from linear algebra is really just a list of numbers, which is how we can represent them in Python.

```python
v = [1, 2, 3]
w = [90,50,10]
```

Python doesn't inherently know how to do linear algebra. We can either pull in some libraries such as `numpy`, which we will do eventually, or we can build our own library functions such as for:

<center>
<img src=figures/dot-product.png width=400>
</center>

```python
def dot(v,w):
    "Return dot product of v and w or None if lengths are different"
    i = 0 # lists are 0-indexed
    if len(v)!=len(w):
        return None
    n = len(v)
    sum = 0
    while i < n:
        sum += v[i] * w[i]
        i += 1
    return sum
```

We can try that out with a simple statement:

```python
print dot(v,w) # gives 220
```

The idea of iterating a variable, `i`, from 0 to the length of a list - 1 is such a common pattern that almost all languages have something to automate this boilerplate code for us: `for` loops.

```python
n = 5
print range(0,5) # gives [0, 1, 2, 3, 4]
for i in range(5): # range(5) == range(0,5)
    print i, # comma on the end of a print means no \n
print # print with no arguments simply gives a \n
```

That prints `0 1 2 3 4`.

## Student exercise

Alter the `dot` function so that it uses a `for` loop instead of a `while` loop.

```python
def dot2(v,w):
    """
    Return dot product of v and w or None if lengths are different.
    Use for not while loop.
    Note:  triple quote allows newlines within comments
    """
    i = 0 # lists are 0-indexed
    if len(v)!=len(w):
        return None
    n = len(v)
    sum = 0
    ...
    return sum
```

Test it with a print statement to make sure you get 220 for the two vectors defined above.
