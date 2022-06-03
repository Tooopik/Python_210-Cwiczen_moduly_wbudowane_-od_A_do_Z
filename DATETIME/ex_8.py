import datetime

today = datetime.date.today()
yearEnd = datetime.date(today.year, 12, 31)
deltaDays = (yearEnd - today).days

print(f'Number of days until the end of the year: {deltaDays}')
