import csv

with open('seniors.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f,fieldnames=(['name','grades','hours']))
    writer.writeheader()