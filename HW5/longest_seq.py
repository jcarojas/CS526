import fcntl
import os

def get_file_name():
    raw_path = fcntl.fcntl(0, fcntl.F_GETPATH, bytes(1024))
    return os.path.basename(raw_path.split(b"\0")[0].decode())

def longest_sequence(a, b):
    best_a = [1] * len(a)
    best_b = [1] * len(b)
 
    for k in range(max(len(a), len(b))):
        if k < len(a):
            for j in range(min(k, len(b))):
                if b[j] < a[k] and best_b[j] + 1 > best_a[k]:
                    best_a[k] = best_b[j] + 1
 
        if k < len(b):
            for i in range(min(k, len(a))):
                if a[i] < b[k] and best_a[i] + 1 > best_b[k]:
                    best_b[k] = best_a[i] + 1
 
    return max(best_a + best_b, default=0)
 
def main():
    file_name = get_file_name()
 
    size_a = int(input())
    size_b = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
 
    print("File Input:", file_name)
    print("Longest Sequence:", longest_sequence(a, b))

main()
