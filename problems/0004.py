#!/usr/bin/python

def is_palindrome(n):
  return str(n) == str(n)[::-1]

def p4_palin_gen():
  for i in xrange(999, 100, -1):
    for j in xrange(i, 100, -1):
      if is_palindrome(i * j):
        yield (i * j, i, j)

print max([x for x, y, z in p4_palin_gen()])
