#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
from math import gcd

def canon(dx, dy):
    g = gcd(abs(dx), abs(dy))
    dx //= g
    dy //= g
    if dx < 0 or (dx == 0 and dy < 0):
        dx, dy = -dx, -dy
    return (dx, dy)

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    pts = [(int(data[1 + 2*i]), int(data[2 + 2*i])) for i in range(n)]

    total = 0
    for i in range(n):
        px, py = pts[i]
        cnt = {}
        for j in range(n):
            if j == i:
                continue
            d = canon(pts[j][0] - px, pts[j][1] - py)
            cnt[d] = cnt.get(d, 0) + 1
        s = 0
        for (dx, dy), c in cnt.items():
            s += c * cnt.get(canon(-dy, dx), 0)
        total += s // 2

    print(total)

main()

