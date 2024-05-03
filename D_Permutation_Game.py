
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
    n, k , pb, ps = MII()

    p = LMII()
    a = LMII()

    pathb =  []
    paths = []

    visted = set()
    i = 0

    
    while i<k and i<n:
        if pb-1 not in visted:
            pathb.append(pb-1)
            visted.add(pb-1)
            pb = p[pb-1]
        else:
            break
        i+=1
    visted  = set()
    i = 0
    while i<k and i<n:
        if ps-1 not in visted:
            paths.append(ps-1)
            visted.add(ps-1)
            ps = p[ps-1]
        else:
            break
        i+=1
    
    comb =[]
    coms = []
    sumb, sums  = [],[]

    for i in range(len(pathb)):
        if comb:
            comb.append(comb[-1]+a[pathb[i]])
        else:
            comb.append(a[pathb[i]])
    for i in range(len(paths)):
        if coms:
            coms.append(coms[-1]+a[paths[i]])
        else:
            coms.append(a[paths[i]])
    
    
    for i in range(len(pathb)):
        sumb.append(comb[i]+a[pathb[i]]*(k-i-1))
    for i in range(len(paths)):
        sums.append(coms[i]+a[paths[i]]*(k-i-1))
    mxb, mxs = max(sumb), max(sums)
    if mxb == mxs:
        print("Draw")
    elif mxb >mxs:
        print("Bodya")
    else:
        print("Sasha")
        



