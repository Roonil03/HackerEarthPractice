# Substring Xor
## Description:
Given a length-$n$ array $a$ and a number $k$, there are $\frac{n \times (n+1)}{2}$ subarrays in total. For each subarray, we can compute the xor sum of its elements.

In this problem, we will sort all these xor-sums in non-increasing order. And we want to find the $k^{th}$ element.

## Input

The first line contains two numbers $n$ ($1 \le n \le 100000$) and $k$ ($1 \le k \le \frac{n \times (n+1)}{2}$).

The second line contains $n$ numbers - $a_1, a_2, a_3, \dots, a_n$ ($0 \le a_i < 2^{20}$).

## Output

Output the $k^{th}$ element in the non-increasing order.

## Examples:
### Example 1:
**Sample Input:**
```
5 10
1 4 3 12 8
```
**Sample Output:**
```
4
```
**Explaination:**  
All the xors of subarrays are $(15, 12, 11, 10, 8, 7, 7, 6, 5, 4, 4, 3, 3, 2, 1)$, the $10^{th}$ is $4$.