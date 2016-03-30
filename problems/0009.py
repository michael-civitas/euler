#!/usr/bin/python

def euclid_form_sum(x, y):
  return (x**2 - y**2) + (2 * x * y) + (x**2 + y**2)

def euclid_form_product(x, y):
  return (x**2 - y**2) * (2 * x * y) * (x**2 + y**2)

def do_loop():
  # first triple is (3, 4, 5), so m = 2 and n = 1
  m = 2
# lazy, not calculating bounds
  while (True):
    n = 1
    while (n < m):
      triple_sum = euclid_form_sum(m, n)
      if 1000 % triple_sum == 0:
        k = 1000 / triple_sum
        return euclid_form_product(m, n) * k**3
      else:
        n += 1

    m += 1

print do_loop()
