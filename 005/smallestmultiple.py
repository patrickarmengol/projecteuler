# just brute forcing
# i was thinking maybe a better way would be to start with multiplying all the primes together
divisors = tuple(d for d in range(1,21))
i = 1
while True:
    for d in divisors:
        if i % d != 0:
            i += 1
            break
    else:
        break
print(i)

"""
from a post by Chloe on the problem thread:
The smallest positive number that is evenly divisible by all of the numbers from 1 to n is the product of every prime between 1 and n(indcluding n), 
each to the highest power they can be risen to without exceeding n. 
"""