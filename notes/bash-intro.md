# 'Bash' your way to victory

## Goals

* Launch a bash shell
* Set the working directory
* List the files in that directory
* Launch Python from the shell
* Print command-line arguments to a Python program

## Description

UNIX shell (`bash` in our case) is an interactive domain specific language used to control and monitor the UNIX operating system, which includes processes, devices, ram, cpus, disks etc. It is also a programming language, though we’ll use it mostly to do scripting: lists of commands. If you have to use a Windows machine, the shell is useless so try to install a UNIX shell.

You need to get comfortable on the UNIX command line because many companies use Linux on their servers, which in my opinion, is best used from the command line for ultimate control over the server or cluster.

When you first start up the `Terminal.app` or launcher shell using whatever Linux app you have, you will see either a simple dollar prompt or something more complicated that displays the current directory or current machine etc:

```bash
$ 
```

The shell is just an interactive interpreter like we have with Python:

```python
>>> print "hello"
hello
>>>
```

To do the same thing in bash:

```bash
$ echo "hello"
hello
$
```

The shell has a number of state variable, one of which is the *current working directory*. Most commands that we execute will be relative to this working directory. You can print that out with command:

```bash
$ pwd
/Users/parrt/github/msan501/notes
$ 
```

After you execute command, you get the prompt back, as you can see.

Any *path* starting with `/` means it is an absolute path starting at the root of the disk directory hierarchy. So anything else is considered relative to the current working directory. For example, if your current working directory is `/Users/parrt/github/msan501` then `ls notes` will give you a directory listing of the `notes` directory underneath `/Users/parrt/github/msan501`.

One of the most common things to do is to change the current working directory with `cd`:

```bash
$ cd /tmp
$ pwd
/tmp
$ 
```

You can ask for a list of the files in that directory:

```bash
$ ls
KSOutOfProcessFetcher.502.ppfIhqX0vjaTSb8AJYobDV7Cu68=/
com.apple.launchd.2G280iawAe/
com.apple.launchd.8lgH3lM2YX/
com.apple.launchd.GVI2txnx6l/
...
```

There are lots of programs on the disk and you can launch them simply by using their name as the first element on a command line. For example, here's how we start Python:

```bash
$ python
Python 2.7.12 |Anaconda 4.2.0 (x86_64)| (default, Jul  2 2016, 17:43:17) 
[GCC 4.2.1 (Based on Apple Inc. build 5658) (LLVM build 2336.11.00)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
Anaconda is brought to you by Continuum Analytics.
Please check out: http://continuum.io/thanks and https://anaconda.org
>>> 
```

That of course gives us a new prompt, `>>>`, which is for Python. We can exit Python by hitting control-D (which means "end of file"). As we exit Python it will take us back to the shell.

Anything that follows the name of the command are considered arguments to that command. For example, here is how to get the directory listing for a specific directory even if you're not currently in that directory:

```bash
$ ls /bin
[*          csh*        echo*       ksh*        mkdir*      rcp*        stty*       wait4path*
bash*       date*       ed*         launchctl*  mv*         rm*         sync*       zsh*
cat*        dd*         expr*       link*       pax*        rmdir*      tcsh*
chmod*      df*         hostname*   ln*         ps*         sh*         test*
cp*         domainname* kill*       ls*         pwd*        sleep*      unlink*
```

The notation is generally:

*command arg1 arg2 arg3*

That is analogous to the following in Python:

*command(arg1, arg2, arg3)*
 
As another example, here is how we execute a specific Python script rather than entering interactive Python mode:

```bash
$ python myscript.py
... any output from the script ...
```

Naturally, we often want to pass arguments to the Python script itself, which simply follow the script argument to the Python command. For example, here is a simple script that we can put into `args.py`:

```python
import sysprint "args:", sys.argv[1]
```

We can run that script like this:
 
```bash
$ python args.py hi mom
args: ['args.py', 'hi', 'mom']
$ 
```