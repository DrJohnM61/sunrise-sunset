#
# This code will print out the dawn, sunrise, sunset and dusk times for a location for the entire year
#
# It converts the time into the local time (seems that the sun function does not work with all
# time zones correctly and the lookup function does not work with all cities.
# Idear is to pipe this to a file and import as a CSV
#
# John Maton 6th July 2022
#
from astral import LocationInfo
from astral.geocoder import database, lookup
from dateutil import tz
import datetime
from astral.sun import sun
#
# Set the from and to zones as from UTC to Local
#
from_zone = tz.tzutc()
to_zone = tz.tzlocal()
#
# set the city information
#
city = LocationInfo("Vancouver", "Canada", "UTC", 49.29081917790567, -123.12730486714607)
#
# Altrnativly, use the following function call to lookup the city information
#
#city = lookup("Seattle", database())


print((
    f"Information for {city.name}/{city.region}\n"
    f"Timezone: {city.timezone}\n"
    f"Latitude: {city.latitude:.02f}; Longitude: {city.longitude:.02f}\n"
))

print("Date,Dawn,Sunrise,Sunset,Dusk")
#
# From today
#
date=datetime.date.today()
#
# Add a day each step of the loop
#
time_change = datetime.timedelta(days=1)
#
# do for 365 days
#
for x in range(365):

    s = sun(city.observer, date)

    utc = s['dawn']
    utc = utc.replace(tzinfo=from_zone)
    local = utc.astimezone(to_zone)
    print(local.strftime("%m/%d/%Y,%H:%M:%S"), end = '')

    utc = s['sunrise']
    utc = utc.replace(tzinfo=from_zone)
    local = utc.astimezone(to_zone)
    print(local.strftime(",%H:%M:%S"), end = '')

    utc = s['sunset']
    utc = utc.replace(tzinfo=from_zone)
    local = utc.astimezone(to_zone)
    print(local.strftime(",%H:%M:%S"), end = '')

    utc = s['dusk']
    utc = utc.replace(tzinfo=from_zone)
    local = utc.astimezone(to_zone)
    print(local.strftime(",%H:%M:%S"))

    date = date + time_change
