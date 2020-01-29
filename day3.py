# -*- coding: utf-8 -*-
"""day3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Zq92Y3H_i4w5WgOa3qjAF7MCatldZVEt
"""

#Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.

#not_string('candy') → 'not candy'
#not_string('x') → 'not x'
#not_string('not bad') → 'not bad'

def not_string(str):
  if len(str)>=3 and str[:3] =="not":
    return str
  return "not " + str

# Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).
#missing_char('kitten', 1) → 'ktten'
#missing_char('kitten', 0) → 'itten'
#missing_char('kitten', 4) → 'kittn'

def missing_char(str, n):
  front = str[:n]
  back = str[n+1:]
  return front + back

#Given a string, return a new string where the first and last chars have been exchanged.

#front_back('code') → 'eodc'
#front_back('a') → 'a'
#front_back('ab') → 'ba'

def front_back(str):
  if len(str) <= 1:
    return str
    
  mid = str[1:len(str)-1]  # can be written as str[1:-1]
  
  # last + mid + first
  return str[len(str)-1] + mid + str[0]