# name = input()                  # Reading input from STDIN
# print('Hi, %s.' % name)         # Writing output to STDOUT

# def sieve_of_eratosthenes(limit):
#     is_prime = [True] * (limit + 1)
#     is_prime[0] = is_prime[1] = False    
#     for i in range(2, int(limit**0.5) + 1):
#         if is_prime[i]:
#             for j in range(i*i, limit + 1, i):
#                 is_prime[j] = False    
#     return is_prime

# MAX_SUM = 1 * 10**5
# is_prime = sieve_of_eratosthenes(MAX_SUM)
# T = int(input())    
# for _ in range(T):
#     N = int(input())
#     A = list(map(int, input().split()))
#     Q = int(input())        
#     for _ in range(Q):
#         L, R = map(int, input().split())
#         L -= 1
#         R -= 1            
#         count = 0
#         for i in range(L, R + 1):
#             for j in range(i + 1, R + 1):
#                 sum_val = A[i] + A[j]
#                 if sum_val >= 2:
#                     count += 1            
#         print(count)

# T = int(input())    
# for _ in range(T):
#     N = int(input())
#     A = list(map(int, input().split()))
#     Q = int(input())        
#     for _ in range(Q):
#         L, R = map(int, input().split())
#         L -= 1
#         R -= 1        
#         range_size = R - L + 1
#         total_pairs = range_size * (range_size - 1) // 2        
#         count_0 = 0
#         count_1 = 0        
#         for i in range(L, R + 1):
#             if A[i] == 0:
#                 count_0 += 1
#             elif A[i] == 1:
#                 count_1 += 1        
#         pairs_sum_0 = count_0 * (count_0 - 1) // 2
#         pairs_sum_1 = count_0 * count_1        
#         result = total_pairs - pairs_sum_0 - pairs_sum_1
#         print(result)

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    zero = [0] * n
    one = [0] * n
    for i in range(n):
        if a[i] == 0:
            zero[i] = 1
        if a[i] == 1:
            one[i] = 1            
        if i > 0:
            zero[i] += zero[i - 1]
            one[i] += one[i - 1]    
    q = int(input())
    for _ in range(q):
        l, r = map(int, input().split())
        l -= 1
        r -= 1
        count_zeros = zero[r]
        if l > 0:
            count_zeros -= zero[l - 1]
        count_ones = one[r]
        if l > 0:
            count_ones -= one[l - 1]
        range_length = r - l + 1
        total_pairs = (range_length * (range_length - 1)) // 2
        pairs_sum_zero = (count_zeros * (count_zeros - 1)) // 2
        pairs_sum_one = count_zeros * count_ones        
        result = total_pairs - pairs_sum_zero - pairs_sum_one
        print(result)


def main():
    T = int(input())
    for _ in range(T):
        solve()

if __name__ == "__main__":
    main()