import matplotlib.pyplot as plt
import numpy as np

income = [5800, 6200, 6400, 6500, 6550, 6580, 8200, 8600, 8800, 9200, 9630, 10570, 11330,
          11600, 11800, 11830, 12650, 13000, 13224, 13766, 14010, 14468, 15000, 15200,
          15600, 16000, 16200]
riders = [192000, 190400, 191200, 177600, 176800, 178400, 180800, 175200, 174400, 173920,
          172800, 163200, 161600, 161600, 160800, 159200, 148800, 115696, 147200, 150400,
          152000, 136000, 126240, 123888, 126080, 151680, 152800]

plt.plot(income, riders, "ro")
plt.xlabel("Monthly income in dollars", fontsize=16)
plt.ylabel("Weekly public transit riders", fontsize=16, rotation='vertical')

#plt.savefig('income-riders.png', format="png")

# Plot degree 1 polynomial (a line) through the data
fit = np.polyfit(income, riders, deg=1)
m, b = fit[0], fit[1]
print "m = %5.2f, b = %8.1f" % (m, b) # gives "m = -5.44, b = 220217.6"

def line(m, b, x):
    return m * x + b

LEFT = round(min(income))
RIGHT = round(max(income))
linex = np.arange(LEFT, RIGHT, 0.1)
liney = [line(m, b, x) for x in linex]
#plt.plot(linex, liney, '--')

# Plot degree 3 polynomial through the data
fit = np.polyfit(income, riders, deg=3)
print fit # [  1.67688238e-07  -5.44026370e-03   5.02283115e+01   4.24152675e+04]
a = fit[0]
b = fit[1]
c = fit[2]
d = fit[3]

def quad(a, b, c, x):
    return a*x**2 + b*x + c

def cubic(a, b, c, d, x):
    return a*x**3 + b*x**2 + c*x + d

curvex = np.arange(LEFT, RIGHT, 0.1)
curvey = [cubic(a,b,c,d, x) for x in curvex]
plt.plot(curvex, curvey, '--')

plt.title("Fit $y = %2.3f x + %2.3f$"%(m,b), fontsize=16)
plt.savefig('income-riders-fit-cubic.png', format="png")

plt.show()
