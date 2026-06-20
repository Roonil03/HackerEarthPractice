# Architect's Dilemma..!
## Description:
An Architect has been assigned a project and some number of workers work for him. Each of the workers is assigned a fixed amount of work. Suddenly, he has been appointed to build a new elegant office by the mayor. He won't disappoint mayor and finish the task as quickly as possible.  
Now, the architect has some amount of extra work to build the new office. He wants to assign this extra work to workers in such a way that there are maximum number of workers with same amount of total work. It might not be possible to give equal amount of work to each worker. He wants to find maximum number of workers possible with same amount of total work. It is not necessary that architect assigns all of his extra work.

## Input Format:

First line has two integers N , number of workers and W , amount of extra work architect has.
The second line contains N integers separated by single space, a1, a2, ... , an where ai is the amount of fixed work ith worker has.

## Output Format:

Output maximum number of workers that have equal amount of total work.

## Input Constraints:
- 1 <= N <= 10^5
- 1 <= W <= 10^7
- 1 <= a<sub>i</sub> <= 10^6

## Examples:
### Example 1:
**Sample Input:**
```
4 5
5 5 3 1
```
**Sample Output:**
```
3
```
**Explaination:**  
Architect gives two amount of work to 3rd worker. So 3 workers (1,2,3) have five amount of total work each.

There is no way that more than 3 worker can have equal amount of total work.