#!/usr/bin/python
first_hundred_count = 0
digits = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

for digit in digits:
  first_hundred_count += len(digit)

for num in teens:
  first_hundred_count += len(num)

# Meh, stupid iteration. Can optimize by storing digit length and multiplying tens length by 10
for num in tens:
  for digit in digits:
    first_hundred_count += len(num) + len(digit)

count = first_hundred_count * 10

for hundred in digits[1:]:
  count += (len(hundred) + len('hundred')) * 100
  count += len('and') * 99

count += len('one') + len('thousand')

print count
