def factors(n: int) -> int:
    i = 1
    count = 0
    while i <= n:
        if n % i == 0:
            count += 1
        i += 1
    return count


def isPrime(n: int) -> bool:
    if factors(n) != 2:
        return False
    return True

    # return factors(n) == 2


number = 7
if isPrime(number):
    print("It is a prime")
else:
    print("It is not a prime")
