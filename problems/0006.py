#!/usr/bin/python

def sum_of_squares(num_list):
  result = 0
  for x in num_list:
    result += x**2
  return result

def square_of_sum(num_list):
  return sum(num_list)**2


problem_list = range(1, 101)
print square_of_sum(problem_list) - sum_of_squares(problem_list)
