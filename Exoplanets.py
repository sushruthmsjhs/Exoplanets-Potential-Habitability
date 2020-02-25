import csv

with open('exoplanets.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print (row['fpl_hostname'])
