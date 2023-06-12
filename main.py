def get_prime_factors(num):
    primes = []
    for n in range(2,int(num/2)+1):
        if num % n == 0:
            primes.append(n)
    return primes if len(primes) > 0 else [num]


print(get_prime_factors(15))
// author method
def get_prime_factors1(num):
    factors = []
    divisor = 2
    while divisor <= num:
        if num % divisor == 0:
            factors.append(num)
            num = num // divisor
        else:
            divisor += 1
    return factors
print(get_prime_factors1(15))