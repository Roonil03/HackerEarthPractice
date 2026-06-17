# Nanachi and Euler Totient
## Description:
Living alone with Mitty in the Abyss, Nanachi has developed an interest in number theory problems. Nanachi recently came up with the following problem but is unable to solve it.

Let $\phi(n)$ denote the count of positive integers up to $n$ which are coprime with $n$. Since summations bore our Nanachi, Nanachi decided to evaluate the function $f(n)$ instead which is defined as:

$$f(n) = \prod_{d|n} \phi(d)$$

where $a|b$ mean $a$ divides $b$. Nanachi seeks your help in finding the value of $f(n)$.

## Input
A single integer $n$

## Output
Value of $f(n)$. Since this value can be large, output it modulo $10^9 + 7$.

## Constraints
$1 \le n \le 10^{12}$

For 10% of the testcases, $n \le 10^6$

## Examples:
### Example 1:
**Sample Input:**
```
12
```
**Sample Output:**
```
32
```
**Explaination:**  
The divisors of 12 are 1, 2, 3, 4, 6 and 12 i.e.  
$f(n) = \phi(1) \cdot \phi(2) \cdot \phi(3) \cdot \phi(4) \cdot \phi(6) \cdot \phi(12)$

$\Rightarrow f(n) = 1 \cdot 1 \cdot 2 \cdot 2 \cdot 2 \cdot 4 = 32$  