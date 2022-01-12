# !/usr/bin/env python3
# -*- encoding: utf-8 -*-

from math import sqrt


def is_prime(n):
    count = 0
    if n in [0, 1]:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            count += 1
    if count > 0:
        return False
    return True


if __name__ == '__main__':
    a = int(input())
    print(is_prime(a))
