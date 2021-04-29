#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'sortedSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#
from typing import List
import bisect

def sortedSum(a):
    # Write your code here
    res = a[0]

    def sortTheNext(segment: List[int], next: int) -> List[int]:
        nonlocal res
        curr = 0
        bisect.insort(segment, next)
        for i in range(len(segment)):
            curr += segment[i] * (i+1)
        res += curr
    
    segment = []
    for i in range(0, len(a)):
        sortTheNext(segment, a[i])
    return int(res % (1e9+7))

