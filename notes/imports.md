# Importing library code

## Goals

* learn to import existing Python code
* use `dir` and `help` to learn about a package or function

## Description

Relying purely on built-in Python statements and expressions is fine except there are lots of very useful libraries we can use to save us lots of effort.

For example, let's import the standard `math` package (which we can think of as a library or file) and use some functions.  First, try to use the square root function without doing an `import`:

```python
print sqrt(100)
```

You will get the following error message: `NameError: name 'sqrt' is not defined`.

So try this:

```python
import math
print math.sqrt(100)
```

The `math` package has lots of functions. How do you know which functions?

```python
dir(math)
```

gives

```
['__doc__', '__file__', '__name__', '__package__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'hypot', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']
```

A better way is to use `help` (see the exercises below).

There are also constants available to you:

```python
print math.pi           # prints 3.14159265359
print math.e            # 2.71828182846
print math.cos(math.pi) # prints -1
```

## Student exercise

Try the following statement immediately after loading the Python interactive shell:

```python
print math.sqrt(100)
```

Despite giving the fully qualified name to the square root function, what does it say?

Now do the proper import and ask for help:

```python
import math
help("math")
help("math.sqrt")
```

