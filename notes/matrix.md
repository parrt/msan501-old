# Matrix operations

## Goals

* Represent matrices as lists of lists
* Use nested `for` loops
* Use list comprehensions for matrix construction
* Learn to factor code into bite-sized methods

The end result is file `matrix.py`.

## Description

```python
def identity(N):
    "Return NxN identity matrix"
    I = [] # make an empty list
    for i in range(N): # i in [0..N)
        row = [0] * N  # make row of N zeroes
        row[i] = 1     # set the ith column to 1
        I.append(row)  # add a row to end of list
    return I
```

```python
def identity2(N):
    I = [[0] * N for i in range(N)]
    return I
```

```python
def zero(N):
    return [[0] * N for i in range(N)]  # make N x N matrix

def identity3(N):
    I = zero(N)  # make N x N matrix
    for i in range(N):
        I[i][i] = 1    # set the ith row, ith column to 1
    return I
```

```python
def set_diagonal(I, x):
    N = len(I)
    for i in range(N):
        I[i][i] = x  # set the ith row, ith column to 1
    return I

def identity4(N):
    I = zero(N)  # make N x N matrix
    set_diagonal(I, 1)
    return I

```

```python
def scale(A,x):
    "Scale matrix A by x in place; don't return a new one"
    N = len(A)
    for i in range(N):
        for j in range(N):
            A[i][j] *= x
    return A
```

