# Countries Grouping
## Description:
People in the group, are sitting in a row numbered from $1$ to $N$. Every person have been asked with a same question as

How many people of your country are there in the group?

The answers provided may be **incorrect**. It is known that people of same countries always sit together.

If all the given answers are correct, determine the number of distinct countries present otherwise print "Invalid Data".

## Input Format:
First line contains one integer, which denotes the number of test cases

Each test case consists of 2 lines:

The first line contains one integer $N$, which denotes the total number of people there in the group.

The second line contains $N$ space-separated integers say $A_i$, which denotes the answer given by the $i^{th}$ person.

## Output Format:
For each test case output a single line containing a single integer denoting the distinct countries or "Invalid Data".

## Constraints:
- $1 \le T \le 1000$
- $1 \le N \le 100$
- $1 \le A_i \le 1000$

## Examples:
#### Example 1:
**Sample Input:**
```
4
2
1 1
2
1 3
7
1 1 2 2 3 3 3
7
7 7 7 7 7 7 7
```
**Sample Output:**
```
2
Invalid Data
4
1
```
**Explaination:**  
First test case, there are two people each from different country.