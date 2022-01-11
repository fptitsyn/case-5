# !/usr/bin/env python3
# -*- encoding: utf-8 -*-


def is_magic_date(day, month, year):
    last_digits = year % 1000 % 100
    if day * month == last_digits:
        return True
    return False


if __name__ == "__main__":
    for i in range(100):
        for j in range(12):
            for i in range(3):
                pass
