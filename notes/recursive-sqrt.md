# Using recursion to compute n factorial

## Goals

* A first look at recursion
* Use recursion to implement recurrence relation

An old joke goes: *To truly understand recursion, one must first understand recursion.*

## Description

Recursion is one of those concepts that separates programmers from people that can make function calls to a library. It is critical to understanding how self-similar data structures, such as trees (random forest classifiers) and graphs (social networks), are constructed.

First the **good news**: recursion is the most natural expression of many computing tasks, particularly for iterative computations. The **bad news** is that the *recursive leap of faith* is hard for many programmers to get at first.

Let's start our study recursion with a baby problem: computing n factorial. That function computes the multiplication of all values from 1 to n:

<center>
<img src=figures/fact-pi.png width=80>
</center>

If we write that out in a different way, we will see an interesting pattern:

<center>
<img src=figures/fact-full.png width=350>
</center>

That's the same thing as saying:

<center>
<img src=figures/fact-recur.png width=140>
</center>

But we eventually have to make the *n-1* stuff "stop" and so we get the full definition:

<center>
<img src=figures/fact-complete.png width=200>
</center>

We can translate that the Python almost directly:

```python
def factorial(n):
    if n==0: return 1
    return n * factorial(n-1)
```

Here is the [source](code/fact.py) with some tests.

```bash
$ python fact.py
1
1
2
120
30414093201713378043612608166064768844377641568960512000000000000
```

The cool thing is that that basic pattern works with just about any recursive function we want.
