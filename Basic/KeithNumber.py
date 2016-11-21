# -*- coding: utf-8 -*-
"""
A n digit number x is called Keith number if it appears in a special sequence
(defined below) generated using its digits. The special sequence has first n
terms as digits of x and other terms are recursively evaluated as sum of
previous n terms.The task is to find if a given number is Keith Number or not.

Examples

Input : x = 197
Output : 1
197 has 3 digits, so n = 3
The number is Keith because it appears in the special
sequence that has first three terms as 1, 9, 7 and 
remaining terms evaluated using sum of previous 3 terms.
1, 9, 7, 17, 33, 57, 107, 197, .....

Input : x = 12
Output : 0
The number is not Keith because it doesn't appear in
the special sequence generated using its digits.
1, 2, 3, 5, 8, 13, 21, .....

Input : x = 14
Output : 1
14 is a Keith number since it appears in the sequence,
1, 4, 5, 9, 14, ...
"""

#code

def digits(N):
    aList = []
    while N > 0:
        aList.append(N % 10)
        N /= 10
    aList.reverse()
    return aList

def keith(N):
    aDigits = digits(N)
    aLen = len(aDigits)
    if aLen == 1:
        return 1
    aFirst = True
    while N > aDigits[-1]:
        aSum = 0
        if aFirst:
            aFirst = False
            for i in xrange(1,aLen+1):
                aSum += aDigits[-i]
        else:
            aSum = 2*aDigits[-1] - aDigits[-aLen-1]    
        if aSum > N:
            return 0
        elif aSum == N:
            return 1
        else:
            aDigits.append(aSum)
    return 0

T = int(raw_input())
for test in xrange(T):
    N = int(raw_input())
    print(keith(N))
