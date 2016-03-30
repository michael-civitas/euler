#!/usr/bin/python
from numtheory import n_primes
from iterrecipes import nth

print nth(n_primes(), 10001 - 1)
