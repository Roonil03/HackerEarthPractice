# Reunion of 1's
## Description:
You are given a string of size **n** consisting of **0s** and/or **1s**. You have to perform total **k** queries and there are **two** types of queries possible:

1. "1" (without quotes): Print length of the longest sub-array which consists of all '1'.
2. "2 X" (without quotes): where **X** is an integer between **1** to **n**. In this query, you will change character at the Xth position to '1' (It is possible that the character at i-th position was already '1').

## Input Format
* First line of input contains **n** and **k**, where **n** is the length of the string, **k** is the number of queries.
* Next line contains a string of 0's and/or 1's of length **n**.
* Each of next **k** lines contains query of any one type(i.e 1 or 2).

## Input Constraints
* $1 \le n, k \le 10^5$
* $1 \le X \le n$
* String contains only 0s and/or 1s.
* Each query is of one of the mentioned types.

## Output Format
* For each query of type 1, print in a new line the maximum size of the subarray with all 1's

## Examples:
### Example 1:
**Sample Input:**
```
5 7
00000
1
2 3
1
2 5
1
2 4
1
```
**Sample Output:**
```
0
1
1
3
```
**Explaination:**  
- Initially there are no 1's in the string, hence the answer is 0.
- In second query of type '1' state of string is 00100, hence answer is 1.
- In Third query of type '1' state of string is 00101, hence answer is 1.
- In Fourth query of type '1' state of string is 00111, hence answer is 3.