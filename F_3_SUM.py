
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
 

for _ in range(II()):
    n = II()
    arr = LMII()
    lastdigit = []
    for val in arr:
        lastdigit.append(val%10)
    count = Counter(lastdigit)
    flg = False
    for i in range(10):
        if count[i] != 0:
            for j in range(10):
                if count[j]!= 0:
                
                    for k in range(10):
                        if count[k] != 0:
                            if i == j ==k and count[i]<3:continue
                            if (i == j and count[i]<2) or  (i == k and count[i]<2) : continue
                            if j == k and count[j]<2: continue

                            if (i+j+k)%10 == 3:
                                flg = True
                                break
                if flg: break
            if flg: break
    if flg: print("YES")
    else:print("NO")
