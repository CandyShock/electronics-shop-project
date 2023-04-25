import csv


def sds():
    with open('../src/items.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        rows = []
        for row in reader:
            rows.append([row['name'], row['price'], row['quantity']])
        return rows



