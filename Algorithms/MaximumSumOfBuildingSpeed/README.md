# Maximum Sum of Building Speed
## Description:
You are the king of Pensville with $2N$ workers. All workers must be grouped into $N$ associations of size 2. The building speed of the $i^{th}$ worker is $A_i$.

When you form an association, the resultant building speed is the **minimum** building speed between the two workers in that association. Your goal is to maximize the sum of these resultant building speeds across all $N$ associations.

## Constraints
* $1 \leq N \leq 5 \times 10^4$
* $1 \leq A_i \leq 10^4$

## Input
* The first line contains an integer $N$, representing the number of associations to be made.
* The next line contains $2N$ space-separated integers, denoting the building speeds of the $2N$ workers.

## Output
* Print the maximum possible sum of the building speeds of all $N$ associations.

## Examples:
### Example 1:
**Sample Input:**
```
2
1 3 1 2
```
**Sample Output:**
```
3
```
**Explaination:**  
Consider workers with speeds $\{1, 3, 2, 4\}$. If you form associations using the first and third worker $(1, 2)$ and the second and fourth worker $(3, 4)$, the resultant building speeds are:
* Association 1: $\min(1, 2) = 1$
* Association 2: $\min(3, 4) = 3$
* Total sum: $1 + 3 = 4$