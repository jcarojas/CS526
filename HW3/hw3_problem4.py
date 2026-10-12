#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
from fractions import Fraction

ELIMINATED = "All Ghosts: were eliminated"
NOT_ELIMINATED = "All Ghosts: were not eliminated"


def line_through(p1, p2):
    (x1, y1), (x2, y2) = p1, p2
    if x1 == x2:
        return None, x1
    slope = (y2 - y1) / (x2 - x1)
    intercept = y1 - slope * x1
    return slope, intercept


def all_eliminated(lines):
    first_slope = lines[0][0]
    if any(slope != first_slope for slope, _ in lines):
        return False
    intercepts = [intercept for _, intercept in lines]
    return len(set(intercepts)) == len(intercepts)


def parse(text):
    rows = text.strip().splitlines()
    n = int(rows[0])

    lines = []
    for row in rows[1:n + 1]:
        _, bx, by, _, gx, gy = row.split()   # the 'B' and 'G' letters are skipped
        buster = (Fraction(bx), Fraction(by))
        ghost = (Fraction(gx), Fraction(gy))
        lines.append(line_through(buster, ghost))

    if len(lines) != n:
        raise ValueError(f"expected {n} pairs, found {len(lines)}")
    return lines


def main():
    try:
        lines = parse(sys.stdin.read())
    except (ValueError, IndexError) as err:
        print(f"Input error: {err}", file=sys.stderr)
        sys.exit(1)

    print(ELIMINATED if all_eliminated(lines) else NOT_ELIMINATED)


if __name__ == "__main__":
    main()

