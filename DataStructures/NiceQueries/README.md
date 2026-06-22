# Nice Queries
## Description:
You are given an array $A$ of length $N$ which is initialized with $0$. You will be given $Q$ queries of two types:

* `1 k`: set value $1$ at index $k$ in array $A$.
* `2 y`: print the smallest index $x$ which is greater than or equal to $y$ and having value $1$. If there is no such index, print $-1$.

**Note:** Indexing is 1-based.

## Input Format
* First line contains two integers $N$ and $Q$ separated by a space.
* The next $Q$ lines contain the type of query (i.e., either a `1` or a `2`), then a space, then for type `1` queries integer $k$ and for type `2` queries integer $y$.

## Output Format
* For each query type `2`, print in a new line, the smallest index $x$ which is greater than or equal to $y$ and having value $1$. If there is no such index, print $-1$.

## Constraints
* $1 \le n \le 10^9$
* $1 \le q \le 5 \times 10^5$
* $1 \le y, k \le n$

## Examples:
### Example 1:
**Sample Input:**
```
5 5
2 3
1 2
2 1
2 3
2 2
```
**Sample Output:**
```
-1
2
-1
2
```
**Explaination:**  
* For the first query: `2 3`, there is no index greater than or equal to index $3$ having value $1$, so the answer is $-1$.
* For the second query: `1 2`, set value $1$ at index $2$.
* For the third query: `2 1`, index $2$ is greater than index $1$, having value $1$, so the answer is $2$.
* For the fourth query: `2 3`, there is no index greater than or equal to index $3$ having value $1$, so the answer is $-1$.
* For the fifth query: `2 2`, index $2$ is equal to index $2$, having value $1$, so the answer is $2$.