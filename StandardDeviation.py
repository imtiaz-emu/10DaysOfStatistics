__author__ = 'Imtiaz'

'''
problem statement: https://www.hackerrank.com/challenges/s10-standard-deviation
solution: Brute Force
Python Version: 3.5
'''

from math import sqrt

N = int(input())
numbers = [int(x) for x in input().split()]

mean = sum(numbers) / N

result = (sum([(number - mean) ** 2 for number in numbers]))/N

print(round(sqrt(result), 1))

