import csv

def sds():
    with open('items.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
             print(row['name'], row['price'], row['quantity'])


