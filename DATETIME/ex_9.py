import datetime

now = datetime.datetime.now()
endYear = datetime.datetime(now.year, 12, 31, 23, 59, 59, 999999)
diff = endYear - now

print(f'Until the end of the year: {diff}')
