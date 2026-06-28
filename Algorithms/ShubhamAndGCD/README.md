# Shubham and GCD
## Description:
You are given an array of $n$ integer numbers $a_1, a_2, \dots, a_n$.

Define a function $f(l, r)$ as the number of pairs $(i, j)$ such that $l \leq i \leq j \leq r$ and $\gcd(a_i, a_j) \neq 1$.

Output the sum of $f(l, r)$ over all $l, r$ such that $1 \leq l \leq r \leq n$. If the sum is greater than $10^{18}$, please output $1$.

## Input format
* First line: $n$ denoting the number of array elements
* Second line: $n$ space separated integers $a_1, a_2, \dots, a_n$.

## Output format
* Output the required sum.

## Constraints
$1 \leq n, a_i \leq 100000$

## Examples:
### Example 1:
**Sample Input:**
```
3
2 4 6
```
**Sample Output:**
```
15
```
**Explaination:**  
$f(1, 1) = 1$  
$f(1, 2) = 3$  
$f(1, 3) = 6$  
$f(2, 2) = 1$  
$f(2, 3) = 3$  
$f(3, 3) = 1$  

$\text{sum} = 1 + 3 + 6 + 1 + 3 + 1 = 15$ 