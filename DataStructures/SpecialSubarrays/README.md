# Special Subarrays
## Description:
An array is said to be *special*, if we can break it down into subarrays where every subarray ($\text{length} > 1$) starts and ends with $0$ and rest all other numbers are $1$.

Given $N$ binary arrays.

Sam decided to write down all the distinct prefix subarrays of the given $N$ binary arrays on a paper (he'll write distinct prefix only). After that he counts the number of special subarrays in every prefix and sum that up (a special subarray will be counted as many times as it is contained in each prefix).

Find the sum found by Sam modulo $10^9 + 7$.

## Input Format:

* The first line contains $N$ denoting the number of binary arrays.
* The $i^{th}$ of the next $N$ lines contains the binary array in form of a string $S[i]$.

## Output Format:

Sum found by Sam modulo $10^9 + 7$

## Constraints:

- $1 \le N \le 10^3$
- $1 \le |S[i]| \le 10^5$
- $1 \le \sum_{i=1}^N |S[i]| \le 2 \times 10^6$

## Examples:
**Sample Input:**
```
3
00
10
001011
```
**Sample Output:**
```
8
```
**Explaination:**  
There are 8 different unqiue prefixes, count of special subarray in each prefix is listed below

* $0 \to 0$ special subarrays
* $1 \to 0$ special subarrays
* $10 \to 0$ special subarrays
* $00 \to 1$ special subarray $[0, 0]$
* $001 \to 1$ special subarray $[0, 0]$
* $0010 \to 2$ special subarrays $[0, 0]$ and $[0, 1, 0]$
* $00101 \to 2$ special subarrays $[0, 0]$ and $[0, 1, 0]$
* $001011 \to 2$ special subarrays $[0, 0]$ and $[0, 1, 0]$