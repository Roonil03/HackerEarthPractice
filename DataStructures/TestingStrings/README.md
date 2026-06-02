# Testing Strings
## Description:
Mr X and Mr Y, his friend are programmers and testers respectively working in the same company. So, once they faced the following scenario :

Mr X wrote an application that took as input some user data. The data the application took as input was a string in some strange language. That language consisted of $K$ distinct letters. However, due to some issues, the application got corrupted and one particular String among many was lost.

However, Mr X had seen that String once before it got lost. He remembers some info about it. Particularly, he remembers the lost String had length equal to $M$.

Mr Y, being the chief QA person in his company needs to try and figure out the number of possible different possible candidate Strings for the lost String.

Mr X remembers $N$ pieces of info. For each one, he gives you 2 numbers $L$ and $R$ and a number $Z$. He remembers for sure that the $Z^{th}$ letter of the language of the string did not occur between positions $L$ and $R$ inclusive of the lost String.

## Input Format :

The first line contains 3 space separated integers $N$, $M$ and $K$.
Each of the next $N$ contains 3 space separated integers, denoting $L$, $R$ and $Z$ respectively.

## Output Format :

You need to find and print the number of different possible candidate Strings for the lost String based on the info Mr X remembers. As the number of such Strings can be large, print it Modulo $10^6 + 3$

## Constraints:

* $1 \le N, M, K \le 10^5$
* $1 \le L \le R \le M$
* $1 \le Z \le K$

## Examples:
### Example 1:
**Sample Input:**
```
1 2 26
1 2 1
```
**Sample Output:**
```
625
```
