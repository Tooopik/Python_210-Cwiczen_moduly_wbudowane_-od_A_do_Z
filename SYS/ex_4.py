import sys

n = len(sys.argv)
result = 0
if n > 0:
    for i in range(1, n):
        result += int(sys.argv[i])

print(result)
