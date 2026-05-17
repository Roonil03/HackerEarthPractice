# Statistics of Strings
## Description:
Data science is very popular now. A lot of universities have courses about it. A lot of companies have open data science positions. So it's quite important to know how to work with statistics. And this task can help you to make first step into statistics.

Lets define $S$ as all strings of the length $n$ consisting of letters from the some alphabet of the size $a$. For each string $s$ lets define $f(s)$ - maximum among all z-function values of the string $s$. Your task is calculate $\sum_{s \in S} f(s)$ modulo $mod$.

You can read more about z-function on [https://e-maxx-eng.appspot.com/string/z-function.html](https://e-maxx-eng.appspot.com/string/z-function.html). Also in this problem we define $z_0 = 0$.

## Input Format:
First line of input contains three space separated integers $n$, $a$ and $mod$ ($1 \le n \le 22$, $1 \le a \le 10^9$, $1 \le mod \le 10^9$).

Note that $mod$ may be composite.

## Output Format:
Print the single integer $\sum_{s \in S} f(s)$ modulo $mod$.

## Examples:
### Example 1:
**Sample Input:**
```
3 2 1000
```
**Sample Output:**
```
8
```
**Explaination:**  
1. $f(aaa) = 2$
2. $f(aab) = 1$
3. $f(aba) = 1$
4. $f(abb) = 0$
5. $f(baa) = 0$
6. $f(bab) = 1$
7. $f(bba) = 1$
8. $f(bbb) = 2$