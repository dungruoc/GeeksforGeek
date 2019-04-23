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
  if x == y:
    return [x + '|' + y]
  return [x + '|' + y, y + '|' + x]

def lcs_m(x, y, memory):
  keys = getkey(x, y)
  for key in keys:
    if key in memory:
      return memory[key]
  if len(x) == 0 or len(y) == 0:
    return 0
  else:
    if x[-1] == y[-1]:
      lcs = 1 + lcs_m(x[:-1], y[:-1], memory)
      for key in keys:
        memory[key] = lcs
    else:
      l1 = lcs_m(x[:-1], y, memory)
      l2 = lcs_m(x, y[:-1], memory)
      if l1 > l2:
        for key in keys:
          memory[key] = l1
      else:
        for key in keys:
          memory[key] = l2
  return memory[keys[0]]

def lcs_sequence(x, y, memory):
  keys = getkey(x, y)
  for key in keys:
    if key in memory:
      # print 'memory'
      return memory[key]
  if len(x) == 0 or len(y) == 0:
    return ''
  else:
    if x[-1] == y[-1]:
      lcs = lcs_sequence(x[:-1], y[:-1], memory) + x[-1]
      for key in keys:
        memory[key] = lcs
    else:
      s1 = lcs_sequence(x[:-1], y, memory)
      s2 = lcs_sequence(x, y[:-1], memory)
      if len(s1) > len(s2):
        for key in keys:
          memory[key] = s1
      else:
        for key in keys:
          memory[key] = s2
  return memory[keys[0]]

def lcs_sequence_all(x, y, memory):
  keys = getkey(x, y)
  for key in keys:
    if key in memory:
      return memory[key]
  if len(x) == 0 or len(y) == 0:
    return (0, {''})
  else:
    if x[-1] == y[-1]:
      aSet = set([])
      for key in keys:
        memory[key] = {}
      aLen, all_lcs = lcs_sequence_all(x[:-1], y[:-1], memory)
      for sequence in all_lcs:
        aSet.add(sequence + x[-1])
      for key in keys:
        memory[key] = (aLen + 1, aSet)
    else:
      aLen1, s1 = lcs_sequence_all(x[:-1], y, memory)
      aLen2, s2 = lcs_sequence_all(x, y[:-1], memory)
      if aLen1 > aLen2:
        for key in keys:
          memory[key] = (aLen1, s1)
      elif aLen1 == aLen2:
        for key in keys:
          memory[key] = (aLen1, s1.union(s2))
      else:
        for key in keys:
          memory[key] = (aLen2, s2)
  return memory[keys[0]]



def main():
  # print lcs(sys.argv[1], sys.argv[2])
  memory = {}
  print lcs_m(sys.argv[1], sys.argv[2], memory)
  # print memory
  memory = {}
  print lcs_sequence(sys.argv[1], sys.argv[2], memory)
  # print memory
  memory = {}
  print lcs_sequence_all(sys.argv[1], sys.argv[2], memory)
  print memory

if __name__ == '__main__':
  main()