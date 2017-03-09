__author__ = 'Imtiaz'

'''
problem statement: https://www.hackerrank.com/challenges/s10-poisson-distribution-2
solution: Brute Force
Python Version: 3.5
'''

# geometric_distribution_formula = (l^k * e^(-l))/k!
# if random poisson distribution variable is given, then E[X^2] = l + l^2
# where   l = is the average number of successes that occur in a specified region.
#         k = is the actual number of successes that occur in a specified region.
#         e = 2.71828

def fact(y):
    if y <= 1:
        return 1
    return y*(fact(y-1))

poisson_random_variables = [float(x) for x in input().split()]

e = 2.71828
l_A = poisson_random_variables[0] # Machine A repair poisson random variable mean variance
l_B = poisson_random_variables[1] # Machine B repair poisson random variable mean variance

cost_A = 160 + 40 * (l_A + l_A**2)
cost_B = 128 + 40 * (l_B + l_B**2)

print("%.3f" % cost_A)
print("%.3f" % cost_B)


