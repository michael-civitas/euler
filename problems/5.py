#!/usr/bin/python
from numtheory import lcm

def list_lcm(num_list):
  x = num_list[0]
  for num in num_list[1:]:
    x = lcm(x, num)
  return x

print list_lcm(range(1, 21))
