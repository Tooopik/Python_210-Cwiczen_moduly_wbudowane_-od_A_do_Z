import os

names = sorted([name for name in os.listdir(
    path=None) if name.endswith('.py')])
print(names)
