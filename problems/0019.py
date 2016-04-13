#!/usr/bin/python

days_since_sunday = 1 + 365 #they gave 1900, which by leap year rules didn't ahve a leap day
count = 0

start_year = 1901
days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for year in xrange(start_year, 2001):
  for (month, days) in enumerate(days_per_month):
    days_since_sunday = days_since_sunday % 7
    if days_since_sunday == 0:
      count += 1
    days_since_sunday += days
    if month == 1 and year % 4 == 0 and (not year % 100 == 0 or year % 400 == 0):
      days_since_sunday += 1

print count
