number = int(input("Enter a number = "))


def sum(number: int):
    total = 0
    while number > 0:
        last_digit = number % 10
        total = total + last_digit
        number = number // 10
    return total


p = sum(number)
print(p)
