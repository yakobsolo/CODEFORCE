#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def recursive(number):
        
        if number>=0 and number<=9:
            return number
        sums = 0
        while number > 0:
            sums += number%10
            number = number//10
        return recursive(sums)
    
def superDigit(n, k):
    # Write your code here
    
    number = 0
    
    for c in n:
        number += int(c)
    number = number*k
    return recursive(number)

    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
