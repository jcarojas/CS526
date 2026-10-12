import sys

def collect_substrings(s, found):
    if s == "" or s in found:
        return
    found.add(s)
    collect_substrings(s[:-1], found)
    collect_substrings(s[1:], found)

def main():
    text = sys.stdin.readline().rstrip("\n")

    found = set()
    collect_substrings(text, found)

    for sub in sorted(found):
        print(sub)
    print(len(found))

if __name__ == "__main__":
    main()

