def solve (n, nums):
    # Write your code here
    digit_sum_freq = {}    
    def get_digit_sum(num):
        total = 0
        while num > 0:
            total += num % 10
            num //= 10
        return total    
    for num in nums:
        ds = get_digit_sum(num)
        digit_sum_freq[ds] = digit_sum_freq.get(ds, 0) + 1    
    pairs = 0
    for freq in digit_sum_freq.values():
        if freq > 1:
            pairs += freq * (freq - 1) // 2    
    return pairs
n = int(input())
nums = list(map(int, input().split()))

out_ = solve(n, nums)
print (out_)