#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        lld = number % 10
    else:
        lld = number % -10
        lld *= -1

   print("{:d}".format(lld), end='')
   return (lld)
