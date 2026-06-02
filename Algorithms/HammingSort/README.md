# Hamming Sort
## Description:
Given an array of integers, denoted as $A$, and an integer $K$, your task is to implement a sorting algorithm. The goal is to arrange the elements in $A$ based on their Hamming Distance from the integer $K$.

The **Hamming Distance** is defined as the count of differing bits in the binary representations of two integers.

The sorting should be done in ascending order of Hamming distance, and in case of a tie in Hamming Distances, the elements should be sorted in ascending numerical order.

## Input Format:

*Note: This is the input format that you must use to provide custom input (available above the Compile and Test button).*

The first line contains $T$ denoting the number of test cases. $T$ also specifies the number of times you have to run the solve function on a different set of inputs. For each test case:

* The first line contains the integer $N$ and $K$.
* The second line contains the array $A$ of length $N$

## Output Format:

For each test case, print the answer in a new line.

## Constraints:

* $1 \le T \le 10$
* $1 \le N \le 10^5$
* $1 \le K \le 10^5$
* $1 \le A[i] \le 10^5$

## Examples:
### Example 1:
**Sample Input:**
```
1
3 2
4 5 6
```
**Sample Output:**
```
6 4 5
```
**Explaination:**  
In the example, binary representation of \(K = 2\) is "\(10\)". Similarly for array \([4,5,6]\), the binary representation is \( [100, 101, 110]\). Now the hamming distance of each element of the array with \(K\) are \([2,3,1]\). Hence sorting on the basis of Hamming Distance, the final output comes out to be \([6,4,5]\).