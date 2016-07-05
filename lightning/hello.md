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
3. When all else fails, download [hello.py](https://raw.githubusercontent.com/parrt/msan501/master/lightning/hello.py) from github.

Once you get the file written to the disk, you should be able to jump to that directory using the commandline shell. Use `ls` to get a directory listing:

```bash
$ cd /Users/YOURID/msan501/inclass
$ ls
hello.py
```

Now, we're going to run that program/script:

```bash
$ python hello.py
$ 
```

We do not get any output. This is a critical difference. The interactive Python shell immediately prints expression values because it is interactive. When you run a file from the commandline, it assumes you wanted to execute like a script in batch mode. That is why we do not get any output.

Now edit that file and change it to

```python
print 500+1
```

Save the file and rerun it. Now you should see:

```bash
$ python hello.py 
501
$ 
```

## PyCharm

Now, we're going to do the exact same thing except using the development environment PyCharm.

1. Launch PyCharm and then under `File` menu, tell it to open a directory with `Open...` menu item. 
2. Navigate to your `/Users/YOURID/msan501/inclass` directory and click okay. You should see your `hello.py` in the `Project` pane of the development environment. 
3. Double-click on it to open it in the editor pane.
4. Right click in the editor window and select `Run hello` item. Another pane will open on the bottom of the IDE that looks something like:

```
/usr/local/bin/python /tmp/inclass/hello.py
501
Process finished with exit code 0
```

Finally, let's create a Python file from within the development environment. 

1. Choose `File:New...` and select item `Python File` in the submenu. It will pop up a dialog box.
2. Enter filename `hi.py`, which will then bring up an empty editor window.
3. Type `print "hi"` followed by newline in the editor window.
4. Right-click and select `Run hi` and, once again, you should see output in the bottom console.

**You should be able to test out small programs or Python snippets very very quickly. Rehearse these procedures until they are second nature.**