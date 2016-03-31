#!/usr/bin/python

CACHE_SIZE = 10000000

def collatz_eval (i, j) :
  cache = [0]*CACHE_SIZE
  v, max_n = 1, 1
  for i in range(i, j + 1):
    num = i
    count = 1
    while num > 1:
      if num % 2 == 1:
        num = num + (num / 2) + 1
        count += 1
      else:
        num = num / 2
      if num <= CACHE_SIZE and cache[num - 1] != 0:
        count += (cache[num - 1])
        break
      count += 1

    cache[i - 1] = count
    if count > v:
      v, max_n = count, i
  return max_n

print collatz_eval(1, 1000000)
