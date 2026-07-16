# Monk and Suffix Sort
## Description:
Monk loves to play games. On his birthday, his friend gifted him a string $S$. Monk and his friend started playing a new game called as Suffix Game. In Suffix Game, Monk's friend will ask him lexicographically $k^{th}$ smallest suffix of the string $S$. Monk wants to eat the cake first so he asked you to play the game.

Video approach to solve this question: here

## Input Format:
First line contains a string $S$ ($1 \le |S| \le 25$) and an integer $k$ ($1 \le k \le |S|$).

## Output Format:
Print the lexicographically $k^{th}$ smallest suffix of the string $S$.

## Note:
Those who are not familiar with suffix and lexicographical order, can read about it from [https://en.wikipedia.org/wiki/Suffix](https://en.wikipedia.org/wiki/Suffix) and [https://en.wikipedia.org/wiki/Lexicographical_order](https://en.wikipedia.org/wiki/Lexicographical_order).

## Examples:
**Input:**
```
aacb 3
```
**Output:**
```
b
```
**Explaination:**  
All the suffices of the string are:  
aacb  
acb  
cb  
b  

After sorting the order of the suffices will be:  
aacb  
acb  
b  
cb  

3<sup>rd</sup> smallest suffix will be b.