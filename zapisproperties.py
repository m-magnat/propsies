from faker import Faker
fake = Faker()
import random
buildingtype = ['mansion', 'apartment', 'castle', 'house', 'flat', 'stable']
import csv

records = []

for i in range(7):
    record = {'name': f'{fake.color_name()} Mansion', 'address': f'{fake.street_address()}', 'city': f'{fake.city()}', 'zip code': f'{fake.postcode()}', 'building type': f'{random.choice(buildingtype)}', 'lease price': f'{fake.random_int(min=100, max=999, step=1)} $'}
    records.append(record)

for r in records:
    print(r.get("name"))

with open("todo.pickle", 'wb') as f:
    pickle.dump(records, f)

with open("todo.pickle", "rb") as f:
    rec = pickle.load(f)
print(rec)

falsedate = fake.date(pattern='%Y-%m-%d', end_datetime=None)
print(falsedate)

print(records[5])
with open(f'properties1.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'address', 'city', 'zip code', 'building type', 'lease price']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for r in records:
        if r != records[4]:
            writer.writerow(r)

with open('properties1.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['name'], row['lease price'], row['city'])

with open(f'properties2.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'address', 'city', 'zip code', 'building type', 'lease price']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for r in records:
        if r != records[3]:
            writer.writerow(r)

with open(f'properties3.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'address', 'city', 'zip code', 'building type', 'lease price']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for r in records:
        if r == records[5]:
            r['city'] = f'{fake.city()}'
            writer.writerow(r)
        else:
            writer.writerow(r)

with open(f'properties4.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'address', 'city', 'zip code', 'building type', 'lease price']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for r in records:
        if r != records[5]:
            if r == records[2]:
                r['lease price'] = f'{fake.random_int(min=100, max=999, step=1)} $'
                writer.writerow(r)
            else:
                writer.writerow(r)
    


