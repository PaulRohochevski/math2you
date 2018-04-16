def gcd(a: int, b: int) -> int:
    while b != 0:
        remainder = a % b
        a, b = b, remainder

    return a


if __name__ == '__main__':
    a = gcd(4851, 3003)
