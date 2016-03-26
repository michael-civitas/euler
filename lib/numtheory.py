#!/usr/bin/python
import math

# Utils involving primes

# Return the first n primes
def primes(n):
  if n < 2: return
  yield 2
  prime_list = [2]
  for i in xrange(3, n, 2):
    check = True
    for j in prime_list:
      if j > n**0.5:
        break
      if i % j == 0:
        check = False
        break

    if check:
      prime_list.append(i)
      yield i

def prime_factors(n):
  for p in primes(int(math.sqrt(n))):
    while n % p == 0:
      yield p
      n /= p
      if n == 1: return

if __name__ == "__main__":
  import sys
  primes(int(sys.argv[1]))
