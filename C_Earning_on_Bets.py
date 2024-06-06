
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
 
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

# Function to compute LCM of an array of numbers
def lcm_of_array(arr):
    return functools.reduce(lcm, arr)


for _ in range(II()):
    n= II()
    arr = LMII()
    fac = lcm_of_array(arr)
    a = []
    for i in range(n):
        a.append(math.ceil(fac/arr[i]))
    sm = sum(a)
    # print(a, sm)
    flg = True 
    for i in range(n):
        if a[i] * arr[i] <= sm:
            flg = False
            break
    if flg:
        print(*a)
    else:
        print("-1")
