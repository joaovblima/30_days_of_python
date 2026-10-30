from datetime import date, datetime

today = date(year=2019, month=12, day=5)
new_year = date(year=2020, month=1, day=1)
time_left_for_new_year = new_year - today
print('time left for new year: ', time_left_for_new_year)

t1 = datetime(year = 2019, month = 12, day = 5, hour = 0, minute = 59, second = 0)
t2 = datetime(year= 2020, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t2 - t1
print('time left for new year = ', diff )