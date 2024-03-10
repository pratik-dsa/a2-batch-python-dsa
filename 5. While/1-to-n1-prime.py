def factorsCount(n: int) -> int:
    i = 1
    # print(id(i))
    count = 0
    while i <= n:
        if n % i == 0:
            count += 1
        i += 1
    return count


def isPrime(n: int) -> bool:
    fc = factorsCount(n)
    if fc == 2:
        return True
    else:
        return False


i = 1
# print(id(i))
n1 = int(input("Enter a number = "))  # 15
count = 0
while i <= n1:
    if isPrime(i):
        print(i)
        count += 1
    i += 1

print(f"Total prime numbers between 1 to {n1} = {count}")
