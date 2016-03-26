#!/usr/bin/python

#Euler defines with 1 and 2 as seed.
def fib(n):
  result = []
  a, b = 1, 2
  while b < n:
    result.append(b)
    a, b = b, a + b
  return result

def fib_gen(n):
  a, b, counter = 1, 2, 0
  while True:
    if (counter > n): return
    yield b
    a, b = b, a + b
    counter += 1

if __name__ == "__main__":
  import sys
  fib(int(sys.argv[1]))
