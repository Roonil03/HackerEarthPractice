# Maximize movie ratings
## Description:
A movie rating website is hacked to *maximize* the total rating of a particular show. The hacker decides to flip (negative becomes positive and vice versa) the sign of $K$ ratings. He has to perform exactly $K$ flips on $N$ ratings stored in the database. The flips may or may not be optimal. He can also flip the sign of the same rating more than once.

Write a program to calculate the highest possible total rating of the show.

## Input format
First line : Two space-separated integers, $N$ and $K$  
second line : $N$ space-separated integers denoting the ratings

## Output format
Print the highest possible rating.

## Constraints
- $1 \le N \le 10^7$
- $1 \le K \le 10^7$
- $-10 \le Rating \le 10$

## Examples:
### Example 1:
**Sample Input:**
```
4 2
-1 1 -1 1
```
**Sample Output:**
```
4
```
**Explaination:**  
We have 2 flips available,also 2 negative ratings. We flip them and arrive at total rating of `(1+1+1+1)=4`