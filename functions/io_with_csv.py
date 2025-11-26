import csv

def read_csv(file_name):
    data = []
    with open(file_name, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data




