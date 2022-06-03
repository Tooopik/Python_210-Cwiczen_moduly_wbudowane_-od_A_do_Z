import datetime

date = datetime.datetime(2020, 1, 1)
diff_7_days = date + datetime.timedelta(days=7)
diff_30_days = date + datetime.timedelta(days=30)
diff_30_hours = date + datetime.timedelta(hours=30)
diff_15_minutes = date + datetime.timedelta(minutes=15)

print(diff_7_days)
print(diff_30_days)
print(diff_30_hours)
print(diff_15_minutes)
