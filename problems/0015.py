#!/usr/bin/python

from math import factorial

# There are 40 edges we have to take
# Since 20 must be right and 20 must be down this is 40C20
# Just like coin flips in sequence

x = factorial(40) / (factorial(20) * factorial(20))
print x
