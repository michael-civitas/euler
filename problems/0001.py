#!/usr/bin/python

x = sum([x for x in xrange(1000) if x % 3 == 0 or x % 5 == 0])
print x
