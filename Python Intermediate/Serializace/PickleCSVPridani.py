import csv

with open("data_textove", 'a') as out_file:
    writer = csv.writer(out_file)
    writer.writerow(["Jenny Scoot", 2500])