# The furious five
## Description:
You are given an integer $N$.

Write a program to find a minimum number $P$ such that $1 \le X \le P$, $\sum F(X) \ge N$ (where $F(X)$ represents the number of times $X$ can be divided by 5).

### Example
$F(250) = 3$, $250/5 = 50$, $50/5 = 10$, $10/5 = 2$: As $2$ cannot be divided by $5$, the procedure stops here.

For $1 \le X \le P$, $\sum F(X)$ is defined as $F(1) + F(2) + F(3) + F(4) + \dots + F(P)$

## Input format
* First line: $T$ (Number of test cases)
* First line in each test case: $N$

## Output format
For each test case, print a minimum number $P$ such that $1 \le X \le P$, $\sum F(X) \ge N$ (where $F(X)$ represents the number of times $X$ can be divided by 5).

## Constraints
$1 \le T \le 10^5$
$1 \le N \le 10^9$

## Examples:
### Example 1:
**Sample Input:**
```
2
1
2
```
**Sample Output:**
```
5
10
```
**Explaination:**  
Second case, $n = 2$, now start checking from $1$, since $1, 2, 3, 4, 6, 7, 8, 9$ are not divisible by $5$, so for count $2$ minimum $P$ will be $10$.
