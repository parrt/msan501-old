# Linked lists

## Goals

* Learn how to build a simple linked list using tuples/lists
* Examine the complexity of key operations

Here's a [sample implementation](https://github.com/parrt/msan501/blob/master/notes/code/linked_list.py).

## Description

We've studied arrays/lists that are built into Python but they are not always the best kind of list to use. Sometimes, we are inserting and deleting things from the head or middle of the list. If we do this with lists implemented as a raise (made up of contiguous cells in memory), we have to move a lot of cells around to make room for a new element or to close a hole made by a deletion.

*Linked list* implementations of abstract lists allow us to efficiently insert and remove things anywhere we want, at the cost of more memory.

### Metaphor for linked lists vs arrays

Imagine that I wanted to take roll in class. Since everyone is sitting next to each other, i.e. contiguous, I can simply point from one person to the next by looking to the left or right. That's the way lists work, as contiguous chunks.

A linked list requires everybody to not only remember their name but also who is to the right of them (a next pointer).  As long as I remember the first person in the list, I can call that person later and ask for their name. Then I can ask them to refer to the next person in line.  This works even if people distribute across the continent or randomly reassign where they are sitting. There is no requirement that these elements be contiguous because each node in the list has the information needed to get to the next person.

A linked list implementation associates a next pointer with each list value. We call these things *nodes* usually: `[value,next]` or `(value,next)`. We also keep a pointer to the *head* of the list and sometimes the *tail* of the list. (The only problem with our implementation will be that tuples don't let us name the elements.)

The simplest list has one element with a `next` pointer/reference that points at nothing.

```python
users = ("parrt", None)
```
<img src=figures/links1.png width=200>

Here's one with two elements:

```python
users = ("parrt", ("tombu", None))
```
<img src=figures/links2.png width=290>

and three elements:

```python
users = ("parrt", ("tombu", ("afedosov", None)))
```
<img src=figures/links3.png width=400>

Or, with lists not tuples, it's easier since we can alter the `next` pointer:

```python
a = ["parrt", None]
b = ["tombu", None]
c = ["afedosov", None]
users = a # points to first node of list
a[1] = b  # first node's next points to 2nd element
b[1] = c
```

The most basic implementation of a list is just a `head` pointer (here I'm using `users` for a specific list). Creating a linked list is then just a matter of saying `head=None`.

### Insertion

To insert something, say, `x` at the head of a linked list, there are two cases: an empty list and a nonempty list. An empty list is a case where `head=None`, the initial conditions of the list. A nonempty list of course will have `head` pointing at some tuple. Both cases can be handled the same way:

```python
head = [x, head]
```

That makes a new tuple holding the new value `x` and a `next` pointer pointing at the old head tuple. Finally, it sets the `head` pointer to point at the new tuple.

Technically I am using a list here because we need to be able to reset `next` pointers for deletion and tuples are immutable.

Inserting in the middle is more complicated. We need to find the node *after* which we want to insert something. Then we hook in the new node.

```python
a = ["parrt", None]
b = ["tombu", None]
c = ["afedosov", None]
users = a # points to first node of list
a[1] = b  # first node's next points to 2nd element
b[1] = c
# insert new node between b and c nodes
b[1] = ["mary", b[1]]
```

### Deletion

To delete the first node of a list, all we have to do is make the `head` point at what the first node's `next` points at. We want to say head.next but we don't know objects it.

```python
head = head[1]
```

or, if we define some nice constants to use (which are typically given in uppercase):

```python
VALUE = 0
NEXT = 1
head = head[NEXT]
```

## Walking a linked list

How do we walk a list? Well, we define a *cursor*  (often called `p` or `q`), which we can think of as just a finger we move along between the nodes in a list. Here's how to implement `a[j]` (get jth item) of a list:

```python
def getitem(j):
    "get ith node in the list starting from 0"
    i = 0
    p = head
    while p is not None:
        if i == j:
            return p
            i += 1
            p = p[NEXT]
    return None
```

Use the pythontutor.com to visualize the manipulation of the list. works great!

**Exercise**. After looking through `add` and `delete` and `show` functions, implement `len()`, which will return the number of elements in the list. Hint: start by cutting and pasting the body of `show()` and putting it into the body of `len()`.