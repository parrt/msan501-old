# Simple statements and functions

## Goals

* use assignment statements
* make a simple function and call it

The end result is file `area.py`.

## Description

Here are some simple Python statements to compute the area from a width and height:

```python
w = 10
h = 30
area = w * h
print area
```

**Something super important**: Programming languages (most but not all) execute one statement after the other, in order, and one statement finishes before the next is started. They are executed *synchronously*.

That is a very simple formula but we should get used to the practice of creating functions to encapsulate common bits of functionality like recipes.
 
```python
def area(w,h):
    return w * h

print area(10,30)
```

Add comment to `area`.

Notice that `w` and `h` are not visible before or after execution of the function:

```python
print w # "NameError: name 'w' is not defined"
```

Behavior of variables

* globals assigned to outside of a function
* global variables can be accessed by any statement in your program file (but not other files)
* locals assigned to inside of a function, not visible outside of that function; locals get created each time we call the function and they disappear when the function finishes.

Note that the general form of a Python program is:

&nbsp;&nbsp;&nbsp;&nbsp;*imports*

&nbsp;&nbsp;&nbsp;&nbsp;*global variable / constant definitions*

&nbsp;&nbsp;&nbsp;&nbsp;*function definitions*

&nbsp;&nbsp;&nbsp;&nbsp;*script code*

## Student exercise

do volume:

```python
def volume(w,h,l): # width, height, length
    ...

print volume(10,30,5)
```
