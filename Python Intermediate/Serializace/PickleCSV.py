import csv

# cela_data = pd.read_csv("list_text")
#     print(cela_data)

with open("list_text") as in_file:
    reader = csv.reader(in_file)
    for row in reader:
        print(row)

# with open("list_text.txt.csv", 'a') as out_file:
#     writer = csv.writer(out_file)
#     writer.writerow(["Jenny Scoot", 2500])

# csv je textovy soubor ve formatu excel ale je to zapsane jako text5
import csv

with open('data_textove.txt') as in_file:
    reader = csv.reader(in_file)
    for row in reader:  # nacitame data po radcich aby nedoslo k preplneni pameti kdyz mame 'BIG data'
        print(row)

with open('data_textove.txt', 'a') as out_file:
    writer = csv.writer(out_file)
    writer.writerow(['Fero Lakatoš', 50000])