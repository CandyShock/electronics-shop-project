import csv

def sds():
    with open('items.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            emp_str1 = (row['name'], row['price'], row['quantity'])
            return ", ".join(emp_str1)



#a = sds()
#print(len(a))