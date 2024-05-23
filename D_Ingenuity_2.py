
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
    direction = list(I())
    count = Counter(direction)

    NS = abs(count["N"]-count["S"])
    EW = abs(count["E"]-count["W"])
    if NS %2 == 0 and EW %2 == 0:
        
        if N==2:
            if ("N" in count and "S" in count) or("W" in count and "E" in count):
                print("NO")
                continue
        ans = []
        if N == 4 and NS == 0 and EW == 0:
            ans = ["R"]*4
            if "N" in direction:
                nind = direction.index("N")
                sind = direction.index("S")
                if count["N"] ==2:
                    
                    for i in range(4):

                        if direction[i] == "S" and i != sind:
                            ans[i] = "H"
                        elif direction[i] == "N" and i!= nind:
                            ans[i] = "H"
                else:
                    for i in range(4):
                        if direction[i] == "E" or direction[i] == 'W':
                            ans[i] = "H"
                print("".join(ans))
                continue
            else:
                wind = direction.index("W")
                eind = direction.index("E")
                
                if count["W"] == 2:
                    for i in range(4):
                        if direction[i] == "E" and i != eind:
                            ans[i] = "H"
                        elif direction[i] == "W" and i!= wind:
                            ans[i] = "H"
                else:
                    for i in range(4):
                        if direction[i] == "N" or direction[i] == 'S':
                            ans[i] = "H"
                print("".join(ans))
                continue
            


        

        
        
        hash = defaultdict(int)
        for v in direction:
            hash[v] +=1
            if hash[v] <=count[v]//2:
                ans.append("R")
            else:
                ans.append("H")
        

        print("".join(ans))



    else:
        print("NO")