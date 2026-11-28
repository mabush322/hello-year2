import pandas as pd
# чмтаем csv как адекватную таблицу
table = pd.read_csv('club.csv',encoding='utf-8')

#Класс этих таблиц называется DataFrame
print(table)

#получение имен столбцов
print(table.columns)
print()

#обращение к отдельному столбцу
print(table['hours'])

#Сумма всех часов
print(table['hours'].sum())
print()

#отбор всех людей с классо больше 9
seniors = table[table['grade']>=9]
print((seniors))
print()

print(seniors[['name','hours']])
print()

#отбор всех людей с классом не меньше 9 и с часами не меньше 12      &-это 'и', |-это "или"
selected = table[(table['grade']>=9) | (table['hours']>16)]
print(selected)
print()
#сохранение в csv файл
seniors.to_csv('seniors.csv',index=False)

#сортировка по классу в порядке убывания
sorted_studs = table.sort_values('grade',ascending=False)
print(sorted_studs)
print()

table['seniors']= table['grade']>=9
print(table)
print('----------------------------------------------------------')

print(len(table[table['grade']>=9]))
print('----------------------------------------------------------')

print(table[table['hours']<16])
print('----------------------------------------------------------')

total_hours=table[(table['grade']>=8)&(table['grade']<=10)]
print(total_hours)
print('----------------------------------------------------------')
print('среднее арифметическое кол-во часов:',total_hours['hours'].sum()/len(total_hours))
print('----------------------------------------------------------')

#уникальные значения столбца
print(table['grade'].unique()[0])
print('----------------------------------------------------------')

a = table['grade'].unique()
for grade in a:
    b = table[table['grade']==grade]
    print(b['hours'].mean)
