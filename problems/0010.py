#!/usr/bin/python
from numtheory import primes

print sum([x for x in primes(2000000)])
