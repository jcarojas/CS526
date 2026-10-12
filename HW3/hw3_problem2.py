#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys

def collect_substrings(s, found):
    if s == "" or s in found:
        return  # nothing left, or already explored this substring
    found.add(s)
    collect_substrings(s[:-1], found)  # drop the last character
    collect_substrings(s[1:], found)   # drop the first character

def main():
    text = sys.stdin.readline().rstrip("\n")

    found = set()
    collect_substrings(text, found)

    for sub in sorted(found):
        print(sub)
    print(len(found))

if __name__ == "__main__":
    main()

