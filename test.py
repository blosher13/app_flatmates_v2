import calendar
import datetime

# x = datetime.datetime.strptime('December', '%B')

month_name = list(calendar.month_name).index('December')

# print(list(calendar.month_name))
# period_month = int(str(datetime.datetime.strptime('December', '%B')))
# period_year = 2024

# num_days = calendar.monthrange(period_year, period_month)

# print(num_days)

x = 'December 2024'

period_month = str(x.split()[0])
month = list(calendar.month_name).index(period_month)

period_year = int(x.split()[1])

# print(month, period_year)

num_days = calendar.monthrange(period_year, month)[1]
print(num_days)