# Subarray Addition
## Description:
You are given an array $A$ having $N$ integers. You take an array $B$ of length $N$ such that $B_i = 0$ for all $1 \leq i \leq N$. You perform $Q$ operations of the following two types:

* **1 $L$ $R$ $X$**: add $X$ to all elements of the subarray $A[L \dots R]$
* **2 $L$ $R$**: add $A_i$ to $B_i$ for all $L \leq i \leq R$.

Print the elements of the array $B$ after $Q$ operations.

## Input format
* The first line of input contains two integers $N, Q$ denoting the length of the array $A$ and the number of operations respectively.
* The second line contains $N$ integers $A_1, A_2, \dots, A_N$, denoting elements of the array $A$.
* Each of the next $Q$ lines contains a description of one of the two types of operations.

## Output format
Print $N$ integers $B_1, B_2, \dots, B_N$, denoting elements of the array $B$ after $Q$ operations.

## Constraints
* $1 \leq N, Q \leq 2 \cdot 10^5$
* $1 \leq A_i, X \leq 10^5$
* $1 \leq L_i \leq R_i \leq N$

## Examples:
### Example 1:
**Input:**
```
5 5
3 2 6 1 3
1 2 3 1
2 3 5
1 1 4 3
1 1 2 6
2 1 4
```
**Output:**
```
12 12 17 5 3
```
**Explaination:**  
* After the first operation, $A$ becomes $[3, 2 + 1, 6 + 1, 1, 3] = [3, 3, 7, 1, 3]$.
* After the second operation, $B$ becomes $[0, 0, 0 + 7, 0 + 1, 0 + 3] = [0, 0, 7, 1, 3]$.
* After the third operation, $A$ becomes $[3 + 3, 3 + 3, 7 + 3, 1 + 3, 3] = [6, 6, 10, 4, 3]$.
* After the fourth operation, $A$ becomes $[6 + 6, 6 + 6, 10, 4, 3] = [12, 12, 10, 4, 3]$.
* After the fifth operation, $B$ becomes $[0 + 12, 0 + 12, 7 + 10, 1 + 4, 3] = [12, 12, 17, 5, 3]$.