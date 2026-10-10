import csv

total = 0
people = []

def person_from_row(row):
    a = {'name':row['name'],'grade':int(row['grade']),'hours':int(row['hours'])}
    return a
try:
    with open('club.csv',encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row = person_from_row(row)
            people.append(row)
except FileNotFoundError:
    print('Файл не найден.Он либо отсутствует либо перемещён')

with open('seniors.csv','w',encoding='utf-8',newline='') as f:
    writer = csv.DictWriter(f,fieldnames=(['name','grade','hours']))
    writer.writeheader()

    for row in people:
        if row['grade']>=9:
            writer.writerow(row)
for i in people:
    total += i['hours']
print(total)
