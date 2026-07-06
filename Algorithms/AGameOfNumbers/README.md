# A Game of Numbers
## Description:
You are given an array $A$ of $N$ integers. Two functions, $F(X)$ and $G(X)$, are defined as follows:

* **$F(X)$:** The smallest index $Z$ such that $X < Z \leq N$ and $A[X] < A[Z]$. (This is the index of the **Next Greater** element).
* **$G(X)$:** The smallest index $Z$ such that $X < Z \leq N$ and $A[X] > A[Z]$. (This is the index of the **Next Smaller** element).

You need to find $A[G(F(i))]$ for each index $i$ of the array, where $1 \leq i \leq N$. If $G(F(i))$ does not exist, output `1`.

## Input
* The first line contains a single integer $N$ denoting the size of array $A$.
* Each of the next $N$ lines contains a single integer, where the integer on the $i^{th}$ line denotes $A[i]$.

## Output
Print $N$ space-separated integers on a single line, where the $i^{th}$ integer denotes $A[G(F(i))]$ or `1`, if $G(F(i))$ does not exist.

## Constraints
* $1 \leq N \leq 30000$
* $0 \leq A[i] \leq 10^{18}$

## Examples:
### Example 1:
**Sample Input:**
```
8
3
7
1
7
8
4
5
2
```
**Sample Output:**
```
1 4 4 4 -1 2 -1 -1
```
**Explaination:**  
| Next Greater | Next Smaller |
| :--- | :--- |
| 3 --> 7 | 7 --> 1 |
| 7 --> 8 | 8 --> 4 |
| 1 --> 7 | 7 --> 4 |
| 7 --> 8 | 8 --> 4 |
| 8 --> -1 | -1 --> -1 |
| 4 --> 5 | 5 --> 2 |
| 5 --> -1 | -1 --> -1 |
| 2 --> -1 | -1 --> -1 |