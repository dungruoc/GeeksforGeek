# -*- coding: utf-8 -*-
"""
Given a matrix of m*n size, the task is to count all the rows in a matrix that
are sorted either in strictly increasing order or in strictly decreasing order?

Examples:

Input : m = 4,  n = 5
        mat[m][n] = 1 2 3 4 5
                    4 3 1 2 6
                    8 7 6 5 4
                    5 7 8 9 10
Output: 3 
 
Input:
The first line of input contains a single integer T denoting the number of test
 cases. Then T test cases follow. Each test case consists of two lines.
First line of each test case consist of two space separated integers M and N,
denoting the number of element in a row and column respectively.
Second line of each test case consists of N*M space separated integers
denoting the elements in the matrix in row major order.

Output:

Corresponding to each test case, print in a new line, count of sorted rows.

Constraints:
1<=T<=200
1<=N,M<=100

Example:

Input:
2
3 3
3 40 38 44 52 54 57 60 69
3 2
18 40 27 38 55 67
 

Output:
2
3
"""

T = int(raw_input())
for test in xrange(T):
    m, n = tuple([int(num) for num in raw_input().split()])
    matrix = [int(num) for num in raw_input().split()]
    nSorted = 0
    for row in xrange(m):
        is_sorted = False
        if n <= 1:
            is_sorted = True
        else:
            order = matrix[row*n + 1] - matrix[row*n]
            if order > 0:
                order = 1
            elif order < 0:
                order = -1
            else:
                order = 0
            if order != 0:
                is_sorted = True
                for col in xrange(2,n):
                    newOrd = matrix[row*n + col] - matrix[row*n + col - 1]
                    if order * newOrd <= 0:
                        is_sorted = False
                        break
        if is_sorted:
            nSorted += 1
    print(nSorted)
            
