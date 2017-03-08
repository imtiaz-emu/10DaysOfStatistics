__author__ = 'Imtiaz'

'''
problem statement: https://www.hackerrank.com/challenges/s10-binomial-distribution-2
solution: Brute Force
Python Version: 3.5
'''

# binomial_distribution_formula = n!/(x! * (n-x)!) * p^x * q^(n-x)
# where   n = number of trials
#         x = number of successes
#         q = failure ratio
#         p = success ratio

# Solution:
#     . 12% of the pistons are rejected
#     . So, the ratio is given 0.88:0.12 then
#         probability of reject (success ratio) = 0.12
#         probability of accept (failure ratio) = 0.88
#     . Then, according to the cummulative formula generate result


def fact(y):
    if y <= 1:
        return 1
    return y*(fact(y-1))

n = 10

p = 0.12
q = 0.88

probability = 0

# No more than 2 rejects
for x in range(0,3):
    probability = probability + (float(fact(n) * p**x * q ** (n-x))/float(fact(x)*fact(n-x)))

print("%.3f" % probability)


# At least 2 rejects
probability = 0
for x in range(2,11):
    probability = probability + (float(fact(n) * p**x * q ** (n-x))/float(fact(x)*fact(n-x)))

print("%.3f" % probability)


