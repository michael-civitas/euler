#!/usr/bin/python

import itertools

#from python docs on itertools recipes
def nth(iterable, n, default=None):
  "Returns the nth item or a default value"
  return next(itertools.islice(iterable, n, None), default)
