# Generating pseudo-random numbers

## Goals

* Learn the difference between global and local variables
* Create functions to return uniform random variables in U(0,1) and U(a,b)

The end result is file `runif.py`.

Various people have been quoted as saying that insanity is doing the same thing over and over but expecting different results. That is exactly what we are hoping from our random number generator function. :)

## Description

To perform computer-based simulation we need to be able to generate random numbers. Generating random numbers following a uniform distribution are the easiest to generate and are what comes out of the standard programming language "give me a random number" function.  Here's a sample Python session:

```python
>>> import random
>>> print random.random()
0.154338190444
>>> print random.random()
0.167115291399
>>> print random.random()
0.107516067611
>>> 
```

We could generate real random numbers by accessing, for example, noise on the ethernet network device but that noise might not be uniformly distributed. We typically generate pseudorandom numbers that aren't really random but look like they are. From Ross' *Simulation* book,  we see a very easy recursive mechanism (recurrence relation) that generates values in [0,m-1]:

<img src=figures/runif-recurrence.png width=150>

That is recursive (or iterative and not *closed form*) because x_n is a function of a prior value:

<img src=figures/runif-recurrence2.png width=150>

To get random numbers between 0 and 1, we use x_n / m.

We must pick a value for `a` and `m` that make x_n seem random. Ross suggests choosing a large prime number for `m` that fits in our integer word size, e.g., `m = 2^31 - 1`, and `a = 7^5 = 16807`.

Initially we set a value for x_0, called the *random seed* (it is not the first random number). Every seed leads to a different sequence of pseudorandom numbers. (In Python, you can set the seed of the standard library by using `random.seed([x])`.

### Python implementation

Our goal is to take that simple recursive formula and use it to generate uniform random numbers. Function `runif01()` return a new random value **every** call. Use `m = 2^31 - 1`, `a = 7^5 = 16807`, and an initial seed of `x_0 = 666`.


```python
a = 16807
m = pow(2,31)-1
x = 666 # this is our x_n that changes each runif01() call

def runif01(): # U(0,1)
	global x
	x = a * x % m
	return x / float(m)
```

Let's try it out:

```
>>> print runif01()
0.00521236192678
>>> print runif01()
0.604166903349
>>> print runif01()
0.233144581892
```

Discuss global versus local variables.

### Setting new seed

Just because we want random numbers when we do simulation, doesn't mean that we don't want a reproducible sequence of random numbers. To do that, we set the seed, which just means resetting our `x` variable.

```python
def setseed(s): # updates the seed global variable
    global x
    x = s

setseed(666)
print runif() # we get the same sequence of random numbers
print runif()
print runif()
```

We can also set the seed to something else and get a different sequence, depending on the starting point.

```python
setseed(99)
print runif()
print runif()
print runif()
```

## Student exercise

Copy the global variables and `runif01()` function for above into `runif.py` and then defined this function that gives the uniform random variable between `a` and `b` instead of 0..1.

```python
def runif(a,b):
    ...
```

To get the shifted random variable, get one between 0..1 then multiply it by the range. Then add the initial `a` value. The following code

```python
setseed(99)
print runif(10,20)
print runif(10,20)
print runif(10,20)
```

should give you:

```
10.0077481056
10.2224102617
18.0492689731
```