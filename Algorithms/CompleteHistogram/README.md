# Complete Histogram
## Description:
Histograms are generally fun to play with. But not all histograms are complete. Making a normal histogram complete, is not such an easy task. We will attempt to do it here.

Let us first define a complete histogram. A histogram is complete iff it satisfies the following conditions -

1. There have to be $N$ bars in the histogram.
2. The height of any bar in the histogram should be either 0 or $M$.
3. For any pair of $i, j$, if $((i == 1$ or $Height_{i-1} != Height_i)$ and $(j == N$ or $Height_{j+1} != Height_j)$ and $(Height_k == Height_i$, for all $i \le k \le j))$ holds, then $a \le j - i + 1 \le b$ should hold.

You are given a histogram, which may or may not be complete. It has to be converted into a complete histogram with minimum cost incurred. You are allowed to increase or decrease height of any bar in it. The cost of increasing any bar by unit height costs $x$ and decreasing any bar by unit height costs $y$.

## Input:
The first line of the input contains 6 integers, $N, M, a, b, x, y$, as mentioned in the problem statement.  
The second line contains $N$ integers, representing an array A of size $N$, where the element at index $i$ represents $Height_i$.

## Output:
A single integer representing the minimum cost needed to convert the histogram into a complete histogram. Print -1 if it is not possible to make a complete histogram.

## Constraints:
* $1 \le N \le 10^5$
* $1 \le M \le 10^5$
* $1 \le x \le 10^5$
* $1 \le y \le 10^5$
* $0 < a \le b \le N$
* $0 \le Height_i \le M$

## Examples:
### Example 1:
**Sample Input:**
```
5 10 1 1 1 1
4 2 9 6 5 
```
**Sample Output:**
```
20
```
**Explaination:**  
We can make 1st, 3rd and 5th bar of height 10 and 2nd, 4th bars of height 0. The total cost is $6 + 2 + 1 + 6 + 5 = 20$.