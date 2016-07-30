# Sets

A *set* is an abstract data structure representing a unique collection of elements. There is no implied order, unlike a list.  That said, you often see sets constructed from lists:

```python
a = ['dog', 'cat', 'dog', 'dog']
>>> s = set(a)
>>> type(s)
<type 'set'>
>>> print s
set(['dog', 'cat'])
```

You can still walk through a set, but you cannot rely on a specific order:

```python
for x in s:
	print x
```

Here's another typical use of sets, getting a bag of words from some text:

```python
s = "It was the best of times it was the worst of times"
wordlist = s.split(" ")
words = set(wordlist)
print words # set(['of', 'It', 'times', 'worst', 'it', 'the', 'was', 'best'])
```

We should normalize those words, which gives us an opportunity to see a list comprehension like expression used as an argument to a function:

```python
words = set(w.lower() for w in words)
print words # set(['of', 'it', 'times', 'worst', 'the', 'was', 'best'])
```

Much of the time we are adding values and testing for membership:

```python
words.add("dog")
print "dog" in words
print "foo" not in words
print "it" in words
```

You might also use the union and intersection operators:

```python
dogs = set(['fido','fuzzy'])
cats = set(['fuzzy','bonkers'])
dogs & cats      # set(['fuzzy'])
dogs | cats      # set(['fuzzy', 'fido', 'bonkers'])
len(dogs | cats) # 3
```

The implementation of sets is typically not an array data structure because checking membership is very common and should be fast. Walking an array to find an element is on the order *O(n)*, which is pretty slow for a large data structure. We will need to use a hash table like data structure to do that.

**Exercise**.  Split the following two sentences into words and turn them into two lowercase bag-of-words `set`s. Then figure out if there are any words in common using a set operator.

```python
s1 = "It is better to burn out than to fade away"
s2 = "How many ears must one man have before he can hear people cry"
...
```