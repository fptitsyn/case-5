# !/usr/bin/env python3
# -*- encoding: utf-8 -*-

def how_many_days(month, year):
    if month < 1 or month > 12:
        return "Недопустимое значение month"
    else:
        if month == 2:
            if (year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0):
                return 29
            else:
                return 28
        elif month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        else:
            return 30


if __name__ == "__main__":
    m = int(input())
    y = int(input())

    print(how_many_days(m, y))
