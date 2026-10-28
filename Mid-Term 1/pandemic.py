import sys
from collections import deque


def print_board(infected, day):
    print(f"Day {day}")
    for row in infected:
        print("  " + " ".join("X" if cell else "." for cell in row))
    print()


def main():
    data = sys.stdin.read().split()
    N = int(data[0])
    coords = data[1:]

    infected = [[False] * N for _ in range(N)]
    count = [[0] * N for _ in range(N)]
    queue = deque()
    infected_total = 0

    for k in range(0, len(coords), 2):
        r, c = int(coords[k]), int(coords[k + 1])
        infected[r][c] = True
        infected_total += 1
        queue.append((r, c))

    day = 1
    print_board(infected, day)

    while queue and infected_total < N * N:
        day += 1
        for _ in range(len(queue)):
            r, c = queue.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and not infected[nr][nc]:
                    count[nr][nc] += 1
                    if count[nr][nc] == 2:
                        infected[nr][nc] = True
                        infected_total += 1
                        queue.append((nr, nc))
        print_board(infected, day)

    if infected_total < N * N:
        print("There are healthy counties left")
    else:
        print("There are no healthy counties left")

if __name__ == "__main__":
    main()
