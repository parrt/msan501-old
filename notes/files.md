# Reading and writing files

## Goals

* Learn differences between files and memory
* Open/close files
* Read / write text files

## Description

### What are files?

Files save information so we don't lose it when the computer gets turned off. RAM memory disappears without power. Disk files "persist" we say.

File data is less convenient to access than directly accessing memory but it is not limited by the size of memory. It is limited by the size of the disk, which is much larger.

Reading from a file is kind of like reading from the keyboard, except that we have to interactively type information when using `raw_input()`. and of course we have to retype input every time.

As we discussed early in the semester, files are just bits. It's how we interpret it that is meaningful. The bits could represent an image, a movie, some text, Python program text, whatever.

Text files are usually 1 byte (8 bits) per character and have the notion of a line. A line is just a sequence of characters terminated with either `\r\n` (Windows) or `\n` (UNIX, Mac). A text file is usually then a sequence of lines.

A binary file is, well, anything else. It still could represent an image or a song but we know at least it's not text.

### File descriptors

Unlike accessing memory directly, we must explicitly tell Python to open a file and then close it later when were done. We must distinguish between reading and writing a file and that dictates how we open the file. We have to:

* open for read
* open for write
* open for append

*Opening a file for write, destroys the previous contents.*

Close flushes any data in memory buffers that needs to be written and informs the operating system that you no longer need that resource. The operating system can only open so many files at once so you should close files when you're done using them. From the Python documentation:

> "It is a common bug to write a program where you have the code to add all the data you want to a file, but the program does not end up creating a file. Usually this means you forgot to close the file."

**Avoid confusion**:

1. The filename is a string that identifies a file on the disk. It can be fully qualified or relative to the current working directory.

2. When we open a file, Python gives us a "file object" that is really just a handle or cookie that the operating system gives us. It's a unique identifier and how the operating system likes to identify a file that we work with. The file object is not the filename and is also not the file itself on the disk. It's really just a descriptor and a reference to the file.

3. The contents of the file is different than the filename and the file object that Python gives us.  

For example, your house contents is different than the address and different than a piece of paper with the address written on it.

So, we will use a filename to get a file object and the file object to get the file contents or to write the file contents.

### Relative paths

Just as with the `bash` shell, Python programs have the notion of a "current working directory". You can ignore this if you use absolute paths (those starting with `/`). But, such programs aren't really very portable.  Relative paths are much better but we need to give filenames relative to the working directory.

```
$ python
Python 2.7.8 (default, Aug 28 2014, 11:37:48)
[GCC 4.2.1 Compatible Apple LLVM 5.1 (clang-503.0.40)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import os
>>> print os.getcwd()
/Users/parrt/courses/MSAN501/notes
>>>
```

When using PyCharm, you have to go into "Edit configurations" in the Run menu and then fill in the "working directory" so that it knows where to start execution.

### Opening/closing files

Here is how to open and immediately close a file:

```
f = open('/tmp/foo.txt', 'w')
f.close()
```

The second argument indicates whether we are going to read `"r"`, write `"w"`, or append `"a"`.

The file `/tmp/foo.txt` is created if it doesn't already exist because of the `"w"`.

You cannot do anything after the file is closed

```
f = open('/tmp/foo.txt', 'w')
f.close()
f.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file
```

### Reading from a text file

Now lets use the `"r"` file open mode.

Assume `/tmp/names.txt` has:

```
3 parrt
2 jcoker
8 tombu
```

**PATTERN**: load all file contents into string

```
f = open('/tmp/names.txt', 'r')
contents = f.read() # read all content of the file
f.close()
print contents
```

Reading the entire contents is often not as useful as reading the input line by line. Because it is a text file, we know there are \n characters there:

```
$ od -c /tmp/names.txt
0000000 3 p a r r t \n 2 j c o k e r
0000020 \n 8 t o m b u \n
0000031
```

**Q.** `open("/tmp/names.txt")` is the same as `open("/tmp/names.txt", "r")`. How does that work?

Here is how we could read in the three lines of the file:

```
f = open('/tmp/names.txt')
first = f.readline()
second = f.readline()
third = f.readline()
f.close()
print first, second, third
```

That prints the same thing as we had before except now we have access to the individual lines. Also note that `readline()` strips off the newline but we get it back because of the normal newline given by print.

Here's how to split the entire contents into lines with a single read:

```
f = open('/tmp/names.txt')
contents = f.read() # read all content of the file
f.close()
lines = contents.strip().split("\n")
```

The `strip()` is important because it drops the last newline, which would otherwise give us an empty string as the last element. It's easier to do this:

**PATTERN**: get all lines in a file into memory

```
f = open('/tmp/names.txt')
lines = f.readlines()
f.close()
print lines # note that this keeps the \n on the end of lines
```

That works well except that it requires we load everything into memory, which is pretty inefficient and limits the size of the data we can process.

**PATTERN**: To read data in line by line easily, we can use the `for` loop:

```
f = open('/tmp/names.txt')
for line in f: # for each line in the file
 print line,
f.close()
```

Once we have a line of text, we can treat them like we did when we had raw input from the user.

```
f = open('/tmp/names.txt')
for line in f: # for each line in the file
    print line.strip().split(" ")
f.close()
```

### Writing to a text file

To write a text file, we open with `"w"` mode, do some `write()`s, and make sure to close. If you use `"r"` instead of `"w"` and then `write()`, you will get this error:

```
IOError: File not open for writing
```

Sample code:

```
f = open('/tmp/foo.txt', 'w')
f.write("This is easy\n") # we need \n in there
f.write("Ok, not too bad\n")
f.close()
```

When you execute that code you get what you would expect into `/tmp/foo.txt`:

```
$ cat /tmp/foo.txt
This is easy
Ok, not too bad
```

**PATTERN**: Write a floating-point number to a file in text representation (not binary):

```
f = open('/tmp/foo.txt', 'w')
f.write("32.921323\n")
f.close()
```

```
$ cat /tmp/foo.txt
32.921323
```

**PATTERN**: Write a list of words to a file, one per line:

```
words = "Dogs have masters Cats have staff".split(" ")
f = open('/tmp/foo.txt', 'w')
for w in words:
    f.write(w)
    f.write("\n")
f.close()
```

```
$ cat /tmp/foo.txt
Dogs
have
masters
Cats
have
staff
$
```