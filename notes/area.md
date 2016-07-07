# Simple statements and functions

Here are some simple Python statements to compute the area from a width and height:

```python
w = 10
h = 30
area = w * h
print area
```

That is a very simple formula but we should get used to the practice of creating functions to encapsulate common bits of functionality like recipes.
 
```python
def area(w,h):
    return w * h

print area(10,30)
```

Notice that w and h are not visible before or after execution of the function:

```python
print w # "NameError: name 'w' is not defined"
```

Add comment to `area`.

Student exercise: do volume:

```python
def volume(w,h,d):
    ...

print volume(10,30,5)
```
