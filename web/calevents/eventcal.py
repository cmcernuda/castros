from ics import Calendar, Event
from datetime import datetime, timedelta

# Create a new calendar
c = Calendar()

#Event Details
e = Event()
e.name = "Espinosa"
#Update with each event BRAND NAME
e.begin = datetime(2024, 5, 30, 16, 0)
#Date and time format: datetime(year, month, day, hour, minute)
e.end = e.begin + timedelta(hours=4)
e.location = "Castro's Back Room Bedford, 132 Bedford Center Rd, Bedford, NH 03110"
e.description = "Join us for an exclusive tasting of Espinosa Cigars. Special deals and swag available. Don't miss out!"
#Update with each event BRAND NAME

#Add event to calendar
c.events.add(e)

#Save calendar to ICS file
#Update with each event FILENAME
with open('Espinosa.ics', 'w') as f:
    f.writelines(c)

print("Event added to calendar")