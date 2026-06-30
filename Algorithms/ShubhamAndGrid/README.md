# Shubham and Grid
## Description:
You are given a grid of $n$ rows and $m$ columns consisting of lowercase English letters $a$, $b$, $c$, and $d$.

We say 4 cells form a **"nice-quadruple"** if and only if

1. The letters on these cells form a permutation of the set $\{a, b, c, d\}$.
2. The cell marked $b$ is directly reachable from cell marked $a$.
3. The cell marked $c$ is directly reachable from the cell marked $b$.
4. The cell marked $d$ is directly reachable from the cell marked $c$.

A cell $(x2, y2)$ is said to be directly reachable from cell $(x1, y1)$ if and only if $(x2, y2)$ is one of these 4 cells $\{(x1 - 1, y1), (x1 + 1, y1), (x1, y1 - 1) \text{ and } (x1, y1 + 1)\}$.

Given the constraint that each cell can be part of at most 1 **"nice-quadruple"**, what's the maximum number of **"nice-quadruples"** you can select?

## Input format

* First line: Two space-separated integers $n$ and $m$
* Next $n$ lines: Each contains $m$ space separated lowercase letters from the set $\{a, b, c, d\}$ denoting the grid cells.

## Output format

Output the maximum number of **"nice-quadruple"** you can select.

## Constraints

$1 \le n, m \le 20$

## Examples:
### Example 1:
**Sample Input:**
```
4 7
d a b a b c d
a d c b d d d
d d d c d d d
d d d d d d d
```
**Sample Output:**
```
2
```
**Explaination:**   
Let $(i, j)$ represent the cell in row $i$ and column $j$ (considering $(1, 1)$ as the top left of the grid). Then the set of cells $\{(1, 2), (1, 3), (2, 2), (2, 3)\}$ form one **"nice-quadruple"** and the set of cells $\{(1, 4), (1, 5), (1, 6), (1, 7)\}$ form another **"nice-quadruple"**. You can verify that you cannot get more than 2 **"nice-quadruple"**.