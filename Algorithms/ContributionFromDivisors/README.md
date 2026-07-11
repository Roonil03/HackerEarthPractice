# Contribution from divisors
## Description:
Let us define a few functions over natural numbers,  
$F(n) =$ sum of odd digits in decimal representation of $n$.  
For example, $F(123) = 1 + 3 = 4$ and $F(15423) = 1 + 5 + 3 = 9$.
 
$G(n) = \sum_{d|n} f(d)$,  
that is, sum of $F(d)$ over all factors $d$ of $n$.  
For example, $G(10) = F(1) + F(2) + F(5) + F(10) = 7$.

## Input:
First line of the input contains 1 integers, $Q$, representing number of queries. Next $Q$ line contains 1 integers each, representing $n$.

## Output:
N lines, each line containing 1 integers, representing $G(n)$.

## Constraints:
* $1 \le Q \le 10^6$
* $1 \le N \le 10^6$

## Examples:
### Example 1:
**Sample Input:**
```
1
10
```
**Sample Output:**
```
7
```
**Explaination:**  
Same example as the one given in the problem statement.