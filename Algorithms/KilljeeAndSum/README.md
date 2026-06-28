# Killjee and Sum
## Description:
Killjee loves playing with numbers. Recently, his friend, Sam, gave him 3 numbers $N, M$, and $R$ and asked him to find a magic value of these numbers.

The magic value of three numbers $= \left( \sum_{i=1}^{R-1} \binom{N}{i} * \binom{M}{R-i} * i * (R - i) \right) \pmod{10^7 + 19}$.

## INPUT FORMAT

The first line of input contains a single integer $T$ denoting the number of test cases. $T$ lines follow each containing 3 space separated integers $N, M$, and $R$.

## OUTPUT FORMAT

For each test case, print the magic value in new line.

## INPUT CONSTRAINTS

* $1 \leq N, M \leq 10^{18}$
* $R \leq (N + M)$
* $1 \leq T \leq 100$

## Examples:
### Example 1:
**Sample Input:**
```
2
3 2 2
2 2 3
```
**Sample Output:**
```
6
8
```
**Explaination:**  
For first test case magic value $= (3 \text{ choose } 1) * (2 \text{ choose } 1) * (1) * (1)$, which is equal to $6$.