# Mathison and the exceptional list
## Description:
Mathison has practised different operations that can be performed on lists. Unfortunately, he has found a set of operations that he cannot perform efficiently so he asks for your help.

You start with an empty list, on which you perform $N$ operations. In one operation $(e, L, R)$ you add $e$ to the back of the list and print the number of *exceptional* subarrays with the length between $L$ and $R$ inclusive, in the current version of the list. An *exceptional* subarray is defined to be a subarray of the list that contains only unique elements (i.e. no two elements share the same value).

## Input
The first line of the input file contains one integer, $N$, representing the number of operations.
Each of the next $N$ lines contains three space-separated integers $e$ $L$ $R$, representing the element that is added to the list in this step and the minimum/maximum length of a queried subarray.

## Output
The output file will contain $N$ lines. The $i^{th}$ line will contain the number of *exceptional* subarrays with a length between $L_i$ and $R_i$.

## Constraints and notes
* $1 \leq N \leq 5 \times 10^5$
* $0 \leq e \leq 10^9$
* $1 \leq L \leq N$
* $1 \leq R \leq N$
* An exceptional substring is a contiguous subsequence of the list that contains only unique elements (i.e. no two elements share the same value).

## Examples:
### Example 1:
**Input:**
```
10
1 1 4
2 3 2
4 2 5
2 1 10
1 2 4
5 4 7
3 3 8
2 2 6
1 1 10
6 2 5
```
**Output:**
```
1
0
3
8
6
1
7
16
28
23
```
**Explaination:**  
There is only one *exceptional* subarray after the first insertion: $1$.  
There are three *exceptional* subarrays after the third insertion: $[1, 2], [2, 4], [1, 2, 4]$.  
There are six *exceptional* subarrays after the fifth insertion: $[1, 2], [2, 4], [4, 2], [2, 1], [1, 2, 4], [4, 3, 1]$.  
There is only one *exceptional* subarray after the sixth insertion: $[4, 2, 1, 5]$.  