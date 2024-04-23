
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
    n, k = MII()

    arr = LMII()
    arr.sort()
    count = Counter(arr)
    l, r = 0, 0
    ans = []
    i = 0
    while i<n:
        if count[arr[i]]>=k:
            ll = arr[i]
            prev = ll-1
            while  i<n and count[arr[i]] >= k:
                if arr[i] == prev+1:
                    prev+=1
                    rr=arr[i]
                    i+=count[arr[i]]
                else:
                    i-=count[arr[i-1]]
                    break
                    
            if i<n:
                i+=count[arr[i]]
            if rr-ll >= r-l:
                r, l = rr, ll

        else:

            i+=count[arr[i]]
    if r ==0:
        print(-1)
    else:
        print(l, r)



