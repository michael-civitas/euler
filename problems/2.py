#!/usr/bin/python
import fibo

x = reduce(lambda x, y: x + y, [x for x in fibo.fib(4000000) if x % 2 == 0])
print x
