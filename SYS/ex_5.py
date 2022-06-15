import sys

n = len(sys.argv)
result = 0

if n > 1:
    for idx in range(1, n):
        result += int(sys.argv[idx])
    print(f'{result/(n-1):.4f}')
else:
    print('No values were given.')
