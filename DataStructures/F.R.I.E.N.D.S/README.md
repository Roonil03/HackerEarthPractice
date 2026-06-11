# F.R.I.E.N.D.S
## Description:
There are $N$ People, $i$-th person wants to be friend with all the person between $[X_i, Y_i]$.

A friendship is possible between two distinct person if and only if both of them wants to be friends with each other i.e, $i$-th and $j$-th person can be friend only if $X_i \leq j \leq Y_i$ and $X_j \leq i \leq Y_j$.

Print the total number of possible friendship.

## Input format
* The first line contains $T$ denoting the number of test cases.
* The first line of each test case contains integers $N$, denoting the number of people.
* The next $N$ lines contain $X_i$ and $Y_i$.

## Output format
For each test case print the total number of possible friendship in a separate line.

## Constraints
* $1 \leq T \leq 1000$
* $1 \leq N \leq 10^5$
* $1 \leq X_i \leq Y_i \leq N$
* The sum of $N$ over all test cases does not exceed $2 \cdot 10^5$

## Examples:
### Example 1:
**Input:**
```
1
6
2 4
1 3
5 6
1 2
1 2
1 6
```
**Output:**
```
3
```
**Explaination:**  
Friendship is only possible between $(1,2)$, $(1,4)$ and $(3,6)$.