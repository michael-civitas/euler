#!/usr/bin/python
from numtheory import n_primes
from itertools import islice

#from python docs on itertools recipes
def nth(iterable, n, default=None):
  "Returns the nth item or a default value"
  return next(islice(iterable, n, None), default)

print nth(n_primes(), 10001 - 1)
