import fcntl
import os

def get_file_name():
    raw_path = fcntl.fcntl(0, fcntl.F_GETPATH, bytes(1024))
    return os.path.basename(raw_path.split(b"\0")[0].decode())

def count_vowel_decodings(morse):
    ways = [0] * (len(morse) + 1)
    ways[0] = 1
 
    for i in range(1, len(morse) + 1):
        total = 0
 
        if morse[i - 1:i] == ".":
            total += ways[i - 1]
 
        if i >= 2 and morse[i - 2:i] in (".-", ".."):
            total += ways[i - 2]
 
        if i >= 3 and morse[i - 3:i] in ("---", "..-"):
            total += ways[i - 3]
 
        ways[i] = total
        
    return ways[len(morse)]

def main():
    file_name = get_file_name()
 
    n = int(input())
    morse = input().strip()
 
    print("File Input:", file_name)
    print("The Number of Vowel combinations is:", count_vowel_decodings(morse))

main()
