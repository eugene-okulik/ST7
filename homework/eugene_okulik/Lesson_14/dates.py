import datetime


now = datetime.datetime.now()
print(now)
today_midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
# today_midnight = now.replace(hour=23, minute=59, second=59, microsecond=999999)
print(today_midnight)
after_midnight = now - today_midnight
print(after_midnight)
print(type(after_midnight))
print(after_midnight.days)
print(after_midnight.microseconds)
birth = datetime.datetime.fromisoformat('1985-01-04 10:20:00.000000')
print((now - birth).days, 'days')
ten_days = datetime.timedelta(days=10)
print(now + ten_days)
