
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
    time, minute = input().split()
    
    time = list(time)

    ans = 0
    minute = int(minute)
    hour = 0
    if minute>=60:
        hour = minute//60
        minute = minute%60
        

    # print(hour, minute)

    def isPalindrome(time):

        if time[0]== time[-1] and time[1] == time[-2]: return True
        return False
    
    visted = set()
    while "".join(time) not in visted:
        visted.add("".join(time))
        if isPalindrome(time): ans+=1


        rem = (int("".join(time[3:])) + minute)%60
        h = (int("".join(time[3:])) +minute)//60
        if rem<10:
            rem = f"0{rem}" 
        else:
            rem = str(rem)        
        
        cur= (int("".join(time[:2]))+hour+ h)%24

        
        if cur<10:
            cur = list(f"0{cur}")
        else:
            cur = list(str(cur))

        
    
        
        time[:2] = cur
        time[3:]  = list(str(rem))
        # print(set(time))

        
    


        
    print(ans)