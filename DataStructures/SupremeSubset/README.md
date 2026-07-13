# Supreme Subset
## Description:
Given a multiset of integers having cardinality $n$, find its **Supreme Subset**.
A supreme subset of a given multiset is one of its subsets in which -
1. if any two elements $i, j$ are chosen from subset, $|i - j|$ is divisible by $m$, where $x$ represents absolute value of x.
2. it has the highest cardinality/size among all candidate subsets satisfying **condition 1**.
3. If there are multiple subsets satisfying above 2 conditions, the supreme subset is the one which is smallest by set comparison.

**Finding order by set comparison** - Given two sets of the same size, the smaller one is defined to be the one which is lexicographically smaller when both sets are arranged in non-decreasing order, for example, the set {3,2,1} is smaller than {3,2,2}.

## **Input:**
The first line of the input contains 2 integers, $n, m$, as specified in the problem statement.  
The second line contains $n$ integers, representing the multiset $A$.  

## **Output:**
First line should have 1 integer, $k$, representing cardinality of the **Supreme Subset**.  
Second line should have $k$ members of the supreme subset in **sorted order**.  

## **Constraints:**
- $1 \le n \le 10^5$
- $1 \le m \le 10^9$
- $1 \le A_i \le 10^9$

## Examples:
### Example 1:
**Sample Input:**
```
5 3
3 2 1 4 5
```
**Sample Output:**
```
2
1 4
```
**Explaination:**  
There are 2 candidates for the Supreme Subset, `{1, 4}` and `{2, 5}`.  
But `{1, 4}` is less than `{2, 5}`.  