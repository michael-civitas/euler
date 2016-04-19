#!/usr/bin/python
from numtheory import p_divisors

nums_to_check = set(range(1, 10001))
result = 0
for i in xrange(1, 10000):
  if i in nums_to_check:
    tmp = sum(p_divisors(i))
    if not tmp == i:
      if sum(p_divisors(tmp)) == i:
        result += i + tmp
        nums_to_check.remove(i)
        nums_to_check.remove(tmp)

print result
