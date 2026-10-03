people = [
    {'name': 'Орлов','grade':7,'hours':12},
    {'name': 'Белова','grade':9,'hours':20},
    {'name': 'Шаров','grade':10,'hours':16},
    {'name': 'Новикова','grade':8,'hours':9}
          ]
best = people[0]

def label(person):
    a = person['name']
    b = person['grade']
    c = person['hours']
    return f'{a},{b}-й класс,{c} ч.'

def senior(person):
    a = person['grade']
    return a >= 9

def best_h(person):
    a = person['hours']
    return a

def report(person):
    best = person[0]
    report = {'count':0,'total':0, 'max_name':''}
    report['count']=+len(person)
    for i in person:
        report['total']+=i['hours']
        if i['hours']>=best['hours']:
            best = i
    report['max_name']=best['name']
    return report
print(report(people))