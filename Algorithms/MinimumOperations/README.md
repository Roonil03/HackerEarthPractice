# Minimum operations
## Description:
You are given an array $A$ of size $N$. You can perform the following operation on array $A$:

* Select two indices $i$ and $j$ such that $1 \le i, j \le N$. (Note that $i$ and $j$ can be equal)
* Assign $A_i = A_i + 2$
* Then assign $A_j = A_j - 1$

You need to make all the elements of the array equal to zero.

### Task
Determine the minimum number of operations required to make all the elements of $A$ equal to zero. Else, print -1 if it is not possible to do so.

### Function description
Complete the function `solve()` provided in the editor. This function takes the following parameters and returns the required answer:

* $N$: Represents the size of the array $A$
* $A$: Represents the elements of array $A$.

## Input format
Note: This is the input format that you must use to provide custom input (available above the Compile and Test button).

* The first line contains $T$, denoting the number of test cases. $T$ also specifies the number of times you have to run the `solve()` function on a different set of inputs.
* For each test case:
    * The first line contains $N$, denoting the size of array $A$.
    * The second line contains space-separated values, denoting the elements of array $A$.

## Output format
For each test case, print the output on a new line. Either the minimum number of operations required to make all the elements of $A$ equal to zero or print -1 if it is impossible to do so.

## Constraints
* $1 \le T \le 1000$
* $1 \le N \le 10^5$
* $-10^9 \le A_i \le 10^9 \quad \forall 1 \le i \le N$
* $\sum N_i \le 10^5 \quad \forall 1 \le i \le T$

## Examples:
### Example 1:
**Sample Input:**
```
2
1
-2
2
1 -1
```
**Sample Output:**
```
2
-1
```
**Explaination:**  
The first line contains the number of test cases, $T = 2$.

*The first test case*  
**Given**
* $N = 1$
* $A = [-2]$

**Approach**  
We can perform the following operations on $A$:
* Select $i = 1, j = 1$, $A_1 = -2 + 2 = 0$ and $A_1 = 0 - 1 = -1$, $A$ becomes $[-1]$.
* Select $i = 1, j = 1$, $A_1 = -1 + 2 = 1$ and $A_1 = 1 - 1 = 0$, $A$ becomes $[0]$.  
Hence, all the elements are equal to zero after 2 operations. Thus, the answer is 2.

*The second test case*  
**Given**
* $N = 2$
* $A = [1, -1]$

**Approach**  
It can be shown that it is not possible to reduce all the elements of $A$ equal to zero simultaneously. Thus, the answer is -1.