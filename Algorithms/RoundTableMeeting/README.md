# Round Table Meeting
## Description:
There are $N$ students in a round table meeting. Each student belongs to a university given in the array $A[i]$, which denotes the university that the $i^{th}$ student belongs to.  
There are $Q$ queries of the form $x$ $y$, denoting two universities. The answer to each query is the minimum time taken by any one of the student from these universities to meet each other.

### Note:
* Exactly 1 student of university $x$ and $y$ have to meet each other
* In this context, meeting means that the absolute distance between the positions is $\le 1$
* Time taken by the student to move from $i^{th}$ position to $i + 1^{th}$ or $i - 1^{th}$ position is exactly 1 second
* Both the students move together at the same time
* Both the students move optimally in the correct direction
* Two students can belong to the same university
* Round Table means that the nth position and 1st position are adjacent

## Input
- The first line of input contains 2 integers $N$ and $Q$
- The second line contains $N$ space seperated integers denoting $A[i]$
- $Q$ lines follow . Each containing 2 integers $x$ and $y$

## Output
The output contains $q$ lines each containing the answer to each query

## CONSTRAINTS
Contraint: $1 \le N \le 50000$, $1 \le Q \le 100$ The elements of the array are between 1 to 100000

$x$ and $y$ are guaranteed to be present in the array

## Examples:
### Example 1:
**Sample Input:**
```
10 4 
7 1 4 3 1 6 4 2 5 1 
3 4 
1 2
2 7
6 7
```
**Sample Output:**
```
0
1
1
2
```
**Explaination:**  
Positions : 1 2 3 4 5 6 7 8 9 10

Values : 7 1 4 3 1 6 4 2 5 1

Query 1: 3 and 4 are already adjacent , therefore answer is 0  
Query 2: 1 and 2, in this case there are three 1's present

Checking the answer for all the 1's

1(at posn 2) : Answer = 2  
1(at posn 5) : Answer= 1  
1(at posn 10) : Answer= 1  

Therefore answer=1;