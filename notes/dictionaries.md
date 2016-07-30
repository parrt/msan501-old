# Dictionaries

## Goals

* Learn how to use a dictionary data structure
* See how hash tables implement dictionaries

## Description

### Review

We've seen one critical data structure already: the list, which looks like `[1,2,3]` or `['a','b','c']` or heterogeneously `[1,'a']`.  We also looked at a tuple `(a,b)` which is just a fixed list that cannot change in length and is immutable in that you cannot change the elements inside.  Assignments to multiple values is actually as a tuple:

```python
a,b = 1,2
(a,b) = (1,2) # same as previous
```

Both lists and tuples are accessed with the index operator `mylist[expr]` where `expr` is any expression evaluating to an integer. (Don't forget we can also nest these things `[a,[1,2],c]`.) Updating a list, we use `mylist[0] = newvalue`.

Loops can either iterate through the elements:

```python
for x in ['parrt','tombu']:
	print x
```

or use an index:

```python
a = ['parrt','tombu']
for i in range(len(a)):
	print a[i]
```

### The notion of a dictionary

It's time to turn to one of the most important abstract data structure you will need as a programmer: the *dictionary*. This is also called a *map*.

A dictionary behaves literally like a dictionary where you have a word or so-called *KEY* that you want to look up. In other words a dictionary stores *KEY*-*VALUE* pairs. It's also like a phone book where you look up somebody's phone number by their name. (Nobody can remember what phonebook is. ha!)

We can map any type to any other type. For example, we could map names to ages (string to ints),  words to definitions (string to string), filename to images (string to Image), name to child names (string to list), etc...

The set of key-value pairs is not typically considered ordered in any way, but one could sort them by key (making it a list not set of key-value pairs).

We can simulate a dictionary using the data structures we have already. All we need is a set of tuples with (key,value).

```python
>>> games = [('Wii Fit', 2007), ('Minecraft', 2012), ('Pac-Man', 1982)]
>>> type(games)
<type 'list'>
>>> type(games[0])
<type 'tuple'>
for g in games:
     print g[0], "maps to", g[1]
Wii Fit maps to 2007
Minecraft maps to 2012
Pac-Man maps to 1982
```

So this works great; we have an association.  But, we can't conveniently look things up by the key. We have to do everything by index.

```python
>>> print games['Minecraft']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: list indices must be integers, not str
>>> print games[2]
('Pac-Man', 1982)
```

We can find the index of a tuple, but that doesn't help us because we need to type in the key **and** the value to find it in a set of tuples.

```python
>>> games.index(('Minecraft', 2012))
1
>>> games.index(('Pac-Man', 1982))
2
```

If we already know the values, 2012 and 1982, we don't need to do the look up! What we need is a function that looks for a key within the set:

```python
def lookup(assocs,key):
	for a in assocs:
		if key==a[0]:
			return a[1]
	return None
```

Then we can do things like this

```python
>>> print lookup(games,'Minecraft')
2012
>>> print lookup(games,'Pac-Man')
1982
>>> print lookup(games,'foo')
None
```

It still doesn't let us use the fun syntax of `games['Minecraft']` though. For that, we would need to learn about finding `class`s in Python, which is beyond the scope of this class.

**Q.** What's wrong with this search strategy? 

It is a linear search.  Watch how slow this is:

```python
for i in xrange(500000000): pass 500M comparisons
```

It takes about 15 seconds on my machine.

Can we do any better? Yes, but it requires some trickery, as we will see later. For now, we will hide all of that and discuss the built-in `dict` object that does the trickery for us.

### Python `dict` objects

Rather than a list of associations, Python has a handy `dict` implementation of the abstract dictionary data structure. It is particularly handy because it lets us use syntax `games['Minecraft']`.

The syntax we use for dictionary literals is with curly braces instead of square brackets to define the list. But, we still use the square brackets to index into the dictionary. Here's the old and the new version

```python
games = [('Wii Fit', 2007), ('Minecraft', 2012), ('Pac-Man', 1982)]
games = {'Wii Fit':2007, 'Minecraft':2012, 'Pac-Man':1982}
type(games) # <type 'dict'>
```

Notice when I print it, out the order is not guaranteed

```python
>>> games
{'Pac-Man': 1982, 'Wii Fit': 2007, 'Minecraft': 2012}
```

Now we can do look things up with array syntax:

```python
>>> games['Minecraft']
2012
```

When we iterate over these things, it iterates over the keys:

```python
for g in games:
	print g, games[g]
Pac-Man 1982
Wii Fit 2007
Minecraft 2012
```

We can also walk the values:

```python
>>> for date in games.values(): print date
1982
2007
2012
```

And also get a list of associations:

```python
>>> for assoc in games.items(): print assoc
('Pac-Man', 1982)
('Wii Fit', 2007)
('Minecraft', 2012)
```

An empty dictionary is `{}` and then we can put stuff inside:

```python
phones = {}
phones['parrt'] = 5707
print phones # {'parrt': 5707}
```

If you use a wrong key, you get an exception:

```python
print phones['foo']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'foo'
```

**Q.** What is the difference between a list and a dictionary?

**Q.** Given example usage of a dictionary.

You can use `phones.clear()` to get rid of all keys in the dictionary.

You can delete a single element like this:

```python
>>> x = {'parrt':99, 'tombu':83}
>>> del x['parrt']
>>> x
{'tombu': 83}
```

Some [useful examples](http://learnpythonthehardway.org/book/ex39.html).  Here's one example from there:

```python
stuff = {'name': 'Zed', 'age': 39, 'height': 6 * 12 + 2}
```

**Exercise**. Write a program that asks the user to enter two student names and test scores. Use a `dict` to store a new record in the dictionary based on the student name (i.e. the name becomes the key) --  associate the student score with that key.  Once you have the dictionary built, simply print it out.  A sample session might look like:

```python
Enter student 1: parrt
Enter grade 1: 99
Enter student 2: tombu
Enter grade 2: 83
{'parrt': 99, 'tombu': 83}
```

Hint: you will need your friend the raw_input() function four times.

**Exercise**. Given 2 lists:

```python
names = ['Pac-Man', 'Wii Fit', 'Minecraft']
dates = [1982, 2007, 2012]
```

re-create the games dictionary we have above. First you need to create an empty dictionary called `games`. Then, you will need a loop that iterates `i` through the lists and stores the name and date into `games`. Finally print out your dictionary to make sure it looks right.

That exercise essentially re-implements function `zip`:

```python
>>> zip(names,dates)
[('Pac-Man', 1982), ('Wii Fit', 2007), ('Minecraft', 2012)]
```

### Hash tables

**Q.** Imagine you go to a conference and approach the table where people are handing out badges. What's the question they ask you and why?

A little bit more abstract function of the key:

**Q.** Imagine our goal is to find a particular person Eric Erickson in the United States. Where would you look first? Southern California or Minnesota?

It turns out that people that immigrated to the United States tended to cluster in regions where they had friends. There were a lot of Scandinavians that moved to Minnesota and, because of its proximity to Mexico, there are many people with Spanish last names in Southern California. That gives us a clue about how we might speed up the search.  

The key gives us a clue about how to restrict the region that we look. Imagine that a person's name uniquely told you in which state they live. That would mean searching only roughly 300M / 50 people instead of all 300M when you had no other information.

What we do is implement something called a "hash table" where we compute a function, a hash function, on the key and that gives us a bucket number that contains roughly *N*/*B* of the search elements for *B* buckets and *N* entries.

#### Creation

```python
# A hash table is a list of buckets
NBUCKETS=7
buckets = [[] for i in range(NBUCKETS)]
print buckets # [[], [], [], [], [], [], []]
```

For a hash function, let's assume all keys are strings and let's use the ASCII code of first letter as the  hash function

```python
>>> def hash(s): return ord(s[0])
>>> hash("Alaska")
104
>>> hash("Nevada")
112
```

#### Storing an association

To *put* something to the list (make an association), we use the hash code to get a bucket number. Since the hash code will be bigger than our number of buckets, we can just make the hash code wraparound using modulo:

```python
>>> hash("Alaska") % NBUCKETS
2
>>> hash("Nevada") % NBUCKETS
1
```

Once we have a bucket number, that gives us a list that we add an association to:

```python
b = hash("Alaska") % NBUCKETS
buckets[b].append(("Alaska", "AK"))
b = hash("Nevada") % NBUCKETS
buckets[b].append(("Nevada", "NV"))
print buckets # [[], [('Nevada', 'NV')], [('Alaska', 'AK')], [], [], [], []]
```

Notice that the hash is not unique and any key with the same hash function will have an association in the same bucket:

```python
b = hash("Oregon") % NBUCKETS
print b # 2
buckets[b].append(("Oregon", "OR"))
print buckets # [[], [('Nevada', 'NV')], [('Alaska', 'AK'), ('Oregon', 'OR')], [], [], [], []]
```

#### Looking up a key

To look up a key, we use the hash function to find a bucket and then linearly search within that bucket:

```python
def lookup(buckets, key):
    b = hash(key) % len(buckets)
    bucket = buckets[b]
    for assoc in bucket:
        if key==assoc[0]:
            return assoc[1]
    return None

print lookup(buckets, "Oregon") # "OR"
print lookup(buckets, "Nevada") # "NV"
```
