# Minimum AND xor OR
## Description:
Given an array $A$ of $N$ integers. Find out the minimum value of the following expression for all valid $i, j$.

$(A_i \text{ and } A_j) \text{ xor } (A_i \text{ or } A_j)$, where $i \neq j$.

## Input Format:
* First line: A single integer $T$ denoting the number of test cases
* For each test case:
    * First line contains a single integer $N$, denoting the size of the array.
    * Second line contains $N$ space separated integers $A_1, A_2, \ldots, A_n$

## Output Format:
For each test case, print a single line containing one integer that represents the minimum value of the given expression

## Constraints:
- $1 \le T \le 10^3$
- $1 \le N \le 10^5$
- $0 \le A_i \le 10^9$
- **Note:** Sum of $N$ overall test cases does not exceed $10^6$
## Examples:
### Example 1:
**Sample Input:**
```
2
5
1 2 3 4 5
3
2 4 7
```
**Sample Output:**
```
1
3
```
**Explaination:**  
For test case #1, we can select elements $2$ and $3$, the value of the expression is $(2 \text{ and } 3) \text{ xor } (2 \text{ or } 3) = 1$, which is the minimum possible value. Another possible pair is $4$ and $5$.

For test case #2, we can select elements $4$ and $7$, the value of the expression is $(4 \text{ and } 7) \text{ xor } (4 \text{ or } 7) = 3$, which is the minimum possible value.