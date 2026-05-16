# Army Parade
## Description:
You are general and your life is good, but president is going to check your work results. It's a problem. So you decided to paint grass into green. It's time for choosing soldiers for this work!

Your army has n . m
 soldiers. Each soldier is either officer or trooper. During morning greeting they are forming n rows of length m. Because this order is very comfortable for them you decided to choose equal number of rows and columns and send all soldiers which are on intersection of these rows and columns for work. You are really nervous and decided to give personal command for one of chosen soldiers that he should check quality of painting. And you understand that he can't be trooper. So you can give personal command only for officers.

For beginning you decided just calculate the number of ways to choose soldiers for this work. Two ways are different if soldiers sets in them are different or officers with personal command in them are different.

## Input Format:

The first line of input contains three space separated integers $n$, $m$ and $k$ ($1 \le n, m \le 10^9, 0 \le k \le \min(n \cdot m, 3 \cdot 10^5)$) - number of rows, number of columns and number of troopers.

Then $k$ lines are following. The $i$-th of them contains two space separated integers $r$ and $c$ ($1 \le r \le n, 1 \le c \le m$) - the row and column number of the $i$-th trooper during morning greeting. It is guaranteed that all $(r_i, c_i)$ are distinct. Also it is guaranteed that all other soldiers are officers.

## Output format

Print the number of ways modulo $2 \cdot 10^9 + 33$.

## Examples:
### Example 1:
**Sample Input:**
```
3 2 2
1 2
3 1
```
**Sample Output:**
```
12
```
**Explaination:**  
There are 12 ways to choose soldiers:
1) intersection of row $1$ and of column $1$; set is $[(1, 1)]$; $(1, 1)$ received personal command

2) intersection of row $2$ and of column $1$; set is $[(2, 1)]$; $(2, 1)$ received personal command

3) intersection of row $2$ and of column $2$; set is $[(2, 2)]$; $(2, 2)$ received personal command

4) intersection of row $3$ and of column $2$; set is $[(3, 2)]$; $(3, 2)$ received personal command

5) intersection of rows $1, 2$ and columns $1, 2$; set is $[(1, 1), (1, 2), (2, 1), (2, 2)]$; $(1, 1)$ received personal command

6) intersection of rows $1, 2$ and columns $1, 2$; set is $[(1, 1), (1, 2), (2, 1), (2, 2)]$; $(2, 1)$ received personal command

7) intersection of rows $1, 2$ and columns $1, 2$; set is $[(1, 1), (1, 2), (2, 1), (2, 2)]$; $(2, 2)$ received personal command

8) intersection of rows $1, 3$ and columns $1, 2$; set is $[(1, 1), (1, 2), (3, 1), (3, 2)]$; $(1, 1)$ received personal command

9) intersection of rows $1, 3$ and columns $1, 2$; set is $[(1, 1), (1, 2), (3, 1), (3, 2)]$; $(3, 2)$ received personal command

10) intersection of rows $2, 3$ and columns $1, 2$; set is $[(2, 1), (2, 2), (3, 1), (3, 2)]$; $(2, 1)$ received personal command

11) intersection of rows $2, 3$ and columns $1, 2$; set is $[(2, 1), (2, 2), (3, 1), (3, 2)]$; $(2, 2)$ received personal command

12) intersection of rows $2, 3$ and columns $1, 2$; set is $[(2, 1), (2, 2), (3, 1), (3, 2)]$; $(3, 2)$ received personal command

