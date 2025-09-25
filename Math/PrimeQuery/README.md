# Prime Query
## Description
You are given an array $A$ having $N$ integers and $Q$ queries. Each query is described by two integers $L$ and $R$. For each query, find the number of pairs $(i, j)$ such that $L \leq i < j \leq R$ and $A_i + A_j$ can be expressed as the sum of one or more prime numbers.

In the sum, you are allowed to use a prime number more than once.

## Input Format

- The first line of input contains an integer $T$ denoting the number of test cases.
- The first line of each test case contains an integer $N$.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.
- Then $Q$ lines follow, each containing two space-separated integers $L$ and $R$.

## Output Format

For each query, print the number of pairs that satisfies the given conditions in a separate line.

## Constraints

- $1 \leq T \leq 10$
- $2 \leq N \leq 10^5$
- $0 \leq A_i \leq 10^5$
- $1 \leq Q \leq 10^5$
- $1 \leq L \leq R \leq N$

## Examples:
### Example 1:
**Input:**
```
1
5
2 4 1 0 5
2
3 5
1 5
```
**Output:**
```
2
9
```
**Explaination:**  
- In the first query the pairs will be -
  - $(3, 5) = A_3 + A_5 = 1 + 5 = 6$ and $6$ can be expressed as the sum of primes $(2 + 2 + 2)$.
  - $(4, 5) = A_4 + A_5 = 0 + 5 = 5$ and $5$ can be expressed as the sum of primes $(2 + 3)$.

- In the second query pairs will be $(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 5), (4, 5)$.
