import os


paths = [os.path.join(
    os.getcwd(), f'dir_{str(i).zfill(2)}') for i in range(1, 14)]

for dir in paths:
    if not os.path.exists(dir):
        os.mkdir(dir)

if os.path.exists(paths[-1]):
    os.rmdir(paths[-1])

dirs = [dir for dir in sorted(os.listdir()) if len(dir) == 6]
print(dirs)
