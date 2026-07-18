# Max num
## Description:
Jehta a famous INTER-NIT player at delhi meets a girl and proposes her but she if so fond of mathematics that she doesn't wanna break with her BF as he is a top notch mathematician (We can not disclose). So to have better mathematician as her BF she challenges manish aka jetha and was given an array A of n elements $A_1, A_2, A_3 \dots A_n$.

Let us define a function $F(x) = \sum_{i=1}^n A_i \& x$

Here & represents BIT WISE AND operator.

He needs to find the number of different values of x for which $F(x)$ is maximized.

But there is a constraint for x that it must have exactly l bits-set in its binary representation.

Being a good mathematician(Self-Declared) he calculated the answer just to verify wants you to do as well.

Vacancies are still open as she found that both had back-logs in the semester exams(Problem setter has good chances :) ).

Your task is to find number of such values for which this function is maximised.

Print the required number.

If there are infinite such numbers output -1.

It can be proved that under the given constrainsts the value to be printed is either infinite or not greater than 1e18.

Video approach to solve this question: here

## Input:
First line will contain number of test cases T.

Second line of input will contain two space seprated integers n and l (As described in the problem).

Third and final line of input contains n space seprated integers $A_1, A_2, A_3 \dots A_n$.

## Output:
There will be T lines of output:

The only line of output for each test case contains a single integer as described in problem.

## Constraints:
- $1 <= T <= 1000$
- $1 <= l <= 30$
- $1 <= N <= 20000$
- $1 <= A[i] <= 1e9$
- As promised he is a good mathematician but no one wants too much burden so it is guaranteed that sum of N over all test cases will not exceed 2e5.

## Examples:
**Input:**
```
2
5 2 
3 5 7 1 4
5 1
3 5 7 1 4
```
**Output:**
```
2
1
```
**Explaination:**  
For the first test case both 5 and 6 can serve the purpose while in second test case only 4 satisfies the constraints.