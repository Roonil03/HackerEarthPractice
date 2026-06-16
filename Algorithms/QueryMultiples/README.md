# Query multiples
## Description:
An array $arr$ has indices numbered from $1$ to $N$. You are given $Q$ queries with two integers, $i X$ in each.

Write a program to find the number of multiples of $X$ in the array $arr$ that falls between the $i^{th}$ index and the end of the array.

## Input format

* First line: Two space-separated integers $N$ and $Q$
* Second line: $N$ space-separated integers (denoting the array $arr$)
* Next $Q$ lines: Two space-separated integers, $i$ and $X$

## Output format

For each query, print the number of multiples of $X$ in the array $arr$ that falls between the $i^{th}$ index and the end of the array.

## Constraints

- $1 \le N \le 10^5$
- $1 \le Q \le 10^5$
- $1 \le X \le 20000$
- $1 \le arr[i] \le 20000$

## Examples:
### Example 1:
**Sample Input:**
```
3 1
9 6 2
2 2
```
**Sample Output:**
```
2
```
**Examples:**  
There are two numbers, 6 and 2, after the index 2 divisible by 2.