#263. Ugly Number  
#set
prime_list=[2,3,5]
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def is_ugly_number(num):
    prime=list(set(prime_factors(num)))
    flag=True
    for i in range(len(prime)):
        if prime[i] not in prime_list:
            flag=False
    return flag
#test
number=raw_input("number: ")
print is_ugly_number(int(number))

