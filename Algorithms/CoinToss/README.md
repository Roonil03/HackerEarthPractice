# Coin Toss
## Description:
Messi and Ronaldo finally decide to see who is the greatest player by means of a game. And this time they don't play a game of football, rather a game of chance. In this game there is a ball $O$ which is initially with **Messi**. Each of them has a biased coin with them. Now in one game they play $k$ rounds. In each round whichever of them has the ball tosses their coin. If it's heads then he passes the ball to the other one, if it's tails then he keeps the ball. After the completion of the rounds whoever has the ball wins.

If they play the game $10^k$ times then find the expected number of times **Ronaldo** would win mod $10^9 + 7$. It is guaranteed that the expectation value would be an integer. Assume that the probability of heads coming on **Messi's** coin is $\frac{p_1}{10}$ and **Ronaldo's** coin is $\frac{p_2}{10}$.

## Input:
Single line containing three space separated integers $p_1, p_2, k$.

## Output:
Single Integer that is the answer to the problem.

## Constraints:
- $1 \le p_1 \le p_2 \le 9$
- $1 \le k \le 10^{18}$

## Examples:
### Example 1:
**Input:**
```
2 5 1
```
**Output:**
```
2
```
**Explaination:**  
Probability of heads on **Messi's** coin is $0.2$ and on **Ronaldo's** coin is $0.5$. Now **Messi** initially has the ball. The game is played $10^1=10$ times. Since there is only one round **Ronaldo** would win the game if **Messi** passes the ball to **Ronaldo**. The probability of that happening is $0.2$. Expected number of times **Ronaldo** would win if one game is played is $0.2$. Hence if they play $10$ games then expected number of times **Ronaldo** would win is $10 * 0.2 = 2$.