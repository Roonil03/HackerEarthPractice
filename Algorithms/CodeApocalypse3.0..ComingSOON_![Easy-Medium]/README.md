# Code Apocalypse 3.0 ..Coming SOON ![Easy-Medium]
## Description:
Cypher guys are ready for the grand event Code Apocalypse!!.
Questions are prepared, Promotions just begun ( from this question, LOL! ). But there is one problem they are facing. What should they do if there is a tie on the final day.
To solve this dilemma, Ayush came up with a tie breaker problem (although this can't be disclosed), give a try to solve it :

You have an army of N unsullied soldiers, you can upgrade a soldier to be stronger by feeding him X magical apples (found beyond the wall!). Initially, you have M magical apples.
You can buy extra magical apples ( from the Iron Bank! :P ), by selling one of your soldiers for Y apples.
Calculate what is maximum number of upgraded soldiers you can have for the long night.

**NOTE : You can upgrade a soldier once only, and, You cannot sell an upgraded soldier.**

## Input Format:
First Line consists of single integer T denoting number of testcases.  
Next T lines, consists of four integers, N, M, X, Y, denoting  
number of soldiers intially,  
number of magical apples initially,  
number of apples needed to upgrade one soldier, and  
number of apples for which a soldier can be sold respectively.

## Output Format:
For each testcase, print a single integer denoting the maximum number of soldiers which can be upgraded.

## Constraints:
- 1 <= T <= 2*10^5
- 1 < =N, M, X, Y <= 10^9

## Examples:
### Example 1:
**Sample Input:**
```
2
5 10 2 1
3 10 4 2
```
**Sample Output:**
```
5
2
```
**Explaination:**  
In the first test case, we can use all the M apples to upgrade to all the N soldiers.  
In the second test case, we can upgrade 2 soldiers with initial candy. but if we sell anyone of the soldiers, we will have 10 + 2= 12 apples, which enough to upgrade 3 soldiers, but there wouldn't be 3 soldiers to upgrade. So, the answer is 2.