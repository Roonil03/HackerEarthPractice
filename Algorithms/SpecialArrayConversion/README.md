# Special Array Conversion
## Description:
Given an array $A$, convert it into a "special array" based on the following characteristics:

1. **Prime Placement:** All prime numbers must appear before all non-prime numbers.
2. **Prime Ordering:** All prime numbers are sorted in **increasing order**.
3. **Non-Prime Ordering:** All non-prime numbers are sorted in **decreasing order**.

*Example:* If the input array $A$ is `1, 4, 3, 2, 6`, the sorted special array will be `2, 3, 6, 4, 1`.
*(Note: 1 is not a prime number. Here, 2 and 3 are prime and sorted increasingly; 6, 4, and 1 are non-prime and sorted decreasingly.)*

## Input
* The first line contains an integer $N$ denoting the total number of elements in array $A$.
* The next line contains $N$ space-separated integers representing the elements of array $A$.

## Output
Print the array elements separated by spaces after the special sorting is applied.

## Constraints
* $1 \leq N \leq 10^5$
* $1 \leq A[i] \leq 10^6$

## Examples:
### Example 1:
**Sample Input:**
```
5
1 4 3 2 6
```
**Sample Output:**
```
2 3 6 4 1 
```
**Explaination:**  
.