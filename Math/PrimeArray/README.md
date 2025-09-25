# Prime Array
## Description:

You are given an array $A$ having $N$ integers. Find the number of triplets $(i, j, k)$ such that

- $1 \leq i < j < k \leq N$
- $A_i \times A_j \times A_k$ is Prime number.

## Input format

- The first line of input contains an integer $T$ denoting the number of test cases. The description of each test case is as follows:
- The first line of each test case contains an integers $N$.
- The second line of each test case contains $N$ integers $A_1, A_2, \ldots, A_N$.

## Output format

For each test case, print the number of triplets that satisfies the given conditions in a separate line.

## Constraints

- $1 \leq T \leq 10$
- $3 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^5$

## Examples:
### Example 1:
**Input:**
```
2
4
4 5 6 2
4
1 1 4 5
```
**Output:**
```
0
1
```
**Explaination:**  
- In the first test case there are no tuples that satisfy the given conditions.
- In the second test case the tuples will be $(1, 2, 4)$ as $1 \times 1 \times 5 = 5$ which is prime number.