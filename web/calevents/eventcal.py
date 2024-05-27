from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from ics import Calendar, Event
from datetime import datetime, timedelta
from pytz import timezone
import os
import subprocess
from tkinter import filedialog
#import sys
#print(sys.executable)


def create_event():
    # Get input values
    date = date_entry.get()
    start_time = time_entry.get()
    length = length_entry.get()
    name = name_entry.get()

    # Validate date
    try:
        month, day, year = map(int, date.split('-'))
        datetime(year, month, day)  # This will raise a ValueError if the date is not valid
    except ValueError:
        messagebox.showerror('Error', 'Invalid date')
        return

    # Validate start time
    try:
        hour, minute = map(int, start_time.split(':'))
        if not (0 <= hour < 24 and 0 <= minute < 60):
            raise ValueError
    except ValueError:
        messagebox.showerror('Error', 'Invalid start time')
        return

    # Validate length
    try:
        hours, minutes = map(int, length.split(':'))
        if hours < 0 or minutes < 0 or minutes >= 60:
            raise ValueError
    except ValueError:
        messagebox.showerror('Error', 'Invalid length')
        return

    # Validate name
    if not name:
        messagebox.showerror('Error', 'Invalid event name')
        return
    
    # Create a new calendar
    c = Calendar()

    #Create Event
    #Event name
    e = Event()
    e.name = name

    #Set timezones
    est = timezone('US/Eastern')

   # Parse date
    month, day, year = map(int, date_entry.get().split('-'))
    e.begin = datetime(year, month, day)

    #parse start time
    hour, minute = map(int, start_time.split(':'))
    if am_pm.get() == 'PM':
        hour += 12
    e.begin = e.begin.replace(hour=hour, minute=minute, second=0, tzinfo=est)

    # Parse length
    hours, minutes = map(int, length.split(':'))
    e.end = e.begin + timedelta(hours=hours, minutes=minutes)

    # Set location
    e.location = location_entry.get()

    # Set event details
    e.description = details_entry.get()

    #Add event to calendar
    c.events.add(e)

    #open a file dialog to choose where to save the ics file
    default_filename = f"{e.name}_{e.begin.strftime('%m-%d-%Y')}.ics"
    filename = filedialog.asksaveasfilename(defaultextension=".ics", initialfile=default_filename)

    #Save calendar to ICS file
    if filename:
        with open(filename, 'w') as f:
            f.writelines(c)

        #Open ICS file in default calendar app
        subprocess.run(['open', filename])

        #Show success message
        messagebox.showinfo("Success", "Event added to calendar")

# Create a new Tkinter window
window = Tk()

# Set window title
window.title("Event Calendar")

# Set window size
window.geometry('500x410')  # Set width and height

# Create input fields
Label(window, text="Event Name").pack()
name_entry = Entry(window)
name_entry.pack()

Label(window, text="Date (MM-DD-YYYY)").pack()
date_entry = Entry(window)
date_entry.pack()

Label(window, text="Start Time (HH:MM)").pack()
time_entry = Entry(window)
time_entry.pack()

# Create AM/PM selection
Label(window, text="AM/PM").pack()
am_pm = StringVar()
Radiobutton(window, text="AM", variable=am_pm, value="AM").pack()
Radiobutton(window, text="PM", variable=am_pm, value="PM").pack()

Label(window, text="Length (hours)").pack()
length_entry = Entry(window)
length_entry.pack()

Label(window, text="Location").pack() #new location field
location_entry = Entry(window)
location_entry.pack()

# Set Event Details
Label(window, text="Event Details").pack() # new event details field
details_entry = Entry(window)
details_entry.pack()

# Create a button to add the event
Button(window, text="Add Event", command=create_event).pack()

# Start the Tkinter main loop
window.mainloop()