__author__ = 'Imtiaz'

'''
problem statement: https://www.hackerrank.com/challenges/s10-poisson-distribution-1
solution: Brute Force
Python Version: 3.5
'''

# geometric_distribution_formula = (l^k * e^(-l))/k!
# where   l = is the average number of successes that occur in a specified region.
#         k = is the actual number of successes that occur in a specified region.
#         e = 2.71828

def fact(y):
    if y <= 1:
        return 1
    return y*(fact(y-1))

e = 2.71828
l = float(input())
k = float(input())

probability = (l**(k) * e**(-l))/fact(k)

print("%.3f" % probability)


