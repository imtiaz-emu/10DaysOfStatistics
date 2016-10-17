__author__ = 'Imtiaz'

'''
problem statement: https://www.hackerrank.com/challenges/s10-interquartile-range
solution: Brute Force, Numpy
Python Version: 3.5
'''

import numpy as np
from math import ceil, floor

N = int(input())
numbers = [int(x) for x in input().split()]
frequency = [int(x) for x in input().split()]
quartiles = [0] * 3

total_numbers = []

for index in range(N):
    total_numbers += ([numbers[index]] * frequency[index])

total_numbers.sort()

# Approach: Brute Force
def approach_bf():
    first_half = total_numbers[:len(total_numbers) // 2]
    second_half = total_numbers[len(total_numbers) // 2:]

    if (len(total_numbers) % 2 == 1):
        second_half = second_half[1:len(second_half)]

    if (len(first_half) % 2 == 1):
        quartiles[0] = first_half[floor(len(first_half) / 2)]
        quartiles[2] = second_half[floor(len(second_half) / 2)]
    else:
        quartiles[0] = (first_half[ceil(len(first_half) / 2)] + first_half[floor(len(first_half) / 2) - 1]) / 2
        quartiles[2] = (second_half[ceil(len(second_half) / 2)] + second_half[floor(len(second_half) / 2) - 1]) / 2

    print(round((float(quartiles[2]) - float(quartiles[0])), 1))


# Approach: NumPy (Median)
def approach_numPy():
    quartiles = [0] * 3
    first_half = total_numbers[:len(total_numbers) // 2]
    second_half = total_numbers[len(total_numbers) // 2:]

    quartiles[1] = np.median(np.array(total_numbers))
    quartiles[0] = np.median(np.array(first_half))
    if (N % 2 == 1):
        second_half = second_half[1:len(second_half)]
    quartiles[2] = np.median(np.array(second_half))

    print(round((float(quartiles[2]) - float(quartiles[0])), 1))


approach_numPy()
