# Tree-Query
## Description:
Mike has a tree with $n$ nodes. On each node $u$, there is an integer $c_u$.

A number is **interesting** if and only if its digits in the decimal representation are distinct. For example, the numbers $1546, 198, 1$ are interesting but the numbers $1222, 1001, 9011$ are not.

Consider a length-$k$ path on the tree $P_1, P_2, \dots, P_k$, a subpath is determined by two parameters $l$ and $r$ ($1 \le l \le r \le k$). The subpath starting from $l^{th}$ node and ending on $r^{th}$ node is $P_l, P_{l+1}, \dots, P_r$. Therefore, a length-$k$ path has $\frac{k \times (k+1)}{2}$ subpaths.

He has $q$ queries. Each query consists of two numbers, $u$ and $v$. Considering the path starting from $u$ and ending at $v$, he wants to know the number of interesting subpaths. A subpath is **interesting** if and only if there exists at least one node on the subpath whose assigned number is interesting.

## Input
The first line contains a number $n$ ($1 \le n \le 500\,000$).

The next line contains $n$ numbers $c_1, c_2, \dots, c_n$ ($c_i$ is the assigned number to node $i$ ($1 \le c_i \le 10^9$)).

The next $n - 1$ lines contains two numbers separated by space. The $(i + 2)^{th}$ line contains $a_i, b_i$ ($1 \le a_i, b_i \le n$) representing that there is an edge from the node $a_i$ to the node $b_i$.

The next line contains a number $q$ ($1 \le q \le 500\,000$).

The next $q$ lines contains two numbers separated by space. The $(n + 1 + i)^{th}$ line contains $u_i, v_i$ ($1 \le u_i, v_i \le n$).

## Output
Output $q$ lines. The $i^{th}$ line must contain the answer for the $i^{th}$ query.

## Examples:
**Sample Input:**
```
8
1 1 11 11 11 1 11 11
1 2
2 4
2 8
1 3
3 5
3 6
3 7
5
4 7
4 6
8 5
2 3
3 5
```
**Sample Output:**
```
11
13
11
5
0
```
**Explaination:**  
For first query, there are 11 interesting subpaths in the path starting from 4 and ending at 7.