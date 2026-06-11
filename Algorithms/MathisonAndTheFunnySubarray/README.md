# Mathison and the funny subarray
## Description:
Mathison has been playing quite a lot with some array $A$ of length $N$. A subarray of the given array is called *funny* if it starts and ends with the same number.

Your task is to find the length of the longest *funny* subarray of the given array.

## Input
The first line of the input file contains an integer, $N$, representing the number of integers in the given array.
The second line of the input file contains $N$ space-separated integers, where the $i^{th}$ integer represents $A[i]$.

## Output
The output file should contain only one integer, the length of the longest *funny* subarray.

## Constraints
* $1 \leq N \leq 10^6$
* $1 \leq A[i] \leq 10^5$
* A **subarray** is a subset of consecutive elements of an array.

## Examples:
### Example 1:
**Input:**
```
9
2 2 3 1 2 2 3 1 1
```
**Output:**
```
6
```
**Explaination:**  
The longest *funny* subarray has a length of 6. There are two possible choices: $[2, 2, 3, 1, 2, 2]$ and $[1, 2, 2, 3, 1, 1]$.