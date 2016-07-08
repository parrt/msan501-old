# Matrix operations

## Goals

* Represent matrices as lists of lists
* Use nested `for` loops
* Use list comprehensions for matrix construction
* Learn to factor code into bite-sized methods

The end result is file `matrix.py`.

## Description

### Lists of lists

Here is how we can create an N x N identity matrix represented as a list of N lists of length N:

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

Printing it out is simple:

```
A = identity(4)
print A
```

The <a href="http://www.pythontutor.com/visualize.html#code=def+identity(N%29%3A%0A++++%22Return+NxN+identity+matrix%22%0A++++I+%3D+%5B%5D+%23+make+an+empty+list%0A++++for+i+in+range(N%29%3A+%23+i+in+%5B0..N%29%0A++++++++row+%3D+%5B0%5D+*+N++%23+make+row+of+N+zeroes%0A++++++++row%5Bi%5D+%3D+1+++++%23+set+the+ith+column+to+1%0A++++++++I.append(row%29++%23+add+a+row+to+end+of+list%0A++++return+I%0A%0AA+%3D+identity(4%29&mode=display&origin=opt-frontend.js&cumulative=false&heapPrimitives=false&textReferences=false&py=2&rawInputLstJSON=%5B%5D&curInstr=23">list in memory</a> looks like:

<img src=figures/4x4-list.png width=300>

### Nested loops

Printing it out is kind of stinky:

```
[[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
```

To do a better job, we can make a function to print it out in 2D using a nested loop:

```python
def mprint(A):
    N = len(A)
    for i in range(N):
        for j in range(N):
            print A[i][j],
        print
```

Then, `mprint(A)` gives:

```
1 0 0 0
0 1 0 0
0 0 1 0
0 0 0 1
```

### Refactoring code

*Code you've written is not sacred* --parrt

Ok, let's see if we can improve the way we build identity matrices.  Cooler kids do this:

```python
def identity2(N):
    I = [[0] * N for i in range(N)]  # make N x N matrix
    for i in range(N): # set the diagonal to 1
        I[i][i] = 1    # set the ith row, ith column to 1
    return I
```

The list comprehension lets us avoid some awkwardness in our loop but we still need one to set the diagonal.

Here is a way to *refactor* the code so it is more clear and pulls out a useful helper method, `zero()`:

```python
def zero(N):
    return [[0] * N for i in range(N)]  # make N x N matrix

def identity3(N):
    I = zero(N)
    for i in range(N):
        I[i][i] = 1    # set the ith row, ith column to 1
    return I
```

Hmm...setting the diagonal might be useful in other cases, so let's factor that out too:

```python
def set_diagonal(I, x):
    N = len(I)
    for i in range(N):
        I[i][i] = x  # set the ith row, ith column to 1
    return I
```

Now we have a function that is much more clear than our original:

```python
def identity4(N):
    I = zero(N)  # make N x N matrix
    set_diagonal(I, 1)
    return I

```

In fact, we might want a diagonal matrix and so we can create:

```
def diagonal(N, x):
    I = zero(N)  # make N x N matrix
    set_diagonal(I, x)
    return I
```

Hmm...that looks familiar.  Yes, we can further simplify `identity` to:

```python
def identity2c(N):
    return diagonal(N, 1)
```

### Higher-order functions

Ok, more on nested loops. If we want to scale a matrix, can use the following function:

```python
def scale(A,x):
    "Scale matrix A by x in place; don't create a new one"
    N = len(A)
    for i in range(N):
        for j in range(N):
            A[i][j] *= x
    return A

A = identity(4)
scale(A,5)
mprint(A)
```

That gives us output:

```
5 0 0 0
0 5 0 0
0 0 5 0
0 0 0 5
```

But that nested loop is "boilerplate code", meaning that any function that needs to apply an operation to each element of a matrix will need to do that.  Let's factor that out into a function that takes a function as an argument!

```python
def apply(A,f):
    "Apply function f to every element of matrix A in place"
    N = len(A)
    for i in range(N):
        for j in range(N):
            A[i][j] = f(A[i][j]) # replace A[i][j]
    return A

A = identity(4)
def mult(x) : return 5 * x # this is applied to each element
apply(A, mult)
mprint(A)
```

That gives us the same output as before.

If you are a cool kid, you use a *lambda function*:

```python
A = identity(4)
apply(A, lambda x : 5 * x) # lambdas are just anonymous functions
mprint(A)
```

Notice that if we do

```python
apply(A, lambda x : 3.0 * x) # mult by floating-point
mprint(A)
```

We get a matrix with floating-point elements:

```
3.0 0.0 0.0 0.0
0.0 3.0 0.0 0.0
0.0 0.0 3.0 0.0
0.0 0.0 0.0 3.0
```

This info is very useful when doing the imaging project.