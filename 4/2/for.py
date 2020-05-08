from math import sqrt, e, tan, log, atan, sin, pi


def func1(y, d, x):
	chis = sqrt(abs(0.25-2*y**3)) + 4.25*d**2
	znam = float((y-x)**2 + 1)
	return chis/znam-e**(abs(4*x-d))*tan(2*x)

def func2(x)
	a = 1.012 # rad
	return 2**x + log(abs(atan(x)-sin(a*x)))+sqrt(x/(a*pi))
