# -*- coding: utf-8 -*-
"""day02.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aM_WtdNN0dQ4TeFXbhtSiqKzHc_WImnO
"""

# Given two int values, return their sum. Unless the two values are the same, then return double their sum.
# sum_double(1, 2) → 3
# sum_double(3, 2) → 5
# sum_double(2, 2) → 8

def sum_double(a, b):
  if a != b:
    return a+b
  else:
    return 2*(a+b)

#We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.
#parrot_trouble(True, 6) → True
#parrot_trouble(True, 7) → False
#parrot_trouble(False, 6) → False

def parrot_trouble(talking, hour):
  if talking == True and hour <7 or talking == True and hour>20:
    return True
  else:
    return False

# Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.

# makes10(9, 10) → True
# makes10(9, 9) → False
# makes10(1, 9) → True

def makes10(a, b):
  if a+b == 10 or a == 10 or b == 10:
    return True
  else:
    return False

#Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.

#pos_neg(1, -1, False) → True
#pos_neg(-1, 1, False) → True
#pos_neg(-4, -5, True) → True

def pos_neg(a, b, negative):
  if negative:
    return (a<0 and b<0)
  else:
    return ((a>0 and b<0) or (a<0 and b>0))