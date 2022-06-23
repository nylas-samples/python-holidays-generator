# Import your dependencies
import os
import sys
import re
import calendar
from datetime import date
import datetime
from nylas import APIClient
from dotenv import load_dotenv

# Load your env variables
load_dotenv()

# Initialize your Nylas API client
nylas = APIClient(
    os.environ.get("CLIENT_ID"),
    os.environ.get("CLIENT_SECRET"),
    os.environ.get("ACCESS_TOKEN"),
)

# Array to hold all events
yearly_events = []
# Months of the year
months = range(1, 13)
# Year that we want to print out
year = str(sys.argv[1])

# Path of file, replace it with your own path
file_name = (
    "/Users/YOUR_USER/Library/Mobile Documents/iCloud~md~obsidian/Documents/YOUR_FOLDER/Holidays Calendar "
    + year
    + " .md"
)

# Comment this if you want to use Regex
START_TIME = int(datetime.datetime(int(year), 1, 1, 0, 0, 0).strftime('%s'))
END_TIME = int(datetime.datetime(int(year), 12, 31, 23, 0, 0).strftime('%s'))

# Use RegEx to filter out by year
# Comment this line if you want to use Regex
regex = re.compile(year)

# Uncomment this line if you want to use RegEx
# Get all events from our Holidays Calendar
#events = nylas.events.where(calendar_id=os.environ.get("HOLIDAYS_CALENDAR_ID"))

# Comment this if you want to use Regex
events = nylas.events.where(calendar_id=os.environ.get("HOLIDAYS_CALENDAR_ID"), 
starts_after = START_TIME, ends_before = END_TIME)

# Store all events in an array
for event in events:
    yearly_events.append(event.when["date"] + " " + event.title)

# Use our RegEx to get only events happening on the requested year

# Uncomment this line if you want to use RegEx
#filtered_events = [event for event in yearly_events if regex.match(event)]
# Comment this if you want to use Regex
filtered_events = yearly_events

# Open the file to write to it
with open(file_name, "w") as f:
    f.write(f"**Holidays Calendar {year}**\n\n")
    # Loop months to get events for each of them
    for month in months:
        if month < 10:
            s_month = "0" + str(month)
        else:
            s_month = str(month)
        # Get only the current month using RegEx
        regex = re.compile(".*-" + s_month + "-.*")
        filtered_month = [event for event in filtered_events if regex.match(event)]
        # Print name of month
        f.write(f"|{calendar.month_name[month]}| |")
        f.write("\n|-|-|")
        # If we have events for that month, print them out
        if len(filtered_month) > 0:
            for filtered in filtered_month:
                # We want to get the day the event happens
                day = re.findall("(..\s)", filtered)
                # And we want the event title
                event = re.findall("(\s.*)", filtered)
                f.write(f"\n|{day[0]}|{event[0]}|")
            f.write("\n\n")
        else:
            f.write("\n\n")
# Close the file
f.close()
