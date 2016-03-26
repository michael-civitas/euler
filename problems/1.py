#!/usr/bin/python

x = reduce(lambda x, y: x+y, [x for x in xrange(1000) if x % 3 == 0 or x % 5 == 0])
print x
