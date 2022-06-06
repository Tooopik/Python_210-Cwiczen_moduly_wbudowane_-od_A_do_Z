import os

names = [name for name in os.listdir(path=None) if name.startswith('e')]

print(sorted(names))
