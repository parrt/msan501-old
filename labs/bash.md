# UNIX (bash) shell

UNIX shell is an interactive domain specific language used to control and monitor the UNIX operating system, which includes processes, devices, ram, cpus, disks etc. There are many shells, but `bash` is the one we'll use and it's the most common.  If you have to use a Windows machine, the shell is useless so [install the UNIX shell](http://www.howtogeek.com/249966/how-to-install-and-use-the-linux-bash-shell-on-windows-10/).

Bash is also a programming language, though we'll use it mostly to do scripting: lists of commands. 

You need to get comfortable on the UNIX command line because many companies use Linux on their servers, which in my opinion, is best used from the command line for ultimate control over the server or cluster.  You will control servers at AWS with bash as well. Facility with the show marks you as a more sophisticated programmer.

Moreover, the shell gives very low level and powerful control of the operating system resources, such as the disk.  For example, imagine having to delete all subdirectories within some root directory that contain the string "temp" in their name?  Depending on the size of the root directory, you could sit there for hours manually deleting subdirectories one by one. Here's a one-liner from the shell using the `find` command:

```bash
$ find somedir -type d -name '*temp*' -exec rm -rf {} \;
```

or with a loop:

```bash
for f in $(find .); do echo $f; done
```

That must look like ancient Aramaic to you at first glance, but once you learn the pattern you can reuse these commands over and over in lots of different situations.

## Everything is a stream

The first thing you need to know is that UNIX is based upon the idea of a stream. UNIX has excellent conceptual integrity. Everything is a stream, or appears to be. Device drivers look like streams, terminals look like streams, processes communicate via streams, etc... The input and output of a program are streams that you can redirect into a device, a file, or another program.

Each process running on a machine has 3 streams:

* standard input
* standard output
* standard error

You can attach streams to those but by default they 

Here is an example device, the null device, that lets you throw output away. For example, you might want to run a program but ignore the output.

```bash
$ ls > /dev/null # ignore output of ls
```

where `# ignore output of ls` is a comment.

Most of the commands covered in this lecture process stdin and send results to stdout. In this manner, you can incrementally process a data stream by hooking the output of one tool to the input of another via a pipe. For example, the following piped sequence prints the number of files in the current directory modified in August.

```bash
$ ls -l | grep Aug | wc -l
```

Imagine how long it would take you to write the equivalent Python or Java program. You can become an extremely productive UNIX programmer if you learn to combine the simple command-line tools.

## The basics

### Disk structure

[UNIX disk structure](http://www.thegeekstuff.com/2010/09/linux-file-system-structure)

`~parrt` is my home directory, `/home/parrt`, as is `~`.

```bash
ls /
```

### Executing commands

Like when were typing in the Python shell, each command is terminated by newline. The first thing we type is the command followed by parameters (separated by whitespace):

```bash
$ foo arg1 arg2 ... argN
```

That is why whitespace in filenames sucks:

```bash
$ ls house\ of\ pancakes
```

But we can use this:

```bash
$ ls 'house of pancakes'
```

The commands can be built into the shell or they can be programs that we write and invoke.  For example, here's how you ask which program is being executed when you type a command:

```bash
which ls python
```

The Python interpreter is a program installed on our disk and when we say `python} at the shell, it finds the program using an ordered list of directories in `PATH} environment variable and executes it.

```bash
$ echo $PATH
/Library/Java/JavaVirtualMachines/jdk1.7.0_51.jdk/Contents/Home/bin:/usr/local/bin:...
```

### Redirecting stdin/stdout

We pass information around using streams and we can shunt that data into a file or pull data from a file using special operators. You can pretend these are like operators in a programming language like addition and multiplication. Each program has standard input, standard output, and standard error; three streams. 

We can set the standard input of a process using > character:

```bash
ls / > /tmp/foo
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
wc < /tmp/foo
```

or

```bash
wc /tmp/foo
```

We can connect to the output of one program to the input of another using pipes: `|}. 

```bash
ls / | wc # count files are in the root directory
```

Here is a simple pipe (show first 5 lines of the text we stored in foo):

```bash
cat /tmp/foo | head -5 
```

So, some programs take filenames on the command line and some expect standard input. For example, the `tr` translation command expects standard input and writes to standard output

```bash
ls / | tr -d e # delete all 'e' char from output
```

## Misc}

* man, help, apropos
* ls, cd, pushd, popd, cd -
* cp, scp
* cat, more
* head, tail
* wc

The most useful incantation of tail prints the last few lines of a file and then waits, printing new lines as they are appended to the file. This is great for watching a log file:

```bash
$ tail -f /var/log/mail.log
```

## Searching streams

One of the most useful tools available on UNIX and the one you may use the most is grep. This tool matches regular expressions (which includes simple words) and prints matching lines to stdout.

The simplest incantation looks for a particular character sequence in a set of files. Here is an example that looks for any reference to System in the java files in the current directory.

```bash
$ grep System *.java
```

You may find the dot `.` regular expression useful. It matches any single character but is typically combined with the star, which matches zero or more of the preceding item. Be careful to enclose the expression in single quotes so the command-line expansion doesn't modify the argument. The following example, looks for references to any a forum page in a server log file:

```bash
$ grep '/forum/.*' /home/public/cs601/unix/access.log
```

or equivalently:

```bash
$ cat /home/public/cs601/unix/access.log | grep '/forum/.*' 
```

The second form is useful when you want to process a collection of files as a single stream as in:

```bash
$ cat /home/public/cs601/unix/access*.log | grep '/forum/.*'
```

If you need to look for a string at the beginning of a line, use caret `^`:

```bash
$ grep '^195.77.105.200' /home/public/cs601/unix/access*.log
```

This finds all lines in all access logs that begin with IP address 195.77.105.200.

If you would like to invert the pattern matching to find lines that do not match a pattern, use -v. Here is an example that finds references to non image GETs in a log file:

```bash
$ cat /home/public/cs601/unix/access.log | grep -v '/images'
```

Now imagine that you have an http log file and you would like to filter out page requests made by nonhuman spiders. If you have a file called spider.IPs, you can find all nonspider page views via:

```bash
$ cat /home/public/cs601/unix/access.log | grep -v -f /tmp/spider.IPs
```

Finally, to ignore the case of the input stream, use -i.

## Basics of file processing

**cut, paste**

```bash
cat ../data/coffee
```

cut grabs one or more fields according to a delimiter like strip in Python. It's also like SQL `select f1, f2 from file}.

```bash
cut -d ' ' -f 1 ../data/coffee > /tmp/1
cut -d ' ' -f 2 ../data/coffee > /tmp/2
```

```bash
cat /tmp/1
```

```bash
cat /tmp/2
```

paste combines files as if they were columns:

```bash
paste /tmp/1 /tmp/2
```

```bash
paste -d ', ' /tmp/1 /tmp/2
```

Get first and third column from names file

```bash
$ cut -d ' ' -f 1,3 names
```

`join` is like an INNER JOIN in SQL. (`zip()` in python) first column must be sorted.


```bash
$ cat ../data/phones
linux command line 131
132 exercises in computational analytics
parrt 5707
tombu 5001
jcoker 5099
$ cat ../data/salary
parrt 50
tombu  51
jcoker 99
$ join ../data/phones ../data/salary
parrt 5707 50
tombu 5001 51
jcoker 5099 99
```

Here is how I email around all the coupons for Amazon Web services without having to do it manually:

```bash
$ paste students aws-coupons
jim@usfca.edu	X
kay@usfca.edu	Y
sriram@usfca.edu	Z
...
```

and here is a little Python script to process those lines:

```python
import os
import sys
for line in sys.stdin.readlines():
    p = line.split('\t')
    p = (p[0].strip(), p[1].strip())
    print "echo '' | mail -s 'AWS coupon "+p[1]+"' "+p[0]
    os.system("echo '' | mail -s 'AWS coupon "+p[1]+"' "+p[0])
```

and here's how you run it:
 
```bash
$ paste students aws-coupons | python email_coupons.py 
```

## Processing log files

```bash
$ cut -d ' ' -f 1 access.log | sort | uniq -c | sort -r -n|head
```

Get unique list of IPs.

Find out who is hitting your site by getting histogram.

How many hits to the images directory? 

How many total hits to the website? 

Histogram of URLs.


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
