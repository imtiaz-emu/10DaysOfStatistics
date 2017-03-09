__author__ = 'Imtiaz'

'''
problem statement: https://www.hackerrank.com/challenges/s10-geometric-distribution-2
solution: Brute Force
Python Version: 3.5
'''

# geometric_distribution_formula = q^(n-1) * p
# where   n = number of trials
#         q = failure ratio
#         p = success ratio


n = 5

p = 1/3
q = 2/3

probability = 0
for x in range(1, 6):
    probability = probability + q**(x-1) * p

print("%.3f" % probability)


