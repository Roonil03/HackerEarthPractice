# Permutation deliveries
## Description:
Consider that you are given a permutation $p$ of length $n$.
Let us define $parts(p)$ as the minimum size of a subset of $\{1, 2, 3, \dots, n\}$ like $s$ that for all $i$ $(1 \leq i \leq n)$, at least one of $i$ or $p_i$ or $p_{p_i}$ or $p_{p_{p_i}}$ or ... are in $s$.
For example, $parts(1, 2, 3) = 3$ and $parts(2, 1, 3) = 2$.

You are given $n$ for all $i$ $(1 \leq i \leq n)$ find number of permutations like $p$ that $parts(p) = i$ modular $998244353$.

## Input format
The only line of input contains an integer $n$.
$1 \leq n \leq 5 \times 10^5$

## Output format
Print a single line $n$ space-separated integers denoting the answer of the problem.

## Examples:
### Example 1:
**Input:**
```
3
```
**Output:**
```
2 3 1
```
**Explaination:**  
$parts(1, 2, 3) = 3$  
$parts(1, 3, 2) = 2$  
$parts(2, 1, 3) = 2$  
$parts(3, 2, 1) = 2$  
$parts(2, 3, 1) = 1$  
$parts(3, 1, 2) = 1$  