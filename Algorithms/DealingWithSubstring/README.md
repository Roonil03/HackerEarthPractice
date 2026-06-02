# Dealing with Substring
## Description:
You are given a string of length $N$ consisting of only lowercase alphabets and two alphabets $x$ and $y$.
There are $Q$ queries given and each query will be specified by two integers $l$ and $r$. You have to consider the sub string $[l, r]$ of the given string and count the total number of distinct sub sequences of the sub string which starts with $x$ and ends with $y$.

**Note:**

* We consider two sub strings to be different if they start or end at different indices of the given string.
* As the count can be very large, so you have print it modulo with $10^9 + 7$.

## Input format:

First line contains a integer $N$ representing the length of string.
Second line contains a string of length $N$.
Third line contains two space separated alphabets $x$ and $y$.
Fourth line contains the number of queries $Q$.
Each of the next $Q$ lines contains two space separated integers $l$ and $r$.


## Output format:

Output Q lines, each containing a single integer representing the number of sub-sequences modulo $10^9 + 7$ for each query.


## Constraints:

* $1 \le N \le 10^5$
* $1 \le Q \le 10^5$
* $0 \le l \le r \le N - 1$

## Examples:
### Example 1:
**Sample Input:**
```
4
aabb
a b
4
0 2
1 3
0 1
0 3
```
**Sample Output:**
```
3
3
0
9
```
