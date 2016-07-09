# Objects versus primitive types

## Goals

* Learn to distinguish between primitives and objects
* Distinguish between types and values

## Description

Every value in a Python program is either a *primitive* or an *object*.  Numbers tend to be primitives, such as 23 and 99.2. More complicated objects such as strings and lists are objects. Every value has *type*, even though we don't have to declare the type as programmers (whereas we do in other programming languages like Java or C++).

```python
x = 1      # x is a memory cell holding a primitive value
y = "hi"   # y is a memory cell holding a reference to a string object
z = [1,2]  # z is a memory cell holding a reference to a list object
```

You can <a href="http://www.pythontutor.com/live.html#code=y+%3D+%22hi%22%0Az+%3D+%5B1,2%5D&mode=display&origin=opt-live.js&cumulative=false&heapPrimitives=true&textReferences=false&py=2&rawInputLstJSON=%5B%5D&curInstr=2">use Pythontutor to visualize</a> the objects.

The key distinction between objects and primitives is that more than one variable can refer to an object value.

```python
x = [1,2]
y = x
```

<img src=figures/shared-obj.png width=220>

If you change the elements of the object referred to by `y`, you are changing the object `x` refers to as well.

```python
x = [1,2]
y = x
y[0]=99
```

<img src=figures/shared-obj2.png width=225>

Another critical detailed understand about Python is how it compares objects and primitives. When we use the `==` operator, we are comparing the value of two expressions.

```python
>>> 10==10
True
>>> 10==5+5
True
>>> "hi"=="hi"
True
>>> "hi"=="mom"
False
>>> [1,5] == [1, 5]
True
```

Objects can have the same value even if they have different identities, meaning they are at physically different locations. For example, if we construct a string rather than simply reference it, the strings might be `==` but not the same physical object. For example, check out the following code in <a href="http://www.pythontutor.com/live.html#code=x+%3D+%5B1,5%5D%0Ay+%3D+%5B1,5%5D&mode=display&origin=opt-live.js&cumulative=false&heapPrimitives=false&textReferences=false&py=2&rawInputLstJSON=%5B%5D&curInstr=2">Python tutor</a>:

```
x = [1,5]
y = [1,5]
```

There are **two** separate lists in memory. `x==y` but crucially `x is not y`:

```python
>>> x == y
True
>>> x is y
False
>>> x is not y
True
```

The `id()` function returns the address of the object:

```python
>>> id(x)
4344545080
>>> id(y)
4344594088
```

This behavior is also true for string objects:

```python
>>> x = "hi"
>>> a = "h"
>>> b = "i"
>>> x==a+b
True
>>> x is a+b
False
>>> id(x)
4344354216
>>> id(a+b)
4344667352
```