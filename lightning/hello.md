# Say Hello

##  Interactive Python

Launch `Terminal.app` (Mac) or whatever the `bash` *terminal* or *commandline prompt* program is (UNIX). From the prompt, type `python` followed by return/newline:

```bash
$ python
Python 2.7.11 (default, Jun  7 2016, 10:09:37) 
...
```

If the version is 2.7.10, then you are probably using the older preinstalled version of Python. That's okay for now, but keep that in mind that you will probably want to do the `brew install python` installation from [setup](https://github.com/parrt/msan501/blob/master/notes/setup.md) at some point.

Now, from the Python prompt `>>>` (we are no longer in `bash`), type `500+1` followed by newline. You should see something like this:

```python
>>> 500+1
501
>>> 
```

Python has evaluated the expression and printed the result back to the screen. It is as if we had done this, which gives us the same result:

```python
>>> print 500+1
501
>>> 
```

The Python interactive shell prints all expression values immediately.
 
## Scripting Python

Go to a suitable directory on your disk, or create one, such as `/Users/YOURID/msan501/inclass`. Now create a **text file** called `hello.py` that contains exactly one line:

```python
500+1
```

This is exactly what you typed in first in the interactive Python shell. Save the file in the `inclass` directory.

Here are solutions to  the most common errors:

1. Do not put `.txt` at the end of the file name
2. Do NOT use M$ Word or any other word processor; You think it's text but it's not. There are lots of text editors out there including Mac's `TextEdit.app`. Just make sure save as plain text not "rich text". There are also plenty of text editor such as [Sublime](https://www.sublimetext.com/) and [TextMate](https://macromates.com/).  (If you are really hard-core, you will learn `vi` or `emacs`, which you will see me use in class.)
3. When all else fails, download [hello.py]() from github.

Once you get the file written to the disk, you should be able to jump to that directory using the commandline shell. Use `ls` to get a directory listing:

```bash
$ cd /Users/YOURID/msan501/inclass
$ ls
hello.py
```

Now, we're going to run that program/script:

```bash
$ python hello.py

```

## PyCharm