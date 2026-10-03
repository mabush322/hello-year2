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
    return int(a)

for i in people:
    if best_h(i)>best_h(best):
        best = i
print(label(best))