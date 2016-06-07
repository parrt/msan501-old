import sys
from PIL import Image
if len(sys.argv) != 2:
	print "$ python view.py imagefilename"
	sys.exit(1)
filename = sys.argv[1] # get the argument passed to us by operating system
img = Image.open(filename) # load file specified on the command line
img = img.convert("L") # grayscale
img.show()
