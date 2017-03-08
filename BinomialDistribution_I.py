__author__ = 'Imtiaz'

'''
problem statement: https://www.hackerrank.com/challenges/s10-binomial-distribution-1
solution: Brute Force
Python Version: 3.5
'''

# binomial_distribution_formula = n!/(x! * (n-x)!) * p^x * q^(n-x)
# where   n = number of trials
#         x = number of successes
#         q = failure ratio
#         p = success ratio

# Solution:
#     . Boys and Girls ratio will be given input
#     . So, if ratio is given 1.09:1 then
#         probability of boy (success ratio) = (1.09)/ (1.09+1)
#         probability of girl (success ratio) = (1)/ (1.09+1)
#     . Then, according to the cummulative formula generate result


def fact(y):
    if y <= 1:
        return 1
    return y*(fact(y-1))


ratio = [float(x) for x in input().split()]

n = 6

p = float(ratio[0]/(sum(ratio)))
q = float(ratio[1]/(sum(ratio)))

probability = 0

for x in range(3,7):
    probability = probability + (float(fact(n) * p**x * q ** (n-x))/float(fact(x)*fact(n-x)))

print("%.3f" % probability)


