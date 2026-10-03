people = [
    {'name': 'Орлов','grade':7,'hours':12},
    {'name': 'Белова','grade':9,'hours':20},
    {'name': 'Шаров','grade':10,'hours':16},
    {'name': 'Новикова','grade':8,'hours':9}
          ]

def label(person):
    a = person['name']
    b = person['grade']
    c = person['hours']
    return f'{a},{b}-й класс,{c} ч.'
def senior(person):
    a = person['grade']
    if a>= 9:
        return True
    else:
        return False
for i in people:
    if senior(i):
        print(label(i))