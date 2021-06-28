import csv

def read_and_compare(p1, p2):
    names = []
    with open(p1, newline ='') as csvfile:
        reader = csv.DictReader(csvfile)
        mansions1 = [row1 for row1 in reader]
    with open(p2, newline ='') as csvfile:
        reader2 = csv.DictReader(csvfile)
        mansions2 = [row2 for row2 in reader2]
    mansions_all = []
    mansions_all.extend(mansions1)
    mansions_all.extend(mansions2)

    names = []
    for mansion in mansions_all:
        names.append(mansion['name'])
    
    allnames = set(names)

    deleted = []
    added = []
    modified = []
    for name in allnames:
        if name not in [m['name'] for m in mansions2]:
            deleted.append(name)
        elif name not in [m['name'] for m in mansions1]:
            added.append(name)
        else:
            for m in mansions1:
                if m['name'] == name:
                    for mn in mansions2:
                        if mn['name'] == name:
                            if m != mn:
                                keys = [k for k in m.keys()]
                                changes = []
                                for k in keys:
                                    if m[k] != mn[k]:
                                        changes.append(f'{m[k]} to {mn[k]}') 
                                modified.append(f'{name} changes: {changes}')



    return (f"Added: {added}, deleted: {deleted}, modified: {modified}")





print(read_and_compare('properties3.csv', 'properties4.csv'))