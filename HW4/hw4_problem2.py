#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    T = int(data[1])
    arr = [int(x) for x in data[2:2 + n]]

    total = 0
    count = 0
    for x in sorted(arr, reverse=True):
        total += x
        count += 1
        if total > T:
            break

    print("Input: " + ",".join(str(x) for x in arr) +
          " Target: " + str(T) + " Answer: " + str(count))

main()

