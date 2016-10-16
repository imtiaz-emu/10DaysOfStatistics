__author__ = 'Imtiaz'

'''
problem statement: https://www.hackerrank.com/challenges/s10-basic-statistics
solution: Brute Force, NumPy, SciPy
Python Version: 3.5
'''

import numpy as np
from scipy import stats
from math import ceil, floor
import time


N = int(input())
numbers = [int(x) for x in input().split()]
numbers.sort()


# Approach: SciPy
def approach_SciPy():
    np_array = np.array(numbers)
    print(round(np_array.mean(), 1))
    if (int(N) % 2 == 1):
        print(round(numbers[floor(N / 2)], 1))
    else:
        print(round((numbers[ceil(N / 2)] + numbers[floor(N / 2) - 1]) / 2, 1))
    print(int(stats.mode(np_array)[0]))


# Approach: Brute Force
def approach_bf():
    results = [0] * 3
    grouping = [0] * 100002
    max_count = 0
    sum = 0

    for number in numbers:
        sum += number
        grouping[number] += 1
        if (max_count < grouping[number]):
            max_count = grouping[number]
            results[2] = number

    results[0] = round(sum / N, 1)
    if (int(N) % 2 == 1):
        results[1] = round(numbers[floor(N / 2)], 1)
    else:
        results[1] = round((numbers[ceil(N / 2)] + numbers[floor(N / 2) - 1]) / 2, 1)

    print(results[0])
    print(results[1])
    print(results[2])


approach_SciPy()