# Two Groups
## Description:
There are $N$ people in a room.  
Your task is to find the number of ways to divide the people in the room into two groups $A$ and $B$, such that each group contains at least one member.  
As the number of ways can be large, print the output modulo $10^9 + 7$.

## Input Format
* First line contains the number of test cases, $T$.
* Next $T$ lines contain $N$ denoting the number of people in a room.

## Output Format
* For each test case, print the number of ways as modulo $10^9 + 7$ in a new line.

## Constraints
* $1 \le T \le 10^5$
* $1 \le N \le 10^9$

## Examples:
### Example 1:
**Sample Input:**
```
1
2
```
**Sample Output:**
```
2
```
**Explaination:**  
In case 1: There are 2 people in the room, so there are two ways, i.e.:  
a) Group 1: $1^{st}$ Person, Group 2: $2^{nd}$ Person  
b) Group 1: $2^{nd}$ Person, Group 2: $1^{st}$ Person  