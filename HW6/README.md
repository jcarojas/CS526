Problem 1: Priority Queue

For this problem I merge the k register logs with a priority queue as a binary min-heap stored in a Python list. The main idea is that I never put all the sales in the queue. Each log is already sorted, so the next sale overall has to be the front sale of one of the registers. I start by pushing the first sale from every register that has one, so the queue holds at most one entry per register. Then I repeat the same step until the queue is empty. I pop the smallest entry, add it to the output, and push the next sale from that same register if there is one. Since every pop is followed by at most one push from the register that was just popped, the queue can never go over k entries.

The entries I push are (time, register) tuples. I use tuples because Python compares tuples from left to right, so if two sales have the same time, the lower register number is smaller and comes out first. That handles the tie rule without extra code, and the popped entry is already in the (time, register) format. Because I only keep the register number in the queue, I use a small list called nxt that remembers which position each register’s log is up to. One thing to watch for is that a register number can only be in the queue once, so two entries in the queue never tie on both time and register.

There were some special cases that I had to consider while writing the code. Empty logs like [] must never be pushed because there is no front sale to look at, blank lines in the input need to be skipped when reading, and duplicate times across registers need the tie rule above. I also had to avoid loading every sale into the queue at the start, since that would break the size rule. For time, each of the N sales is pushed once and popped once, and each push or pop on a queue of size at most k costs O(log k), so the total is O(N log k). For memory, the queue and the nxt list are both O(k), not counting the input and the output list.


Problem 2:

Problem 3:
