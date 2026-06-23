# Group Photo
## Description:
You and your friends want to take group photos. The process of taking photos can be described as follows:

On the photo, each photographed friend occupies a rectangle of pixels: the $i^{th}$ of them occupies the rectangle of width $w_i$ pixels and height $h_i$ pixels. On the group photo, everybody stands in a line, thus the minimum pixel size of the photo including all the photographed friends is $W \times H$, where $W$ is the total sum of all widths and $H$ is the maximum height among the heights of all the photographed friends.

The friends made $n$ photos - the $j^{th}$ $(1 \le j \le n)$ photo had everybody except for the $j^{th}$ friend, as he was the photographer. Print the minimum size of each made photo in pixels.

## Input Format
* First line of the input will contain $n$ denoting the number of students.
* Next $n$ lines contain two integers each denoting $w_i$ and $h_i$. First line of these $n$ lines denotes the width and height occupied by the first student, second corresponds to the second student, and so on.

## Output Format
* Print $n$ space-separated numbers $b_1, b_2, \dots, b_n$, where $b_i$ is the total number of pixels on the minimum photo containing all friends except for the $i^{th}$ one.

## Constraints
* $1 \le n \le 2 \times 10^5$
* $1 \le w_i \le 10$
* $1 \le h_i \le 10^3$

## Examples:
### Example 1:
**Sample Input:**
```
3
2 10
1 9
3 7
```
**Sample Output:**
```
36 50 30 
```
**Explaination:**  
In the given sample we have a total of three people. When the first person is clicking the photograph, the width of the remaining two people is 4 and the maximum height among them is 9; thus, a minimum photograph of size 36 is required to capture both. In a similar manner, whenever person 2 or person 3 is the photographer, the minimum size of the photograph is 50 and 30, respectively.

