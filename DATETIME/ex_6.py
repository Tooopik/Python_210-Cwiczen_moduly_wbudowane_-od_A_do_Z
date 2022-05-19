from datetime import datetime

data = datetime(2021, 4, 20, 11, 30)

print(datetime.strftime(data, '%Y-%m-%d'))
print(datetime.strftime(data, '%d-%m-%Y'))
print(datetime.strftime(data, '%m-%Y'))
print(datetime.strftime(data, '%B-%Y'))
print(datetime.strftime(data, '%d %B, %Y'))
print(datetime.strftime(data, '%Y-%m-%d %H:%M:%S'))
print(datetime.strftime(data, '%m/%d/%Y %H:%M:%S'))
print(datetime.strftime(data, '%d(%a) %B %Y'))
