import sys

def has_big_window(A):
    n = len(A)
    if n < 3:
        return False
        
    A = [0] + A
    total = A[n]
    
    for i in range(1, n - 1):
        window = A[i + 2] - A[i - 1]
        if 2 * window > total:
            return True
    return False

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    A = [int(x) for x in data[1:1 + n]]
    
    answer = "YES" if has_big_window(A) else "NO"
    print(f"{' '.join(map(str, A))} solution: {answer}")

if __name__ == "__main__":
    main()


# 
