from datetime import datetime


date_str_1 = '3 March 1995'
date_str_2 = '3/9/1995'
date_str_3 = '21-07-2021'

print(datetime.strptime(date_str_1, '%d %B %Y'))
print(datetime.strptime(date_str_2, '%d/%m/%Y'))
print(datetime.strptime(date_str_3, '%d-%m-%Y'))
