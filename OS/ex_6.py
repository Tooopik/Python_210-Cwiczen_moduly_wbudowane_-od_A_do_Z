import os

os.mkdir('documents')
os.chdir('documents')

for month in range(1, 13):
    if month < 10:
        os.mkdir('0'+str(month)+'_sales')
    else:
        os.mkdir(str(month)+'_sales')

print(sorted(os.listdir()))
