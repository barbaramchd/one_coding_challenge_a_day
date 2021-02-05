#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count = 0
    ar.sort() #putting my list in ascenting order
    ar.append('#')
    i = 0
    while i < n:
        if ar[i]==ar[i+1]: #checking x with the next x
            count += 1 # count one more bc we started at 0
            i += 2 #as it is a pair, we need to count 2
        else:
            i += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
