# Dictionaries

## Goals

* Learn how to use a dictionary data structure
* See how hash tables implement dictionaries

## Description

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


Python's "dict" objects

It's time to turn to the next most important data structure you will need is a computer scientist: the dictionary. This is also called a "map" (e.g., is most frequent called a map in Java).

The dictionary behaves literally like a dictionary where you have a word or so-called KEY that you want to look up. In other words a dictionary stores KEY-VALUE pairs. It's also like a phone book where you look up somebody's phone number by their name.

we can map any type to any other type. For example, we could map names to ages (string to ints),  words to definitions (string to string), filename to images (string to Image) etc...

The key-value pairs are not typically not considered ordered in any way. In other words it is a set of keyvalue pairs not a list of keyvalue pairs.

We can simulate a dictionary using the data structures we have already. All we need is a set of tuples with (key,value).

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

So this works great we have an association. One thing it doesn't do for us is allows to look things up by the key. We have to do everything by index.

>>> print games['Minecraft']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: list indices must be integers, not str
>>> print games[2]
('Pac-Man', 1982)

We can find the index of a key however:

stuff = ['a', 'b', 'c']
stuff.index('c')
2

but that doesn't help us because we need to type in the key and the value to find it in a set of tuples.

games.index(('Minecraft', 2012))
1

If I already know the value, 2012, I don't need to do the look up.

what we need is a function that looks for a key within the set:

def lookup(assoc,key):
	for a in assoc:
		if key==a[0]:
			return a[1]
	return None

 then we can do things like this

lookup(games,'Minecraft')
2012

awesome.  It still doesn't let us use the funds syntax of games['Minecraft'] though.

What's wrong with this method anyway? It is a linear search. 

watch how slow this is:

x = [1]*50000000 # 50M elements in that list
for i in x:
     pass

it takes a few seconds on my machine.

Can we do any better? Yes, but it requires some trickery.

Question. Imagine our goal is to find a particular person Eric Erickson in the United States. Where would you look first? Southern California or Minnesota? It turns out that people that immigrated to the United States tended to cluster in regions because they had friends. There were a lot of Scandinavians then moved to Minnesota and because of its proximity to Mexico, there are many people with Spanish last names in Southern California. That gives us a clue about how we might speed up the search.  The key gives us a clue about how to restrict the region that we look. Imagine that a person's name uniquely told you in which state they live. That would mean searching only roughly 300M / 50 people instead of all 300M when you had no other information.

What we do is implement something called a "hash table" where we compute a function, a hash function, on the key and that gives us a bucket number that contains roughly N/B of the search elements for B buckets and N elements. This is an implementation detail, but you should know the term hash table and the strategy uses to improve search speed.

ANYway, this brings us back to a built-in data structure that handles all of this for us so that we can use syntax games['Minecraft'] and have it work extremely quickly rather than linearly as a function of the number of elements in the list.

The syntax we use is curly braces is that a square  brackets to define the list, but we still use the square brackets to index. Here's the old and the new version

games = [('Wii Fit', 2007), ('Minecraft', 2012), ('Pac-Man', 1982)]
games = {'Wii Fit':2007, 'Minecraft':2012, 'Pac-Man':1982}
type(games)
<type 'dict'>

notice when I printed out the order is not guaranteed

>>> games
{'Pac-Man': 1982, 'Wii Fit': 2007, 'Minecraft': 2012}


Now we can do:

games['Minecraft']
2012

when we iterate over these things they iterate over the keys:

for g in games:
	print g
Pac-Man
Wii Fit
Minecraft

 We can also walk the values:

>>> for v in games.values():
...     print v
... 
1982
2007
2012


empty dictionary is {} and then we can put stuff inside

phones = {}
phones['parrt'] = 5707
print phones

prints:

{'parrt': 5707}

 if you use a wrong key you get an exception:

print phones['dkfjfd']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'dkfjfd'

you can use phones.clear() to get rid of all keys in the dictionary

you can delete a single element like this:

>>> x = {'parrt':99, 'tombu':83}
>>> del x['parrt']
>>> x
{'tombu': 83}

some useful examples here that we can go over:

http://learnpythonthehardway.org/book/ex39.html

stuff = {'name': 'Zed', 'age': 39, 'height': 6 * 12 + 2}

EX: Write a program that asks the user to enter in two of student names and test scores. Use a Dictionary to store a new record in the dictionary based on the student name (i.e. the name becomes the key) – store the student score at that position.  Once you have the dictionary built, simply printed out.  A sample session might look like:

Enter student 1: parrt
Enter grade 1: 99
Enter student 2: tombu
Enter grade 2: 83
{'parrt': 99, 'tombu': 83}

Hint: you will need your friend the raw_input() function four times.

EX: given 2 lists

names = ['Pac-Man', 'Wii Fit', 'Minecraft']
dates = [1982, 2007, 2012]

re-create the games dictionary we have above. First you need to create an empty dictionary called games. Then, You will need a loop that walks through the lists and stores the name and date into games. Finally print out your dictionary to make sure it looks right.
