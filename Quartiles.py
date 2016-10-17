__author__ = 'Imtiaz'

'''
problem statement: https://www.hackerrank.com/challenges/s10-quartiles
solution: Brute Force, Numpy
Python Version: 3.5
'''

import numpy as np
from math import ceil, floor

N = int(input())
numbers = [int(x) for x in input().split()]
numbers.sort()


# Approach: Brute Force
def approach_bf():
    quartiles = [0] * 3
    first_half = numbers[:len(numbers) // 2]
    second_half = numbers[len(numbers) // 2:]

    if(N%2 == 1):
        quartiles[1] = second_half[0]
        second_half = second_half[1:len(second_half)]
    else:
        quartiles[1] = (second_half[0] + first_half[len(first_half)-1])//2

    if (len(first_half) % 2 == 1):
        quartiles[0] = first_half[floor(len(first_half) / 2)]
        quartiles[2] = second_half[floor(len(second_half) / 2)]
    else:
        quartiles[0] = (first_half[ceil(len(first_half) / 2)] + first_half[floor(len(first_half) / 2) - 1]) // 2
        quartiles[2] = (second_half[ceil(len(second_half) / 2)] + second_half[floor(len(second_half) / 2) - 1]) // 2


    result_print(quartiles)


# Approach: NumPy (Median)
def approach_numPy():
    quartiles = [0] * 3
    first_half = numbers[:len(numbers) // 2]
    second_half = numbers[len(numbers) // 2:]

    quartiles[1] = np.median(np.array(numbers))
    quartiles[0] = np.median(np.array(first_half))
    if (N % 2 == 1):
        second_half = second_half[1:len(second_half)]
    quartiles[2] = np.median(np.array(second_half))

    result_print(quartiles)

def result_print(qtr):
    print(int(qtr[0]))
    print(int(qtr[1]))
    print(int(qtr[2]))

approach_numPy()