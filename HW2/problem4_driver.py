#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import sys

from problem4 import SortedDoublyLinkedList

ARG_COUNTS = {
    "add": 1,
    "delete": 1,
    "exists": 1,
    "count": 1,
    "total": 0,
    "sum_middle_three": 0,
    "median": 0,
    "print_list": 0,
}


def parse_number(text):
    try:
        return int(text)
    except ValueError:
        pass
    try:
        number = float(text)
    except ValueError:
        return None
    return number if math.isfinite(number) else None


def main():
    lst = SortedDoublyLinkedList()

    for line_no, raw in enumerate(sys.stdin, start=1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue

        parts = line.split()
        directive, args = parts[0], parts[1:]

        if directive not in ARG_COUNTS:
            print(f"Warning (line {line_no}): unknown directive '{directive}'")
            continue
        if len(args) != ARG_COUNTS[directive]:
            print(f"Warning (line {line_no}): '{directive}' expects "
                  f"{ARG_COUNTS[directive]} argument(s), got {len(args)}")
            continue

        value = None
        if args:
            value = parse_number(args[0])
            if value is None:
                print(f"Warning (line {line_no}): '{args[0]}' is not a number")
                continue

        if directive == "add":
            lst.add(value)
        elif directive == "delete":
            if not lst.delete(value):
                print(f"Warning (line {line_no}): {value} is not in the list")
        elif directive == "exists":
            print(f"exists({value}) = {lst.exists(value)}")
        elif directive == "count":
            print(f"count({value}) = {lst.count(value)}")
        elif directive == "total":
            print(f"total() = {lst.total()}")
        elif directive == "sum_middle_three":
            try:
                print(f"sum_middle_three() = {lst.sum_middle_three()}")
            except ValueError as e:
                print(f"Warning (line {line_no}): {e}")
        elif directive == "median":
            try:
                print(f"median() = {lst.median()}")
            except ValueError as e:
                print(f"Warning (line {line_no}): {e}")
        elif directive == "print_list":
            lst.print_list()

    print("Final list: ", end="")
    lst.print_list()


if __name__ == "__main__":
    main()

