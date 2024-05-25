from tkinter import *
from tkinter import messagebox
from ics import Calendar, Event
from datetime import datetime, timedelta
from pytz import timezone
import os
import webbrowser
from tkinter import filedialog


def create_event():
    # Get input values
    date = date_entry.get()
    start_time = time_entry.get()
    length = length_entry.get()
    name = name_entry.get()

    # Validate date
    try:
        year, month, day = map(int, date.split('-'))
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
        length = int(length)
        if length <= 0:
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

    #Event Details
    e = Event()
    e.name = name

    #Set timezones
    est = timezone('US/Eastern')

    # Parse date and start time
    year, month, day = map(int, date.split('-'))
    hour, minute = map(int, start_time.split(':'))
    e.begin = datetime(year, month, day, hour, minute, 0, tzinfo=est)

    # Set event length
    e.end = e.begin + timedelta(hours=int(length))

    #Add event to calendar
    c.events.add(e)

    #open a file dialog to choose where to save the ics file
    filename = filedialog.asksaveasfilename(defaultextension=".ics")

    #Save calendar to ICS file
    if filename:
        with open(filename, 'w') as f:
            f.writelines(c)

        #Open ICS file in default calendar app
        webbrowser.open(filename)

        #Show success message
        messagebox.showinfo("Success", "Event added to calendar")

# Create a new Tkinter window
window = Tk()

# Create input fields
Label(window, text="Date (YYYY-MM-DD)").pack()
date_entry = Entry(window)
date_entry.pack()

Label(window, text="Start Time (HH:MM)").pack()
time_entry = Entry(window)
time_entry.pack()

Label(window, text="Length (hours)").pack()
length_entry = Entry(window)
length_entry.pack()

Label(window, text="Event Name").pack()
name_entry = Entry(window)
name_entry.pack()

# Create a button to add the event
Button(window, text="Add Event", command=create_event).pack()

# Start the Tkinter main loop
window.mainloop()