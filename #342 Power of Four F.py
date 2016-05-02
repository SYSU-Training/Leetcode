import math
def isPowerOfThree(n):
	return False if n <= 0 else n == pow(4, round(math.log(n, 4)))

'''
All "Power of n" Problems can be solved by this code.
If n is Prime Number, we can use the prime_factorize function in "Ugly Number" to deal with it.
'''
