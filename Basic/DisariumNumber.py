# -*- coding: utf-8 -*-
"""
Given a number “n”, find if it is Disarium or not. A number is called Disarium if sum of its digits powered with their respective positions is equal to the number itself.

Input:
The first line of input contains a single integer T denoting the number of test cases. Then T test cases follow. Each test case consist of one line. The first line of each test case consists of an integer N.

Output:
Corresponding to each test case, in a new line, print 1 if N is Disarium , else 0.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 1000

Example:
Input:
2
89
80

Output
1
0

Explanation
1. For first test case as 8^1+9^2 = 89 thus output is 1
2. For sec test case 8^1 + 0^2 = 8 thus output is 0
"""

def list_digit(N):
    aList = []
    while N > 0:
        aList.append(N % 10)
        N /= 10
    aList.reverse()
    return aList

T = int(raw_input())
for test in xrange(T):
    N = int(raw_input())
    aSum = 0
    for i, num in enumerate(list_digit(N)):
        aPow = i+1
        aSum += num ** aPow
    if aSum == N:
        print(1)
    else:
        print(0)
