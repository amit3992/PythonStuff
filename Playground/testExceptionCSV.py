import csv
import os
try:
    with open('examples.csv') as csvFile:
        readCSV = csv.reader(csvFile, delimiter=",")
        dates = []
        colors = []

        for row in readCSV:
            color = row[3]
            date = row[0]

            dates.append(date)
            colors.append(color)

        print(dates)
        print(colors)
except Exception as e:
    print(e)
