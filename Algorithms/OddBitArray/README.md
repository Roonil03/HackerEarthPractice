# Odd Bit Array
## Description:
You are given an array $A$ of $N$ integers. A partitioning of the array $A$ is the splitting of $A$ into one or more non-empty contiguous subarrays such that each element of $A$ belongs to exactly one of these subarrays.

Find the number of ways to partition $A$ such that the Bitwise XOR of elements within each subarray has an odd number of set bits (i.e., 1s). Since the answer may be large, output the answer modulo $10^9 + 7$.

## Input format

* The first line of input contains an integer $T$ denoting the number of test cases.
* The first line of each test case contains an integer $N$.
* The second line of each test case contains $N$ space-separated integers $A_1, A_2, \dots, A_N$.

## Output format

For each test case, print the answer in a separate line.

## Constraints

* $1 \le T \le 10$
* $1 \le N \le 10^5$
* $0 \le A_i \le 10^9$

## Examples:
### Example 1:
**Sample Input:**
```
2
3
1 6 10
5
1 4 6 8 8
```
**Sample Output:**
```
1
4
```
**Explaination:**  
For test case \(1\) - The array can be partitioned as follows
- \([1, 6, 10]\)

For test case \(2\) - The array can be partitioned as follows

- \([1], [4, 6], [8], [8]\)
- \([1], [4, 6, 8, 8]\)
- \([1], [4], [6, 8], [8]\)
- \([1, 4, 6, 8], [8]\)