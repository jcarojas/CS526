import sys


class PQ:
    def __init__(self):
        self.a = []

    def __len__(self):
        return len(self.a)

    def push(self, item):
        a = self.a
        a.append(item)
        i = len(a) - 1
        while i > 0:
            p = (i - 1) // 2
            if a[i] < a[p]:
                a[i], a[p] = a[p], a[i]
                i = p
            else:
                break

    def pop(self):
        a = self.a
        top = a[0]
        last = a.pop()
        if a:
            a[0] = last
            i, n = 0, len(a)
            while True:
                l, r, s = 2 * i + 1, 2 * i + 2, i
                if l < n and a[l] < a[s]:
                    s = l
                if r < n and a[r] < a[s]:
                    s = r
                if s == i:
                    break
                a[i], a[s] = a[s], a[i]
                i = s
        return top


def merge(logs):
    pq = PQ()
    nxt = [0] * len(logs)
    for reg, log in enumerate(logs, start=1):
        if log:
            pq.push((log[0], reg))
            nxt[reg - 1] = 1
    out = []
    while len(pq) > 0:
        t, reg = pq.pop()
        out.append((t, reg))
        i = nxt[reg - 1]
        if i < len(logs[reg - 1]):
            pq.push((logs[reg - 1][i], reg))
            nxt[reg - 1] = i + 1
    return out


def parse_line(line):
    inner = line.strip()[1:-1].strip()
    if inner == "":
        return []
    return [int(piece) for piece in inner.split(",")]


def main():
    logs = []
    for line in sys.stdin.read().splitlines():
        if line.strip():
            logs.append(parse_line(line))
    print(merge(logs))


if __name__ == "__main__":
    main()
