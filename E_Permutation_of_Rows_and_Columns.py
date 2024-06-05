
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
    n, m = MII()
    a , b = set(), set()
    mta, mtb = [], []
    flg = False

    for _ in range(n):
        row = LMII()
        
        rw = tuple(sorted(row))
        mta.append(row)
        a.add(rw)
    for _ in range(n):
        row = LMII()      
        rw = tuple(sorted(row))
        b.add(rw)
        mtb.append(row)
    e, j = set(), set()
    for c in range(m):
        rwa, rwb = [],[]
        for r in range(n):
            rwa.append(mta[r][c])
            rwb.append(mtb[r][c])
        e.add(tuple(sorted(rwa)))
        j.add(tuple(sorted(rwb)))
    
    for v in a:
        if v not in b:
            flg = True
            break
    for v in e:
        if v not in j:
            flg = True
            break
    
       
    if flg:
        print("NO")
    else:
        print("YES")
