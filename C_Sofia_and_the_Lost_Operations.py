
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
    return map(str, input().split())
 
def LI():
    return list(input().split())
 
def LMII():
    return list(map(str,  input().split()))

 
# def GMI():
#     return map(lambda x: int(x) - 1, input().split())
 
# def LGMI():
#     return list(map(lambda x: int(x) - 1, input().split()))
 


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
    N = II()
    a = LMII()
    b = LMII()
    m = II()
    d = LMII()

    count = defaultdict(int)
    for v in d:
        count[v]+=1
    end = False
    notFound = False
    for i in range(N):
        if b[i] == d[-1]:
            end = True
        if a[i] != b[i]:
            if b[i] in count:
                count[b[i]] -=1
                if count[b[i]] == 0:
                    del count[b[i]]
            else:
                notFound = True
                break
    if notFound:
        print("NO")
    else:
        if end:
            print("YES")
        else:
            print("NO")
        