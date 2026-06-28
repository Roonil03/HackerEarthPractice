# Killjee and Magic Value
## Description:
In this question, Killjee gives you three integers $N$, $M$, and $K$. You need to find the **magic value** of three numbers.

Suppose $P = \sum_{i=N}^{M} \text{fibonacci}[i] \times i!$ (factorial here), where $\text{fibonacci}[0] = \text{fibonacci}[1] = 1$ and $\text{fibonacci}[i] = \text{fibonacci}[i - 1] + \text{fibonacci}[i - 2]$. The **magic value** is maximum $X$ such that $K \times X \leq P$.

Since the answer could be very large, you only need to print the **magic value** $\pmod{10^9 + 7}$.

## INPUT FORMAT
First line of input contains a single integer $T$, number of test case. $T$ lines follow each containing three space separated integers $N, M, K$.

## OUTPUT FORMAT
For each test case print a single integer, magic value of 3 numbers in new line.

## INPUT CONSTRAINTS
* $1 \leq N \leq M \leq 2 \times 10^6$
* $1 \leq K \leq 10^6$
* $1 \leq T \leq 20$

## Examples:
### Example 1:
**Sample Input:**
```
2
1 3 6
2 4 8
```
**Sample Output:**
```
3
17
```
**Explaination:**  
For 1st test case:

$\text{fib}(1)=1, \text{fac}(1)=1$
$\text{fib}(2)=2, \text{fac}(2)=2$
$\text{fib}(3)=3, \text{fac}(3)=6$

so $P = 1 + 4 + 18$

now $6 \times 3 = 18$ which is closest multiple of $6$ to $23$. So, $3$ is magic value for this case.