import datetime

date_time = "2020-01-15 09:03:32.744178"
obj = datetime.datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S.%f')

extract_year = lambda x: x.year
extract_month = lambda x: x.month
extract_date = lambda x: x.day
extract_time = lambda x: x.strftime('%H:%M:%S.%f')

year = extract_year(obj)
month = extract_month(obj)
date = extract_date(obj)
time = extract_time(obj)


print(date_time)
print(year)
print(month)
print(date)
print(time)
