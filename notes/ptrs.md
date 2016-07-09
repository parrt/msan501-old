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
