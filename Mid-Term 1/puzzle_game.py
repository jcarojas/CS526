import sys
from math import isqrt


def is_valid():
    n = int(sys.stdin.readline())
    symbols = set(sys.stdin.readline().strip().split(','))
    s = isqrt(n)
    
    cols = [set() for _ in range(n)]
    boxes = [set() for _ in range(n)]

    for r in range(n):
        row = sys.stdin.readline().strip().split(',')
        row_seen = set()

        for c, sym in enumerate(row):
            if sym == '.':
                continue

            box = (r // s) * s + c // s

            if (sym not in symbols
                    or sym in row_seen
                    or sym in cols[c]
                    or sym in boxes[box]):
                return False

            row_seen.add(sym)
            cols[c].add(sym)
            boxes[box].add(sym)

    return True

def main():
    if is_valid():
        print("The board is valid")
    else:
        print("The board is invalid")


if __name__ == "__main__":
    main()
