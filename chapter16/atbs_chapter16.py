# Removing the Header from CSV Files
"""
#! python3
# Removes the header from all CSV files in the current working directory.

import csv, os

os.makedirs('headerRemoved', exist_ok=True)

# Loop through every file in the current working directory.
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue    # skip non-csv files
    print('Removing header from ' + csvFilename + '...')

        # Read the CSV file in (skipping first row).
    csvRows = []
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue    # skip first row
        csvRows.append(row)
    csvFileObj.close()

    # Write out the CSV file.
    csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w',
                newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()
"""

# Fetching Current Weather Data

#! python3
# Prints the weather for a location from the command line.

import json, requests, sys, os
from dotenv import load_dotenv

load_dotenv() # load .env
APPID = os.getenv("Open_Weather_API_KEY")

# Compute location from command line arguments.
if len(sys.argv) < 2:
    print('Usage: getOpenWeather.py city_name, 2-letter_country_code')
    sys.exit()

if not APPID:
    print('Missing Open_Weather_API_KEY in .env')
    sys.exit(1)

location = ' '.join(sys.argv[1:])

# Use 3-hourly forecast endpoint; we'll sample ~now, +24h, +48h
url = 'https://api.openweathermap.org/data/2.5/forecast?q=%s&APPID=%s' % (location, APPID)
response = requests.get(url)
response.raise_for_status()

# Load JSON data into a Python variable.
weatherData = json.loads(response.text)

# Pick entries ~0h, 24h, 48h ahead (3h steps -> 8 entries per day)
lst = weatherData['list']
if len(lst) < 17:
    print('Not enough forecast data returned.')
    sys.exit(1)

w = [lst[0], lst[8], lst[16]]  # keep your w[0], w[1], w[2] usage below

# Print weather descriptions.
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])