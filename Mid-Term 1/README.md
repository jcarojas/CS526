Problem 1:

The key observation is that A is a prefix-sum array, so it already stores running totals. The snowfall on days i, i+1, and i+2 is the total through day i+2 minus the total through day i-1.

Any range sum becomes a single subtraction, so I never re-add daily snowfall. My first instinct was to add A[i-2] + A[i-1] + A[i], but that adds three running totals, which doesn’t represent three days of snow. For the example [6, 13, 13, 17], days 2-4 had 7 + 0 + 4 = 11 inches, and A[4] - A[1] = 17 - 6 = 11, while adding three entries gives 43. Again, the key is understanding that the values are cumulative.

The main idea behind my program is to slide a three-day window across the array of values until we arrive at the end of the array. For each window, compute A[i+2] - A[i-1] and compare it to half the total. The output is YES at the first window that qualifies, and NO if none do.

The first trap is the first window and A[0]. The formula needs A[i-1], and for the first window (i = 1) that is A[0], the total before day 1, which is 0. The input array doesn’t contain it though. With 0-indexed code, writing A[j-3] for the first window evaluates to A[-1], which is the last element of the list, meaning the grand total.

I avoided this by prepending a 0 to the list. Now A[0] = 0 and A[1…n] match the problem’s 1-indexed notation, so the formula A[i+2] - A[i-1] works for every window with no special case and no negative indexing.

The next trap is that the problem requires strictly more than half, so a window that is exactly half the total does not count. Sample input 3 tests this. Its total is 32, and the best window (days 2-4) has 5 + 6 + 5 = 16, exactly half, so the correct answer is NO. Using >= would wrongly output YES.

I also avoided floats strategically. Instead of comparing the window to total / 2, I compare 2 * window > total. Both sides are integers, so the comparison is exact, with no rounding concerns and no float conversion.

The next trap I believe is the bounds of the program. When n < 3, the answer is NO, and the code checks this explicitly instead of relying on the loop happening to do nothing. With the prepended 0, the window start i runs from 1 to n-2, written range(1, n - 1). The largest index accessed is A[i+2] = A[n], the last valid element, so the loop never goes out of bounds. When n = 3, exactly one window is checked (days 1-3), and the loop handles it correctly.

In terms of memory, after the prepend, the total is A[n]. I store it once in a variable instead of recomputing it each iteration.

The algorithm is O(n). Building the list is O(n), and the loop checks at most n-2 windows, each in constant time because of the subtraction. Without the prefix-sum insight, summing each window’s days separately would still be O(n) for a fixed window size of 3, but it would require first converting the cumulative array into daily values. Using the prefix sums directly avoids that extra step and generalizes to any window size without extra cost per window. A single pass is also optimal in the worst case, because if the answer is NO every window has to be examined.

The function returns True as soon as one window qualifies, so YES cases often finish before reaching the end of the array. The program stores the input array in O(n) space. Prepending the 0 with [0] + A creates a new list, so there is a temporary second copy of the array, which is still O(n) overall. I accepted this because it removes the special case for the first window and makes the code simpler and less error-prone, and the cost is negligible at these input sizes. If memory were critical, I could avoid the copy by computing the “before” value with a conditional (0 if i == 0 else A[i-1]) and keeping the original list, or by only keeping the last few values while reading the input. For this problem, I chose clarity over saving a constant factor of memory.


Problem 2:


