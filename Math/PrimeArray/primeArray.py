# name = input()                  # Reading input from STDIN
# print('Hi, %s.' % name)         # Writing output to STDOUT

def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False
    return is_prime

MAX_VAL = 10**5
is_prime = sieve_of_eratosthenes(MAX_VAL)
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))    
    count_ones = 0
    primes = []    
    for i in range(N):
        if A[i] == 1:
            count_ones += 1
        elif A[i] <= MAX_VAL and is_prime[A[i]]:
            primes.append(i)    
    if count_ones >= 2:
        result = len(primes) * count_ones * (count_ones - 1) // 2
    else:
        result = 0    
    print(result)