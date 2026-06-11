# Mathison and the furthest point
## Description:
Mathison has taken a course in Computational Geometry. He managed to solve almost all problems from his latest problem sheet. The hardest one was sent to you and is described below.

You are given a $C \times C$ grid that currently contains no active points and on which you can perform certain operations.
An operation can be an activation $(x, y)$, in which you mark the point at coordinates $(x, y)$ as active if the point was not already marked. Otherwise, you do nothing.  
The second type of operation is a query $(x, y) (x_1, y_1) (x_2, y_2)$: you have to find the greatest **manhattan distance** between the point $(x, y)$ and any **active** point that lies inside the rectangle with the bottom-left corner in $(x_1, y_1)$ and the top-right one in $(x_2, y_2)$.

You are given $N$ such operations and you have to execute them all!

## Input
The first line of the input file contains one integer, $N$, representing the number of operations.
Each of the next $N$ lines will contain either an activation or a query in the following format:

* $0 \ x \ y$: mark the point at $(x, y)$ as **active**
* $1 \ x \ y \ x_1 \ y_1 \ x_2 \ y_2$: find the greatest manhattan distance between $(x, y)$ and any **active** point from $Rectangle((x_1, y_1), (x_2, y_2))$

## Output
The output file will contain a line for each operation of type $1$. If there is no point in the given rectangle, you should print "no point!" (without quotes).

## Constraints
* $1 \leq N \leq 2 \times 10^5$
* $1 \leq C \leq 10^8$
* $0 \leq x, y, x_1, y_1, x_2, y_2 \leq C$
* $x_1 \leq x_2$ and $y_1 \leq y_2$ for all rectangles $Rectangle((x_1, y_1), (x_2, y_2))$
* The manhattan distance between $A$ and $B$ is defined to be $d(A, B) = |A_x - B_x| + |A_y - B_y|$.

## Examples:
### Example 1:
**Input:**
```
10
1 299 1000 51 14 968 953
0 328 810
1 93 776 328 810 328 810
1 91 706 328 810 328 810
0 307 664
0 491 146
1 624 697 491 146 491 146
0 922 430
0 553 764
0 678 177
```
**Output:**
```
no point!
269
341
684
```
**Explaination:**  
There are no active points for the first query so the answer is **no point!**.  
The rectangle consists of only one (active) point for the second query so the answer is $|93 - 328| + |776 - 810| = 269$.  
The rectangle consists of only one (active) point for the third query so the answer is $|91 - 328| + |706 - 810| = 341$.  
The rectangle consists of only one (active) point for the forth query so the answer is $|624 - 491| + |697 - 146| = 684$.  