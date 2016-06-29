# Software/Lab set up

## github account

Please create a https://github.com/join?source=hero-personal user account as you will need this during your time in MSAN, likely day 1 in computational bootcamp MSAN501. 

USE your USF email address when you sign up!  Please choose a github all-lower-case user id that is presentable to prospective employers later. I.e., hotstud4you or idrinktoomuch are *bad* ideas. It would also help if have something about your name in there but it’s not required.  For example, my id is parrt. 

You should be able to get unlimited private repos as a student.  Make sure to request the student pack 

https://education.github.com/pack

for the free stuff. It can take them a while to verify your student-ness via your email address. 

##  Amazon Web services

Create an account at [amazon web services](http://aws.amazon.com) where you’ll spool up some beefy computers to kick the crap out of data.

## Development environments

Your next pre-bootcamp homework is to make sure that your (if you like pleasant install experiences) Mac laptop is ready to get its code on. 

### R

For exploratory data analysis and any other courses that use R, you will want to install RStudio

https://www.rstudio.com/products/rstudio/download/

### Python

For Python, you will be using not only the commandline python interpreter but also the PyCharm development environment, which you can download here

https://www.jetbrains.com/pycharm/download/

The Mac comes with a very old version of Python and you need the latest, which you can do easily with

$ brew install python

from the commandline. (The $ means you’re sitting at the commandline prompt of Terminal.app) if it says “what the hell is brew”, then go here and follow the instructions:

http://brew.sh/

This homebrew thingie will become your friend from now on as we will use it to install all sorts of things. It installs the latest up-to-date version of Python when you ask it to, which means you have two of them installed but don’t worry about that now. 

Next, you will need to get matplotlib and numpy installed. Do this from the commandline after installing the latest Python with brew:

$ pip install numpy

Then, to install matplotlib:

$ brew install pkg-config
$ pip install matplotlib

If that fails, then you will enjoy googling the error messages.

### First project

If you’re bored and not enjoying your last few days of freedom before a frenzied 12 months of MSAN, than I suggest you start on the first project for the competition boot camp.

https://github.com/parrt/msan501/blob/master/projects/images.pdf