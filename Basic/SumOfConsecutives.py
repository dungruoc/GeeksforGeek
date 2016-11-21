# -*- coding: utf-8 -*-
"""
Given a number n, the task is to check whether it can be expressed as a sum of
 two or more consecutive numbers or not.

Examples:

Input  : n = 10 
Output : 1
It can be expressed as sum of two consecutive
numbers 1 + 2 + 3 + 4.

Input  : n = 16  
Output : 0
It cannot be expressed as sum of two consecutive
numbers.

Input  : n = 5  
Output : 1
2 + 3 = 5
 

Input:

The first line contains 'T' denoting the number of test cases.
Then follows description of test cases.
Each test case contains a single positive integer n.

Output:
Print "1" if number can be expressed as sum of consecutives else "0". (Without the double quotes)

Constraints:
1<=T<=200
0<=N<=10^18

Example:
Input :
2
4
5

Output :
0
1

Solution:
https://en.wikipedia.org/wiki/Polite_number
These are polite numbers. As stated, impolite numbers are exactly powers of 2.

Proof:
1 - Any odd number is a polite number: 2k + 1 = k + (k+1)
2 - Any even number that is the product of 2 and an odd number is polite:
    2 * (2k + 1) = (k-1) + k + (k+1) + (k+2)
3 - And by induction, we can see that any number that is product of 2 and a polite
    number is a polite number:
    N = i + ... + (i + k - 1)
    - if k is even: N is then odd, so 2*N is polite as in (2)
    - if k is odd: there is a median in the above sum, namely S:
      N = (S - (k-1)/2) + ... (S - 1) + S + (S+1) + ... (S + (k-1)/2)
      2*N = (2S - k+1)+ ... (2S-2) + 2S + (2S + 2) + ... (2S + k-1)
      We can then rebalance the left an right of 2S
       - taking 1 from 2S + 2 to 2S - 2 -> 2S - 1 ... 2S + 1
       - taking 2 from 2S + 4 to 2S - 4 -> 2S - 2 .... 2S + 2
       ...
       - taking (k-1)/2 from (2S + k-1) to (2S - k+1)
      So:
      2N = (2S - (k-1)/2) + ... + 2S + ... + 2S + (k-1)/2
      that is polite too
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
