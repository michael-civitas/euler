#!/usr/bin/python
from numtheory import num_divisors

def gen_triangle_numbers():
  accum = 1
  counter = 2
  while True:
    yield accum
    accum += counter
    counter += 1

for x in gen_triangle_numbers():
  if num_divisors(x) > 500:
    print x
    break
