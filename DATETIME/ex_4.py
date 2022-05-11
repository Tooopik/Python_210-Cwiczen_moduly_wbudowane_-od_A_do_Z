import datetime

deltaDays = abs(datetime.datetime(2020, 7, 21) -
                datetime.datetime(2020, 12, 31))

print(f'Number of days: {deltaDays.days}')

# ----------------------------------------------------------
d1 = datetime.date(2020, 7, 21)
d2 = datetime.date(2020, 12, 31)
diff = (d2 - d1).days
print(f'Number of days: {diff}')
