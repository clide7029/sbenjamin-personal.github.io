def primes(end):
    prime_list = []
    nums = list(range(2,end+1))
    for n in nums:
        if(is_prime(n)):
            prime_list += [n]
    print(prime_list)
    return prime_list


def is_prime(num):
    subn = list(range(2,num))
    for n in subn:
        if(num % n == 0):
            return False
    return True

def prime_factors(num):
    pr_factors = []
    while not is_prime(num):
        pos_factors = primes(num)
        new_factor = find_factor(num, pos_factors, pr_factors)
        pr_factors += [new_factor]
        num = num // new_factor
    if(is_prime(num)):
        pr_factors += [num]
    print(pr_factors)

def find_factor(num, pos_factors, pr_factors):
    for x in pos_factors:
        if(num % x == 0):
            return x

user = int(input("enter a number: "))

# primes(user)

prime_factors(user)