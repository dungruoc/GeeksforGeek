#!/bin/env python

import sys

def lcs(x, y):
  if len(x) == 0 or len(y) == 0:
    return 0
  if x[-1] == y[-1]:
    return 1 + lcs(x[:-1], y[:-1])
  else:
    l1 = lcs(x[:-1], y)
    l2 = lcs(x, y[:-1])
    if l1 > l2:
      return l1
    else:
      return l2
  return 0

def getkey(x, y):
  return x + '|' + y

def lcs_m(x, y, memory):
  key = getkey(x, y)
  if key in memory:
    return memory[key]
  if len(x) == 0 or len(y) == 0:
    return 0
  else:
    if x[-1] == y[-1]:
      memory[key] = 1 + lcs_m(x[:-1], y[:-1], memory)
    else:
      l1 = lcs_m(x[:-1], y, memory)
      l2 = lcs_m(x, y[:-1], memory)
      if l1 > l2:
        memory[key] = l1
      else:
        memory[key] = l2
  return memory[key]

def lcs_sequence(x, y, memory):
  key = getkey(x, y)
  if key in memory:
    return memory[key]
  if len(x) == 0 or len(y) == 0:
    return ''
  else:
    if x[-1] == y[-1]:
      memory[key] = lcs_sequence(x[:-1], y[:-1], memory) + x[-1]
    else:
      s1 = lcs_sequence(x[:-1], y, memory)
      s2 = lcs_sequence(x, y[:-1], memory)
      if len(s1) > len(s2):
        memory[key] = s1
      else:
        memory[key] = s2
  return memory[key]

def lcs_sequence_all(x, y, memory):
  key = getkey(x, y)
  if key in memory:
    return memory[key]
  if len(x) == 0 or len(y) == 0:
    return ['']
  else:
    if x[-1] == y[-1]:
      memory[key] = []
      for sequence in lcs_sequence_all(x[:-1], y[:-1], memory):
        memory[key].append(sequence + x[-1])
    else:
      s1 = lcs_sequence_all(x[:-1], y, memory)
      s2 = lcs_sequence_all(x, y[:-1], memory)
      if len(s1[0]) > len(s2[0]):
        memory[key] = s1
      elif len(s1[0]) == len(s2[0]):
        memory[key] = s1 + s2
      else:
        memory[key] = s2
  return memory[key]

def lc_string(x, y):
  if len(x) == 0 or len(y) == 0:
    return ''
  prefix = 0
  while prefix < len(x) and prefix < len(y) and x[prefix] == y[prefix]:
    prefix += 1
  sub1 = ''
  if prefix:
    sub1 = x[:prefix]
  sub2 = lc_string(x[1:], y)
  sub3 = lc_string(x, y[1:])
  if len(sub2) > len(sub1):
    sub1 = sub2
  if len(sub3) > len(sub1):
    sub1 = sub3
  return sub1



def main():
  print lcs(sys.argv[1], sys.argv[2])
  memory = {}
  print lcs_m(sys.argv[1], sys.argv[2], memory)
  print memory
  memory = {}
  print lcs_sequence(sys.argv[1], sys.argv[2], memory)
  memory = {}
  print lcs_sequence_all(sys.argv[1], sys.argv[2], memory)
  print lc_string(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
  main()