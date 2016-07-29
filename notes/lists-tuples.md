# Lists and tuples

## Goals

* Distinguish between lists and tuples
* Examine the cost of common operations

## Description

We've been playing with lists all along, but it's time to study them in more detail.

### (Array) Lists

A list is actually an abstract data structure in the sense that it does not specify the implementation.  And abstract data structure describes a set of operations that we can perform. For a list, the most common operations are *append element*, *insert element*, *get ith element*.

The most commonly-used implementation of a list is an *array*. In fact it is so common that we use the terms interchangeably.  An array is a fixed-size chunk of memory big enough to hold all elements of a list in a contiguous region.

A natural question is: how fast can we perform the list operations using an array implementation. Because computers are different speeds, we normalize things by counting the number of basic, atomic operations such as memory read/write and comparisons. We use notation *O(expression)*.

Q. How many operations does it take to fetch the ith element of an array?

Q. How about append?

Q. How about insert an element in the middle of an array?

### Tuples

A *tuple* in Python is really just a list but one that typically has heterogeneous elements. For example, we typically make lists of names or salaries. Tuples, on the other hand, allow us to group elements that should be treated together. We've already seen it when returning multiple elements from a function:

```python
def user():
    return "parrt",5707 # implicit tuple

name,id = user()
print name, id
```

Another way to write that is with parentheses around the name and the identifier:

```python
def user():
    return ("parrt",5707)

(name,id) = user()
print name, id
```

With the same function we can also capture the return tuple with a single variable and then access the elements like a list:
 
```python
t = user()
print t[0], t[1]
```

**Tuples are fixed size**. We could just as easily return `["parrt",5707]` from Python but I believe there is some efficiency gains when grouping data as fixed-size tuples. For example, the following is illegal for tuple `t`:

```python
t.append(99)
```

You get error:

```
AttributeError: 'tuple' object has no attribute 'append'
```

We use tuples to group data that should be held together; we are not thinking about the elements as a list, even if Python allows us to access the elements that way!

We will use tuples to represent nodes in data structures, such as linked lists and trees.