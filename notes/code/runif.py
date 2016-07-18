a = 16807
m = pow(2,31)-1
x = 666 # this is our x_n that changes each runif01() call

def runif01(): # U(0,1)
    global x
    x = a * x % m
    return x / float(m)

def setseed(s): # updates the seed global variable
    global x
    x = s

def runif(a,b):
    rv = runif01()
    return a + (b-a)*rv
