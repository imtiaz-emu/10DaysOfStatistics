__author__ = 'Imtiaz'

'''
problem statement: https://www.hackerrank.com/challenges/s10-weighted-mean
solution: Brute Force
Python Version: 3.5
'''

import timeit

N = int(input())
numbers = [int(x) for x in input().split()]
weights = [int(x) for x in input().split()]

# Approach: Brute Force
def approach_bf():
    weights_sum = 0
    mean_sum = 0
    for indx in range(len(numbers)):
        mean_sum += (numbers[indx] * weights[indx])
        weights_sum += weights[indx]

    print(round((mean_sum/weights_sum), 1))

# start = timeit.default_timer()
#
# approach_bf()
#
# stop = timeit.default_timer()
#
# print(stop - start)


# Approach: Brute Force - Zip (Half time faster O(n/2))
def approach_bf_zip():
    weights_sum = 0
    mean_sum = 0
    for num, wei in zip(numbers, weights):
        mean_sum += (num * wei)
        weights_sum += wei

    print(round((mean_sum/weights_sum), 1))

# start = timeit.default_timer()

approach_bf_zip()

# stop = timeit.default_timer()

# print(stop - start)
