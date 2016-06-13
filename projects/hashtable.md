# Search Engine Implementation

The goal of this project is to learn how hashtables work and to *feel* just how much slower a linear search is. Along the way, you'll learn the basic mechanics of implementing a search engine, including displaying search results in a browser window and being able to navigate to documents. You'll also learn a tiny bit of HTML.

## Discussion

A **search engine** accepts one or more **terms** and searches a corpus for files matching all of those terms.  A **corpus** is just a directory and possibly subdirectories full of text files. If you go to the [American National corpus](http://www.anc.org/data/oanc/contents/), you'll see lots of fun text data. I have extracted articles from [Slate](https://github.com/parrt/msan501/blob/master/data/slate.7z) magazine and also from [Berlitz travelogues](https://github.com/parrt/msan501/blob/master/data/berlitz1.7z).  These are your data sets.  Berlitz is smaller and so I use that in some of my [unit tests](https://github.com/parrt/msan501-starterkit/blob/master/hashtable/test_search.py).  Here is a fragment of a sample search results page as displayed in Chrome (activated from Python):

<img src="figures/search-page.png" width=300>

Clicking on a link brings up the actual file:

<img src="figures/search-file-page.png" width=300>

You're going to implement 3 different search mechanisms:

1. Linear search; file [linear_search.py](https://github.com/parrt/msan501-starterkit/blob/master/hashtable/linear_search.py)
2. Hashtable via built in Python `dict` objects; file [index_search.py](https://github.com/parrt/msan501-starterkit/blob/master/hashtable/index_search.py)
3. Hashtable that you implement yourself; file [myhtable_search.py](https://github.com/parrt/msan501-starterkit/blob/master/hashtable/myhtable_search.py)

All three mechanism should give exactly the same results, but you will notice that the linear search is extremely slow. On my really fast machine with an SSD, it takes about five seconds to search through the Slate data. With either of the hash tables, it's a matter of milliseconds.

File [search.py](https://github.com/parrt/msan501-starterkit/blob/master/hashtable/search.py) is the main program, which you execute like this:

```bash
$ python search.py linear ../data/slate
$ python search.py index ../data/slate
$ python search.py myhtable ../data/slate
```

assuming you have placed the `slate` directory under a `data` directory at the same level as your `hashtable` project code (`~/msan501/data`).

### Linear search

Your first task is to perform a brain-dead linear search, which looks at each file in turn to see if it contains all of the search terms. If it does, that filename is included in the set (not list) of matching documents.

Given a list of fully-qualified filenames containing the search terms, the main program uses function `results()` to get a string containing HTML, widget rights to file `/tmp/results.html'. It then requests, via `webbrowser.open_new_tab()` that your default browser open that page.

### HTML output

You can create whatever fancy HTML you want, but here is the basic form you should follow:

```
<html>
<body>
<h2>Search results for <b>ronald reagan</b> in 164 files</h2>
    
    <p><a href="file:///Users/parrt/github/msan501/data/slate/15/Article247_3872.txt">/Users/parrt/github/msan501/data/slate/15/Article247_3872.txt</a><br>
    relationship with Ronald Reagan, whom he served in the White House for eight<br>
    Hatch also took credit for just about everything significant Ronald Reagan did<br>expansion over the last number of years. It's been primarily because Reagan got<br><br>
    
    <p><a href="file:///Users/parrt/github/msan501/data/slate/49/ArticleIP_12436.txt">/Users/parrt/github/msan501/data/slate/49/ArticleIP_12436.txt</a><br>
    his two Republican predecessors, Reagan and Bush, they would have been<br>
    The only time Ronald<br>Reagan ever talked about Iran-Contra under oath was in a deposition for the<br><br>
    
    ...
    
</body>
</html>
```      

Notice that the links are URLs just like you see going to website except they refer to a file on the local disk instead of another machine.
 
```
file:///Users/parrt/github/msan501/data/slate/49/ArticleIP_12436.txt
```

(My data is stored in a slightly different spot than yours will be maybe.)

### Creating an index using `dict`

Rather than looking through each file for every search, it's better to create a fast lookup index that maps a word to all of the files that contain that word. It takes about the same time to create the index as it does to do one linear search because both are linearly walking through the list of files. The main program follows this basic structure for this version of the search engine and the one using your own hashtable:

```python
# files and docs are fully-qualified list of filenames
# terms is a list of normalized words
index = create_index(files)
docs = index_search(files, index, terms)
```

Once the index is created, function `index_search()` can crank out search results faster than you can take your fingers off the keyboard.

Here are the two key methods you must implement:
 
```python
def create_index(files):
    """
    Given a list of fully-qualified filenames, build an index from word
    to set of document indexes. The document indexes just the index into the
    files parameter (indexed from 0).
    Make sure that you are mapping a word to a set, not a list.
    For each word w in file i, add i to the set of documents containing w
    """
```

```python
def index_search(files, index, terms):
    """
    Given an index and a list of fully-qualified filenames, return a list of them
    whose file contents has all words in terms as normalized by your words() function.
    Parameter terms is a list of strings.
    You can only use the index to find matching files; you cannot open the files and look inside.
    """
```

These functions will use expressions like `index[w]` where `index` is a `dict` to access the documents containing word `w`. To compute the search results for multiple words, find the intersection of documents in each `index[w]` set. The resulting set will be just the documents that have all words.

### Creating an index using your own hashtable



## Getting started

Please go to [Hashtable starterkit](https://github.com/parrt/msan501-starterkit/tree/master/hashtable) and grab all the python files.  Store these in your repo, such as `~/msan501/hashtable`.

Store the [Slate](https://github.com/parrt/msan501/blob/master/data/slate.7z)and[Berlitz](https://github.com/parrt/msan501/blob/master/data/berlitz1.7z) data sets outside of your repo so that you are not tempted to add that data to the repository. Perhaps you can make a general data directory for use in lots of classes such as `~/data` or just for this class `~/msan501/data`.


## Deliverables

## Submission
