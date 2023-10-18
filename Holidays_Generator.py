# Import your dependencies
import os
import sys
import re
import calendar
from datetime import date
import datetime
from nylas import Client
from dotenv import load_dotenv

# Load your env variables
load_dotenv()

# Initialize your Nylas API client
nylas = Client(
    api_key = os.environ.get("V3_API_KEY"),
)

# Array to hold all events
yearly_events = []
# Months of the year
months = range(1, 13)
# Year that we want to print out
year = str(sys.argv[1])

# Path of file
file_name = (
    "/Users/blag/Library/Mobile Documents/iCloud~md~obsidian/Documents/Blag/Holidays Calendar "
    + year
    + ".md"
)

# Use RegEx to filter out by year
regex = re.compile(year)

# Get first half of the year
START_TIME = int(datetime.datetime(int(year), 1, 1, 0, 0, 0).strftime('%s'))
END_TIME = int(datetime.datetime(int(year), 12, 31, 23, 0, 0).strftime('%s'))

# Define the query parameters
query_params = {"calendar_id": os.environ.get("HOLIDAY_CALENDAR")}
query_params['start'] = START_TIME
query_params['end'] = END_TIME
query_params['limit'] = 200

# Get all events from our Holidays Calendar
events = nylas.events.list(os.environ.get("GRANT_ID") , query_params = query_params).data

# Store all events in an array
for event in events:
    yearly_events.append(event.when.date + " " + event.title)

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
        filtered_month = [event for event in yearly_events if regex.match(event)]
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
