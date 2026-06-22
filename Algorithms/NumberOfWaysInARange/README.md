# Number of ways in a range
## Description:
You are given three integers, namely $L$, $R$, and $X$, where $X$ varies from $[L, R]$.

Write a program to find the sum of the number of ways in which $X$ people are chosen. If you choose a $person_i$ $(1 \le i \le X)$, then you cannot choose its neighboring person.

## Input Format
* First line: $T$ (number of test cases)
* First line in each test case: Two space-separated integers $L$ and $R$

## Output Format
* For each test case, print the sum of the number of ways modulo $10^9 + 7$ in which $X$ people are chosen, where if you choose a $person_i$ $(1 \le i \le X)$, you can choose one or none of its immediate neighbors, but not both.

## Constraints
* $1 \le T \le 10^3$
* $1 \le L \le R \le 10^9$

## Examples:
### Example 1:
**Sample Input:**
```
3
1 1
1 2
1 3
```
**Sample Output:**
```
2
6
13
```
**Explaination:**  
Case 1: If the number of persons is 1, you can either choose it or not choose it. 2 ways.