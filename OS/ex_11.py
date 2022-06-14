import os


fnames = [f"{str(i).zfill(2)}_sales.csv" for i in range(1, 25)]

for idx, name in enumerate(fnames):
    if idx < 12:
        print(os.path.join(os.getcwd(), '2020', name))
    else:
        print(os.path.join(os.getcwd(), '2021', name))
