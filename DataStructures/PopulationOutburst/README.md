# Population outburst
## Description:
A new species is trying to rule the planet. This species is creating their own population outburst to dominate other species. It all started with 1 single member of the species. The population increases in treelike fashion abiding by few rules as listed below.

* Single member is able to reproduce by itself.
* A new member is added to the population every minute.
* Every member is associated with integral name.
* Multiple members can share a common name.
* Every member has it's own reproduction capacity, that is maximum number of children it can reproduce.
* A member can start to reproduce only if all members older than it have exhausted their reproduction capacity.
* Level 0 in family tree of this species comprise of single member at the start of multiplication.
* Integral name of single member at the start is 0.
* The population grows level wise, where number of members at level i is dependent on reproduction capacity of members at prior level.

Given the integral name of new member and it's reproduction capacity that is added to the population, you have to find it's parent, level at which it is added and it's ascending age wise rank among siblings.

## Input:
First line of the input contains 2 integers, $N, RC_0$, representing number of minutes we will be examining the population increase and reproduction capacity of member at epoch. Next $N$ line contains 2 integers each, $ID_i, RC_i$, representing integral name and reproduction capacity of new member born at time $i$.

## Output:
N lines, each line containing 3 integers, $P, L, C$, representing integral name of the parent, level at which it is added and it's ascending age wise rank among siblings.

### Note:
It will always be possible to reproduce a new child or in other words, through out the given time, there exists atleast one member which can still accomodate new child.

## Constraints:
- $1 \le N \le 10^6$
- $-10^9 \le ID_i \le 10^9$
- $0 \le RC_i \le 10^9$

## Examples:
### Example 1:
**Sample Input:**
```
9 2
1 2
2 1
5 2
4 1
10 0
15 0
21 0
23 1
42 100
```
**Sample Output:**
```
0 1 1
0 1 2
1 2 1
1 2 2
2 2 1
5 3 1
5 3 2
4 3 1
23 4 1
```
**Explaination:**  
The resultant family tree looks like this.  
<img src="https://he-s3.s3.amazonaws.com/media/uploads/54a935a.png"><br>