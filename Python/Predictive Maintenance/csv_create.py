import csv
import time

HEADER = ['LIGHT', 'VOLTAGE']

# ...


def processing_loop(csvfile):
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(HEADER)

    # ...
    while True:
        light = ReadChannel(light)
        voltage =  ConvertVoltage(light)
        csv_writer.writerow([light, voltage])
        csvfile.flush()
        time.sleep(5)


with open('results.csv', 'w') as csvfile:
    processing_loop(csvfile)