# Good Evening sweetheart!![Medium]
## Description:
Scube sold you N candles, for each candle i you know its height H[i]​.​Using a candle during one evening decreases the candle height by 1. You plan to have at most M romantic evenings. For each evening i you know the number of candles C[i] you want to lit. Find a strategy of lighting the candles in order to maximize the number of evenings you can spend. You are forced to stop after the the night i when you can't light C[i] candles.
## Input Format:
The first line contains two integers N and M.  
The second line contains N integers representing the initial heights of the candles.  
The third line contains M integers representing the number of candles you want to lit each evening.

## Output Format:
Print a single integer representing the maximum number of evening you can spend, satisfying the candle requirements.

## Constraints
- 1≤N,M≤10^5
- 1<=H[i]<=10^5
- 1 <=C[i]<=10^5

## Examples:
### Example 1:
**Sample Input:**
```
3 5
1 2 5
1 2 3 2 1
```
**Sample Output:**
```
3
```
**Explaination:**  
One way spend 3 romantic evenings would be:  
Used candle are written in bold  
1 2 5 - before evening 1  
1 2 **4**- after evening 1  
1 1 **3**- after evening 2  
​0 0 **2**- after evening 3  
Note that you can't satisfy the requirements for evening 4, the answer is 3.  
Even though you can satisfy evening 5, you must spend the evenings in order .  
