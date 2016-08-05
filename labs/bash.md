# UNIX (bash) shell

See ['Bash' your way to victory](../notes/bash-intro.md) first.  Also you might find [A full tutorial](http://tldp.org/LDP/Bash-Beginners-Guide/html/index.html) useful.

UNIX shell is an interactive domain specific language used to control and monitor the UNIX operating system, which includes processes, devices, ram, cpus, disks etc. There are many shells, but `bash` is the one we'll use and it's the most common.  If you have to use a Windows machine, the shell is useless so [install the UNIX shell](http://www.howtogeek.com/249966/how-to-install-and-use-the-linux-bash-shell-on-windows-10/).

Bash is also a programming language, though we'll use it mostly to do scripting: lists of commands. 

You need to get comfortable on the UNIX command line because many companies use Linux on their servers, which in my opinion, is best used from the command line for ultimate control over the server or cluster.  You will control servers at AWS with bash as well. Facility with the show marks you as a more sophisticated programmer.

Moreover, the shell gives very low level and powerful control of the operating system resources, such as the disk.  For example, imagine having to delete all subdirectories within some root directory that contain the string "temp" in their name?  Depending on the size of the root directory, you could sit there for hours manually deleting subdirectories one by one. Here's a one-liner from the shell using the `find` command:

```bash
$ find somedir -type d -name '*temp*' -exec rm -rf {} \;
```

That must look like ancient Aramaic to you at first glance, but once you learn the pattern you can reuse these commands over and over in lots of different situations.  

## Everything is a stream

The first thing you need to know is that UNIX is based upon the idea of a stream. UNIX has excellent conceptual integrity. Everything is a stream, or appears to be. Device drivers look like streams, terminals look like streams, processes communicate via streams, etc... The input and output of a program are streams that you can redirect into a device, a file, or another program.

Each process running on a machine has 3 streams, which you can think of as faucets where you can hook up hoses for input and output:

* standard input (`stdin`)
* standard output (`stdout`)
* standard error (`stderr`)

You can attach streams to those but by default the shell hooks up the keyboard to standard input and hooks the standard output and standard error to the console. All normal output of your program goes to standard output, but standard error is a separate stream where programs typically spit error and debugging output. When you are using PyCharm, the stuff that it puts in red in the console window is standard error.

## Disk structure

[UNIX disk structure](http://www.thegeekstuff.com/2010/09/linux-file-system-structure)

`~parrt` is my home directory; same as `/Users/parrt` on mac or `/home/parrt` on linux; same as `~`.

The `homebrew` program installs stuff in `/usr/local/Cellar`:

```bash 
$ ls /usr/local/Cellar/
ant/          gcc/          gnupg/        libksba/      little-cms2/  openssl/      ruby/
autoconf/     gdbm/         graphviz/     libmpc/       maven/        p7zip/        sqlite/
automake/     gettext/      imagemagick/  libpng/       mono/         pkg-config/   tree/
berkeley-db4/ git/          isl/          libtiff/      mpfr/         python/       valgrind/
cmake/        gmp/          jpeg/         libtool/      node/         python3/      webp/
freetype/     gnu-indent/   libgpg-error/ libyaml/      numpy/        readline/     xz/
```

## Command syntax

Shell commands start with the command name and then optionally a space-separated list of arguments. Every command ends with a newline:

`$` *commandname* *arg1* *arg2* ...  *argN*

If this were a programming language, it would look like

*commandname*(*arg1*, *arg2*, ...,  *argN*)

You can separate multiple commands on the same line with a semicolon:

`$` *cmd1* *arg1* *arg2* ...  *argN* `;` *cmd2* *arg1* *arg2* ...  *argN*

If you want to have a space in an argument, you have to put it in single or double quotes. (As with Python, you have both single and double quotes so that you can use them in strings without escaping them.)

Here's an example command with a single argument that tells the shell to set its current working directory to the root:

```bash
$ cd /
```

You should avoid spaces in filenames because it makes it awkward on the command line to refer to them, since space separates arguments. Example:

```bash
$ ls house\ of\ pancakes
```

But we can use this:

```bash
$ ls 'house of pancakes'
```

When you run a Python program, we are using the `python` command which knows to load the first argument as the script. It also knows to treat the further arguments as arguments to the Python script not the `python` command itself:

`$` python *scriptfilename.py* *arg1* *arg2* ...  *argN*

The shell commands can be built into the shell or they can be programs that we write and invoke.  For example, we use the `which` command to ask which program is being executed when you type a command:

```bash
$ which ls python
/bin/ls
/usr/local/bin/python
```

The Python interpreter is a program installed on our disk and when we say `python` at the shell, it finds the program using an ordered list of directories in `PATH` environment variable and executes it.

```bash
$ echo $PATH
/bin:/usr/local/bin:...
```

Here are the built-in commands you might use: `cd`, `pwd`, `export`, `alias`, `unalias`, `export`, `unset`.

### Scripts

You can put commands into a file just like you can with Python. You can then run the command with `source`:

```bash
$ source myscript.sh
```

Where we typically use `.sh` as the file extension for scripts. You can also tell the operating system that that script file is executable:

```
$ chmod +x myscript.sh
$ ./myscript.sh # if in current directory you need './'
```

### Controlling processes

When you run a command from the shell, the shell waits for the process to terminate and then gives you the `$` prompt back. If the process doesn't terminate, you can kill it with control-C: `^C`.

```bash
$ echo "while True: pass" > /tmp/forever.py
$ python /tmp/forever.py.py  # will never come back
^C
Traceback (most recent call last):
  File "/tmp/forever.py", line 1, in <module>
    while True: pass
KeyboardInterrupt
$ 
```

If you would like the process to run in the *background* and give you the prompt back immediately, put a `&` operator as the last piece of the command:

```bash
$ echo "for i in range(100000000): pass" > /tmp/t.py
$ python /tmp/t.py &
[1] 69021
$ 
```

That 69021 is the process ID (PID). You immediately get the prompt back and can do other work. Some processes take a very long time or run indefinitely, such as Web servers. These processes are always put into the background.

If you wait long enough, that process will finish and, as you execute other commands, you will see this pop-up:

```bash
[1]+  Done                    python /tmp/t.py
```

To get a list of the running processes, you can use process status. I have a whole bunch of shells running because I do so much from the commandline:

```
$ ps
  PID TTY           TIME CMD
29502 ttys000    0:00.28 -bash
58672 ttys001    0:00.24 -bash
36938 ttys002    0:00.12 -bash
97249 ttys003    0:00.22 -bash
58790 ttys004    0:00.14 -bash
63124 ttys005    0:00.14 -bash
67978 ttys006    0:00.09 -bash
 1201 ttys007    0:00.64 -bash
61154 ttys007    0:00.01 vi matlib.py
68321 ttys008    0:00.67 -bash
 1096 ttys010    0:01.16 -bash
25775 ttys012    0:00.25 -bash
27274 ttys013    0:00.20 -bash
29237 ttys014    0:00.14 -bash
27226 ttys015    0:00.01 vi test_descent.py
```

The `vi` command is a text editor and so it is indicating that I'm editing two files somewhere from within my shell windows.

There is also the `top` command which shows you all the processes currently taking resources, not just your own.

The `PID`, or process ID, is useful if you need to kill something that is running without a shell (in a shell, you could just hit `^C`). For example, if I needed to kill the `vi matlib.py` process, I can run `kill`:

```bash
$ kill -KILL 61154
[1]+  Killed: 9               vi matlib.py  (wd: ~/courses-stargate/MSAN501/labs/code)
```

The term `kill` is actually a misnomer. The command really should be called `signal`, because we are sending the `KILL` signal to the process ID.

### Timing processes

You can time how long a program takes to run by putting the built-in `time` command in front of the process you want to time:
 
```bash
$ time ls /
...
real	0m0.006s
user	0m0.002s
sys	0m0.002s
```

We can time Python scripts the same way:

```bash
$ echo "for i in range(100000000): pass" > /tmp/t.py
$ time python /tmp/t.py

real	0m5.725s
user	0m4.406s
sys	0m1.232s
```

### Startup script / profile

From `man bash`:

> When bash is invoked as an interactive login shell, or as a non-interactive shell with the --login option, it first reads and executes commands from the file /etc/profile, if that file exists.  After reading that file, it looks for ~/.bash\_profile, ~/.bash\_login, and ~/.profile, in that order, and reads and executes commands from the first one that exists and is readable.

In summary, you should create a `.bash_profile` file in your home directory, `~`, and put your initialization bash code there. For example, I run Java so much from the command line that I alias `j` to be `java` to save typing. I put this into my `.bash_profile`:

```bash
alias j="java"
```

If you want your prompt to show not just `$`, but also the current directory, you need to run the following command. You can also put it in your `.bash_profile`:

```bash
export PS1="\w $ "
```

## Redirecting stdin/stdout

We pass information around using streams and we can shunt that data into a file or pull data from a file using special operators. You can think of these as operators in a programming language like addition and multiplication. Each program has standard input, standard output, and standard error; three streams.

We can set the standard output of a process using > character:

```bash
$ ls / > /tmp/foo
```

Here is how to type something directly into a text file:
 
```bash
$ cat > /tmp/foo
the first line of the file
the second line of the file
^D
$ 
```

The `^D` means control-D, which means end of file.  `cat` is reading from standard input and writing to the file. The way it knows we are done is when we signal in the file with control-D.

We can set the standard input of a process to the contents of a file and redirect the output of a process to a file.

```bash
$ wc < /tmp/foo
```

or, since `wc` knows about arguments, we can do this:

```bash
$ wc /tmp/foo
```

We can connect to the output of one program to the input of another using pipes: `|`. 

```bash
$ ls / | wc # count files are in the root directory
```

Here is a simple pipe (show first 5 lines of the text we stored in foo):

```bash
$ ls / | head -5 
```

So, some programs take filenames on the command line and some expect standard input. For example, the `tr` translation command expects standard input and writes to standard output

```bash
$ ls / | tr -d e # delete all 'e' char from output
```

## Useful commands

To get documentation on a command C:

```bash
$ man C
```

What computer name am I running on?

```bash
$ hostname
varmint.cs.usfca.edu
```

What username and my running under?
 
```bash
$ whoami
parrt
```

To create a new directory, use:

```bash
$ mkdir /tmp/foo
```
 
To save the current directory, moved to a different directory, and pop back to the old directory:

```bash
$ pushd /tmp
/tmp ~
$ ls
...
$ popd  # back to ~ dir
~
$ 
```

Copy file or directory

```bash
$ cp foo.txt /tmp
$ cp -r ~/msan501/hashtable /tmp # copy recursively
```

To move a file or directory

```bash
$ mv foo.txt /tmp
$ mv ~/msan501/hashtable /tmp # mv entire directory
```

```bash
$ cat file  # dump the file to standard output
$ more file # dump to standard output but paginate
```

To show the first few or last few lines of a file:

```bash
$ head file
$ tail file
```

The most useful incantation of tail prints the last few lines of a file and then waits, printing new lines as they are appended to the file. This is great for watching a log file:

```bash
$ tail -f /var/log/mail.log
```

Often you want to know how many lines, words, and characters are in a file:
 
```bash
$ echo "hi mom" > /tmp/foo.txt
$ wc /tmp/foo.txt
       1       2       7 /tmp/foo.txt
```

## File name expansion

Recall that a filename beginning with `/` is a fully qualified file name, starting with the root of the file hierarchy. Anything other than that starting character means the file is relative to the current working directory.

Dot, `.`, means current directory and `..` means the directory above the current working directory. For example, I might do something like `../data` to get to the sibling `data` directory of the current working directory.

We also use wildcards quite a bit such as:

```bash
$ ls *.txt # show me all files ending in .txt
```

Sometimes we'd like to create a number of similar filenames. For example, here I create three new directories underneath `/tmp`:
 
```bash
$ mkdir /tmp/{old,new,logs}
```

Note that the shell is actually expanding this to a list of arguments:

```bash
$ mkdir /tmp/old /tmp/new /tmp/logs
```

Even `*.txt` expands to the list of files in current directory. If there are `t.txt` and `u.txt`, then `ls *.txt` is actually: `ls t.txt u.txt`. i.e., `ls` and other commands see the expanded list not the the wildcard.

## Python programs

```
$ python code/linux/printargs.py hi mom
```

That Python code:
 
```python
import sys
print "args:", sys.argv[1], sys.argv[2]
```

We can use those arguments as filenames to open or we can read from standard input:
 
```python
import sys
print sys.stdin.readlines()  
```

Print coffee data out

```bash
python code/linux/mycat.py < ../data/coffee
```

## Bash programming

### Hello world

```bash
$ echo "Hello, World!"
```

The `echo` command is just like `print` in Python.

### Environment variables

> When a program is invoked it is given an array of strings called the *environment*. This is a list of name-value pairs, of the form name=value.

Use `env` to dump environment:

```bash
$ env
rvm_bin_path=/Users/parrt/.rvm/bin
TERM_PROGRAM=Apple_Terminal
TERM=xterm-256color
SHELL=/bin/bash
TMPDIR=/var/folders/93/9kzk2ccm8xj8k70059b28jk80000gp/T/
...
```

These are **global variables**. The convention is uppercase letters. Use the following notation to set variables just like in a programming language:

```bash
$ export X="hi"
$ export Y='mom'
```

Without the `export`, the variables become local variables (local to this instance of the shell). For simplicity, let's do everything with global variables.
 
To get the value of a variable, use `$VARNAME`:

```bash
$ echo $X $Y
hi mom
```

Use `unset` to get rid of those:

```bash
$ unset X
$ unset Y
```

The `PATH` environment variable is the most important because it dictates (the list of directories) where the shell looks for commands.

```bash
$ echo $PATH
/opt/local/bin:/opt/local/sbin:/usr/local/Cellar/imagemagick/6.7.1-1/bin:...
```

### Script parameters

Scripts have access to the commandline arguments just like Python does. Use `$`*n* for n=1..n. Here is a simple script that just prints out the first two arguments:

```
echo $1 $2
```

If you put that in `/tmp/t.py`, and run it, here's what you see:

```bash
$ source /tmp/t.py a b
a b
$ bash /tmp/t.py a b
a b
```

### Loops

Bash has loops that are super useful for processing files.  Imagine that we have the following data files:

```bash
$ cd github/msan501/data/berlitz1
$ ls
HandRHawaii.txt		HistoryItaly.txt	IntroLasVegas.txt	WhatToMalaysia.txt
HandRHongKong.txt	HistoryJamaica.txt	IntroLosAngeles.txt	WhatToMallorca.txt
HandRIbiza.txt		HistoryJapan.txt	IntroMadeira.txt	WhereToDublin.txt
HandRIsrael.txt		HistoryJerusalem.txt	IntroMadrid.txt		WhereToEdinburgh.txt
HandRIstanbul.txt	HistoryLakeDistrict.txt	IntroMalaysia.txt	WhereToEgypt.txt
HandRJamaica.txt	HistoryLasVegas.txt	IntroMallorca.txt	WhereToFWI.txt
...
```

We can use a loop to process each file. In this case I'm just printing the name:
 
```bash
for f in *.txt
do
    echo $f
done
```

or all on one line:

```bash
$ for f in *.txt; do echo $f; done
HandRHawaii.txt
HandRHongKong.txt
HandRIbiza.txt
HandRIsrael.txt
HandRIstanbul.txt
HandRJamaica.txt
...
```

As another example, I have a directory with all of your projects in it. If I want to run a test script on all of your files, I can do the following.

```bash
$ cd grading
$ for f in *-regression; do python mytest $f; done
```

### Command substitution

Sometimes it's very useful to run a command whose output you'd like to use in another command. The syntax is either `$(command)` or \``command`\`. 

For example, we can `ls` those berlitz1 files and write the output to a file:

```bash
$ ls *.txt > /tmp/files
```

These will be on the line by itself because the `ls` command noticed it was not spewing data to the console. The most likely scenario is we want to process files and so it puts them all on a line by themselves.

Now we need to execute a `cat /tmp/files` command to get those filenames back. If we enclose it for command substitution, we can use it in a for loop:

```bash
$ for f in $(cat /tmp/files); do echo $f; done
```

Loops are particularly useful when argument lists are huge and the shell gives you an error from filename expansion.


### Playing with filenames

The `basename` command is super useful as it strips out the file name from a path and can also give you the file name without the extension:

```bash
$ basename /Users/parrt/github/msan501/data/berlitz1/WhereToFrance.txt 
WhereToFrance.txt
$ basename -s .txt WhereToFrance.txt
WhereToFrance
```

When you combine this with a loop, it's very easy to rename files. First, let's test with an echo rather than doing the rename right away. Here's how we print just the filenames without the file suffix:

```bash
$ for f in *.txt; do echo $(basename -s .txt $f); done
```

And here is printing the `mv` command to rename the files, but not executing it:

```bash
$ for f in *.txt; do echo mv $f $(basename -s .txt $f) ; done
```

Finally, we can remove the echo and do the command for real, which gives shows that we have successfully stripped the `.txt` from the filenames:

```bash
$ for f in *.txt; do mv $f $(basename -s .txt $f) ; done
$ ls
HandRHawaii		HistoryItaly		IntroLasVegas		WhatToMalaysia
HandRHongKong		HistoryJamaica		IntroLosAngeles		WhatToMallorca
HandRIbiza		HistoryJapan		IntroMadeira		WhereToDublin
...
```

### Processing files

It was brought up that my Berlitz data files had non-ASCII characters in them: `“”‘’`. I tested the deletion of these from a file with a couple of commands:

```bash
$ echo "bad: “”‘’" > /tmp/foo
$ tr -d "“”‘’" < /tmp/foo
bad: 
```

for f in *.txt; do tr -d "“”‘’" < $f > /tmp/foo; mv /tmp/foo $f; done

