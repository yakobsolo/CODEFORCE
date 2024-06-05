
import re
import functools
import random
import sys
import os
import math
from collections import Counter, defaultdict, deque
from functools import lru_cache, reduce, cmp_to_key
from itertools import accumulate, combinations, permutations
from heapq import nsmallest, nlargest, heappushpop, heapify, heappop, heappush
from io import BytesIO, IOBase
from copy import deepcopy
import threading
from typing import *
from operator import add, xor, mul, ior, iand, itemgetter
import bisect
from string import ascii_lowercase, ascii_uppercase
BUFSIZE = 4096
inf = float('inf')

def I():
    return input()
 
def II():
    return int(input())
 
def MII():
    return map(int, input().split())
 
def LI():
    return list(input().split())
 
def LMII():
    return list(map(int,  input().split()))

 
def GMI():
    return map(lambda x: int(x) - 1, input().split())
 
def LGMI():
    return list(map(lambda x: int(x) - 1, input().split()))
 


# check if a number is prime
def isPrime(x: int) -> bool:
   d = 2
   while d * d <= x:
       if x % d == 0:
           return False
       d += 1
   return True





#  returns prime factorization of a number


def Primefactorization(n: int) -> list[int]:
    factorization = []
       
    d = 2

    while d * d <= n:
        while n % d == 0:
            factorization.append(d)
            n //= d
        d += 1
    if n > 1:
    	  factorization.append(n)
  
    return factorization
 

for j in range(II()):
    n = II()
    a = LMII()

    b = []
    for i in range(1, n):
        b.append(math.gcd(a[i], a[i-1]))
    c = 0
    j = inf
    for i in range(1, n-1):
        if b[i]<b[i-1]:
            c +=1
            j = i
            break
    if j != inf:
        aa = a.copy()
        aaa = a.copy()
        aa.pop(j+1)
        bb = []
        # print(aa, a, j)
        for i in range(1, n-1):
            # print(i)
            bb.append(math.gcd(aa[i], aa[i-1]))

        cc= 0
        for i in range(1, n-2):
# /            print(bb)
            if bb[i]<bb[i-1]:
                cc +=1
                break
        if cc == 0:
            c = 0
        bbb = []
        aaa.pop(j)
        print(aa, aaa, j)
        for i in range(1, n-1):
            # print(i)
            bbb.append(math.gcd(aaa[i], aaa[i-1]))

        ccc= 0
        for i in range(1, n-2):
# /            print(bb)
            if bb[i]<bb[i-1]:
                ccc +=1
                break
        if ccc == 0:
            c = 0
    # print(b)
    if c == 0:
        print("YES")
    else:
        print("NO")
    

    