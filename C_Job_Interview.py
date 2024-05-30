
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
    p = LMII()
    t = LMII()

    tc,pc = 0, 0
    can = []
    skpc = 0
    sktc = 0
    skillp, skillc = [], []
    for i in range(n+m+1):
        if p[i]>t[i]:
            pc+=1
            skpc+=p[i]
            skillp.append(t[i])

            can.append("p")
        else:
            tc+=1
            sktc+=t[i]
            skillc.append(p[i])
            can.append("t")
    skillc.sort()
    skillp.sort()

    ans = []
    for j in range(n+m+1):
        temp = 0
        if can[i] == "t":
            

    
    


    

