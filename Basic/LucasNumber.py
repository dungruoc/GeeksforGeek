# -*- coding: utf-8 -*-
"""
A Lucas Number is a number which is represented by the following recurrence
Ln = Ln-1 + Ln-2 for n>1
L0 = 2
L1 = 1

Now given a number n your task is to find the nth lucas number.

Note: Since the output could be very long take mod 1000000007

Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each line contains an integer n.

Output:
For each test case in a new line print the nth lucas no.

Constraints:
1<=T<=100
1<=N<=100

Example:
Input:
2
9
3
Output:
76
4
"""

#code

def lucas_number(N, modulo):
    table = []
    for i in xrange(N+1):
        if i == 0:
            table.append(2)
        elif i == 1:
            table.append(1)
        else:
            table.append((table[i-1] + table[i-2]) % modulo)
    return table[N]
    

T = int(raw_input())
for test in xrange(T):
    N = int(raw_input())
    print(lucas_number(N, 1000000007))