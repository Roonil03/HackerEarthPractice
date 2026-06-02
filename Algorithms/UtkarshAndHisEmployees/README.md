# Utkarsh and his employees.
## Description:
Utkarsh as the HR of Apple Inc. has to select candidates for hiring. He has been given **N** candidates and he can only select candidates that are adjacent to each other. You have to tell that in how how many ways he can select employees.

He has to select at least two candidates.

### Input Format
The first line contains a single integer T the number of test cases.

Than for every test case there is the n the number of candidates

### Output Format
For each test case there is single output number as said in the above question.

### Constraints
- 1 < t < 10^5
- 2 < n < 10^9

### Examples:
#### Example 1:
**Sample Input:**
```
3
2
4
5
```
**Sample Output:**
```
1
6
10
```
**Explaination:**  
For Test Case 1:  
The number of candidates are 2 so you can only select them in one way.  
So answer is 1.  

For Test Case 2:  
He can select candidates in following ways :  
`{1,2}`, `{2,3}`, `{3,4}`, `{1,2,3}`, `{2,3,4}`, `{1,2,3,4}`  
So answer is 6.  
