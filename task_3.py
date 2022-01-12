# !/usr/bin/env python3
# -*- encoding: utf-8 -*-
from task_2 import how_many_days


def is_magic_date(day, month, year):
    last_digits = year % 1000 % 100
    if day * month == last_digits:
        return True
    return False


if __name__ == "__main__":
    for i in range(100):
        if i < 10:
            year = int(f"190{i}")
        else:
            year = int(f"19{i}")
        for month in range(1, 13):
            for day in range(1, how_many_days(month, year) + 1):
                if is_magic_date(day, month, year):
                    if day < 10 and month < 10:
                        print(f"0{day}.0{month}.{year} is a magic date")
                    elif month < 10:
                        print(f"{day}.0{month}.{year} is a magic date")
                    elif day < 10:
                        print(f"0{day}.{month}.{year} is a magic date")
                    else:
                        print(f"{day}.{month}.{year} is a magic date")
