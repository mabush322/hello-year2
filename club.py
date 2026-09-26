people = [
    {'name': 'Орлов','grade':7,'hours':12},
    {'name': 'Белова','grade':9,'hours':20},
    {'name': 'Шаров','grade':10,'hours':16},
    {'name': 'Новикова','grade':8,'hours':9}
          ]

def label(person):
    a = str(person['name'])
    b = str(person['grade'])
    c = str(person['hours'])
    return a + ", " + b + ' класс, ' + c +' часов'
for i in people:
    print(label(i))