#!/usr/bin/python
import math

# Utils involving primes

# Return the primes smaller than n
def primes(n):
  if n < 2: return
  yield 2
  sievebound = (n-1) / 2
  sieve = [False] * sievebound
  crosslimit = int(n**0.5) / 2
  for i in xrange(1, crosslimit):
    if not sieve[i]:
      for j in xrange(2*i*(i+1), sievebound, 2*i+1):
        sieve[j] = True
  for i in xrange(1, sievebound):
    if not sieve[i]:
      yield 2*i+1

# Returns generator of infinite list of primes
# Can't use the seive without an upper bound
def n_primes():
  yield 2
  prime_list = [2]
  x = 3
  while True:
    check = True
    for j in prime_list:
      if j > x**0.5:
        break
      if x % j == 0:
        check = False
        break

    if check:
      prime_list.append(x)
      yield x
    x += 2

# Find the prime factors of n
def prime_factors(n):
  for p in primes(int(math.sqrt(n))):
    while n % p == 0:
      yield p
      n /= p
      if n == 1: return

# number of divisors for n
def num_divisors(n):
  if n < 1:
    return 1
  accum = 0
  for p in xrange(1, int(math.sqrt(n))):
    if n % p == 0:
      accum += 2
  if int(math.sqrt(n))**2 == n:
    accum += 1
  return accum

# get all divisors of n
def divisors(n):
  divs = []
  if n <= 1:
    return divs
  for p in xrange(1, int(math.sqrt(n))+1):
    if n % p == 0:
      divs.append(p)
      if not p == n / p:
        divs.append(n / p)
  return divs

# get all proper divisors on n
def p_divisors(n):
  tmp = divisors(n)
  if len(tmp) > 1:
    tmp.remove(n)
  return tmp

# Find the greatest common denominator using Euclid's algorithm
def gcd(a, b):
  t = b
  while t != 0:
    a, t = t, a % t
  return a

def lcm(a, b):
  return a * b / gcd(a, b)

if __name__ == "__main__":
  import sys
  primes(int(sys.argv[1]))
