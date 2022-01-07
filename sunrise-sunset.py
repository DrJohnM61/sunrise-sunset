import datetime
from suntime import Sun, SunTimeException

latitude = 49.29081917790567
longitude = -123.12730486714607

sun = Sun(latitude, longitude)

abd = datetime.date.today()
print(abd)

time_change = datetime.timedelta(days=1)

for x in range(31):

# On a special date in your machine's local time zone

    abd_sr = sun.get_local_sunrise_time(abd)
    abd_ss = sun.get_local_sunset_time(abd)
    print('On {} the sun at 590 Nicola Street, raised at {} and get down at {}.'.
          format(abd, abd_sr.strftime('%H:%M'), abd_ss.strftime('%H:%M')))

    abd = abd + time_change
