import datetime

startDate = datetime.datetime(2020, 1, 1)
endDate = datetime.datetime(2020, 1, 4, 16)
dates = []

dates.append(startDate)
while True:
    if endDate not in dates:
        dates.append(dates[-1]+datetime.timedelta(hours=8))
    else:
        break

for date in dates:
    print(date)
