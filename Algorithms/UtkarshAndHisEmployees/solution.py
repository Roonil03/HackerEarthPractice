import sys

input_data = sys.stdin.read().split()
print('\n'.join(str(int(n) * (int(n) - 1) // 2) for n in input_data[1:]))