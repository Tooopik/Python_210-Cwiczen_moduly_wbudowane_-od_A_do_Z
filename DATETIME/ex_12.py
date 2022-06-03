import datetime

rate = 0.04
pv = 1000
startDate = datetime.date(2021, 7, 1)
endDate = datetime.date(2021, 12, 31)
dailyRate = rate/365
diff = endDate - startDate
fv = pv*(1+dailyRate)**diff.days
print(f'Future value: {fv:.2f} USD')
