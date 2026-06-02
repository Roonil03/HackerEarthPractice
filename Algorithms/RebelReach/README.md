# RebelReach
## Description:
In a kingdom with $N$ cities connected by $N - 1$ roads, the king's palace is located in the first city. Each city has a specific number of guards, given in an array $Guards[]$, where $Guards[i]$ is the number of guards in the city $i$. The kingdom must assess the risk of revolts starting from any city and how close rebels could get to the king's palace. The guards' effectiveness is such that one guard can stop one rebel.

To tackle this, the king has asked you to develop a method for analyzing such scenarios. This includes answering queries of type 'query($U, X$)', where $U$ represents the city where the revolt might begin, and $X$ indicates the number of protestors at the start. Your task is to determine for each query the nearest city to the king's palace (i.e., city 1) that the rebels can reach.

*Note:* If the rebels can reach City 1, you should print City 1, as this is the city where the King's palace is located.

### Input format

* The first line contains a single integer $T$, which denotes the number of test cases.
* For each test case:
    * The first line contains $N$ denoting the number of Cities.
    * The following $N - 1$ lines contain 2 space-separated integers, $u$ & $v$ indicating that there is a road between City $u$ & City $v$
    * The next line contains N integers, denoting the array Guards.
    * The next line contains $Q$ denoting the number of queries.
    * The next $Q$ lines contain 2 space-separated integers, $U$ and $X$, where $U$ denotes the city where the revolt might begin, and $X$ indicates the number of rebels at the start.

### Output format

For each test case, answer all the $Q$ queries. For each query, print in a new line the nearest city to the king's palace (i.e., city 1) that the rebels can reach.

### Constraints

- $1 \le T \le 10^5$
- $3 \le N \le 10^6$
- $1 \le u, v \le N$
- $1 \le Guards[i] \le 10^9 \ \forall \ i \in [1, N]$
- $1 \le Q \le 10^6$
- $1 \le U \le N$
- $1 \le X \le 10^{15}$
- The sum of all values of N over all test cases doesn't exceed $10^6$
- The sum of all values of Q over all test cases doesn't exceed $10^6$

## Examples:
### Example 1:
**Sample Input:**
```
1
7
1 2
1 5
2 3
5 6
5 7
3 4
5 3 2 4 6 4 4
3
4 10
6 10
7 2
```
**Sample Output:**
```
1
5
7
```
**Explaination:**  
The first line denotes $T = 1$.

For test case 1:

We are given:

* $N = 7$, and the city connection looks like this:
  
  ![City Connection Graph Placeholder](https://he-s3.s3.amazonaws.com/media/uploads/c57f3475-12c5-40d4-ac3d-4a4850ff27d8.png)
  
* Guards in each of the cities are : $[5, 3, 2, 4, 6, 4, 4]$
* We need to answer 3 queries.

Now,

1. For the first query, 10 rebels start from city 4.
    * out of 10, 6 rebels can reach City 3, 2 rebels will be stopped at City 3 & 4 can reach City 2, 3 rebels will be stopped here & 1 can reach City 1. Hence, the answer to this query is 1.
2. For the second query, 10 rebels start from city 6.
    * out of 10, 6 rebels can reach city 5, and 0 can reach city 1, as all 6 rebels will be stopped at city 5. Hence the answer for this query is 5.
3. For the third query, 3 rebels start from city 7.
    * out of 3, 0 can reach city 5, as all 3 rebels will be stopped at city 7. Hence the answer for this query is 7.