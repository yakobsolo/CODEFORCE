
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
    N = II()
    arr = LMII()

    def checker(k):

        bits = [0]*21
        for i in range(k):
            for j in range(arr[i].bit_length()):
                if arr[i]>>j &1 == 1:bits[j]+=1
        counter = bits.copy()
        # print(bits, "bit")
        for i in range(k, N):
            # print(i, k)
            for j in range(arr[i].bit_length()):
                if arr[i]>>j &1 == 1:counter[j]+=1
            
            for j in range(arr[i-k].bit_length()):
                if arr[i-k]>>j &1 == 1:counter[j]-=1

            # print(counter, arr[i])
            for m in range(21):
                if counter[m] ==0 and bits[m]>0: return False

                if counter[m] !=0 and bits[m]==0: return False
            
        return True






    l, r = 1, N

    while l<=r:
        mid = l + (r-l)//2
        # print(arr, mid)

        if checker(mid):
            r  = mid-1
            res = mid
        else:
            l = mid+1

    print(res)