
# i don't remember how to check for primes, but this makes sense to me
# there's almost certainly a faster way to do this...
# def check_if_prime(n):
#     for i in range(2,(n//2)+1):
#         if n % i == 0:
#             return False
#     return True

# num = 600851475143
# largest = 0
# for i in range(1,(num//2)+1,2):
#     print(f'checking {i}')
#     if(check_if_prime(i) and num % i == 0):
#         largest = i
# print(largest)

# the above solution is far too slow... lets see if i can improve it
# my prime checker above seems to be described in https://en.wikipedia.org/wiki/Primality_test as 'trial division'
# reading through the article, a simple and more efficient primality check can done with the 6k+-1 method
# but I think an even better method is computing primes up to sqrt(n) with the sieve of eratosthenes https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

from math import sqrt

def sieve(n):
    a = [True for i in range(n+1)]
    for i in range(2, int(sqrt(n))):
        if a[i] == True:
            for j in range(i**2, n, i):
                a[j] = False
    return [i for i in range(2, n+1) if a[i]]

num = 600851475143
relevant_primes = sieve(int(sqrt(num)))
largest_prime = 0
for prime in relevant_primes:
    if num % prime == 0:
        largest_prime = prime
print(largest_prime)

# nice, it worked! but i have a sneeking suspicion that this