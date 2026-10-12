#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sys


def is_palindrome(s):
    return s == s[::-1]

def main():
    count = 0
    for line in sys.stdin:
        word = line.rstrip("\n")
        result = is_palindrome(word)
        print(result)
        if result:
            count += 1
    print(count)

if __name__ == "__main__":
    main()

