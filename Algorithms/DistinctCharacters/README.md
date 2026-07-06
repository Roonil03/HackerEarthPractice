# Distinct characters
## Description:
You are given a string $S$ of length $N$ and $Q$ queries. In each query, you are provided with two integers $L$ and $R$. Find the number of distinct characters present in the range $[L, R]$.

## Input
* The first line of input contains $N$, the length of the string $S$.
* The second line of input contains the string $S$ (consisting of lowercase alphabets only).
* The third line of input contains $Q$, the number of queries.
* Each of the following $Q$ lines contains two integers, $L$ and $R$.

## Output
For each query, output the number of distinct characters in the specified range on a new line.

## Constraints
* $1 \leq N \leq 10^5$
* $1 \leq Q \leq 10^5$
* $1 \leq L \leq R \leq N$

## Examples:
### Example 1:
**Sample Input:**
```
6
nikunj 
2
1 6
1 4
```
**Sample Output:**
```
5
4
```
**Explaination:**  
In the First Query , there are 5 distinct characters from substring '`nikunj `' .

In the Second Query , 4 there are 4 distinct characters from substring '`niku`'.