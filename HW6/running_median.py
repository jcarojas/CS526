import sys
from heap import MinHeap

class MaxHeap(MinHeap):
    def _before(self, a, b):
        return a > b

def running_medians(sales):
    lo = MaxHeap()
    hi = MinHeap()
    out = []
    for x in sales:
        if lo.is_empty() or x <= lo.peek():
            lo.insert(x)
        else:
            hi.insert(x)

        if len(lo) > len(hi) + 1:
            hi.insert(lo.extract_min())
        elif len(hi) > len(lo):
            lo.insert(hi.extract_min())

        if len(lo) > len(hi):
            out.append(float(lo.peek()))
        else:
            out.append((lo.peek() + hi.peek()) / 2)
    return out

def parse_list(text):
    text = text.strip()
    if text == "":
        return []
    inner = text[1:-1].strip()
    if inner == "":
        return []
    return [int(piece) for piece in inner.split(",")]

def main():
    sales = parse_list(sys.stdin.read())
    print(running_medians(sales))

if __name__ == "__main__":
    main()
