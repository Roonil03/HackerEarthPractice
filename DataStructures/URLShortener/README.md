# URL shortener
## Description:
You have a URL-shortening service that registered users can use to create custom short links for any website. The service can also be used through an API which has the following requirements:

* There is a rate limit of 5 seconds for every user, i.e, the user must wait for at least 5 seconds after using the service before using it again.
* The URL provided must begin with either `http://` or `https://`.
* The custom key chosen must be between 2 and 12 characters long (inclusive), and consist of alphabets and numbers only.
* The custom key should not be taken already (the custom key must be unique).

If all the conditions are met, then the custom key is added to the database and it redirects to the given website. The database is empty before the first query and after that, the custom keys of successful queries are added to the database one by one.

You will be given a list of queries made to the API in chronological order. Determine whether each query is successful. Each query will contain the following:

* *time*: The epoch time at which the query was made.
* *URL*: The URL of the original website.
* *key*: The custom key.
* *userId*: An integer that identifies the particular user who made the query.

### Task
You are given $N$ queries. If a query is successful, print "YES" else print "NO".

### Example
**Assumptions**
* $N = 4$
* *queries* = [["1000000000", "https://www.google.com", "gg1", "25"], ["1000000004", "https://www.youtube.com", "yt", "25"], ["1000000004", "hackerearth.com", "he", "50"], ["1000000005", "https://www.facebook.com", "FB", "25"]]

**Approach**
* The first query is successful so we print "YES".
* For the second query, the user with id 25 already made a successful query in the last 5 seconds, so this query fails and we print "NO".
* For the third query, the provided URL does not begin with either `http://` or `https://` so this query fails and we print "NO".
* The fourth query is valid as 5 seconds have passed since the last successful query for the user with id 25, we print "YES".

**Function description**
Complete the function *solve* provided in the editor. This function takes the following 2 parameters and returns the required answer:
* $N$: Represents the number of queries
* *queries*: Represents a 2D array of N rows and 4 columns denoting the queries

## Input format
Note: This is the input format that you must use to provide custom input (available above the **Compile and Test** buttons).
* The first line contains a single integer $N$, denoting the number of queries.
* Each of the next $N$ lines contains 4 values - the time, URL, key, and user id for the corresponding query.

## Output format
For each query, print either "YES" or "NO" (case-sensitive) depending on whether the query is successful or not.

## Constraints
* $1 \leq N \leq 10000$
* $1 \leq \text{time.length} \leq 10$
* $1 \leq \text{URL.length} \leq 100$
* $1 \leq \text{key.length} \leq 20$, key could contain alphanumeric and special characters as well.
* $1 \leq \text{userId.length} \leq 10$

## Examples:
### Example 1:
**Input:**
```
4
1000000000 https://www.google.com gg1 25
1000000004 https://www.youtube.com yt 26
1000000004 https://HackerEarth.com he 50 
1000000005 https://www.facebook.com F!B 25
```
**Output:**
```
YES
YES
YES
NO
```
**Explaination:**  
* All the first queries are successful so we print "YES", except for the last query. The last query contains a special character in the key (F!B) itself so it's invalid that's why the answer will be "NO" for the last one.