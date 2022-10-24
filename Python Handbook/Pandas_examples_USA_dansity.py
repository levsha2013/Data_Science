import pandas as pd
import numpy as np

pop = pd.read_csv("USstates/state-population.csv")
areas = pd.read_csv("USstates/state-areas.csv")
abbrevs = pd.read_csv("USstates/state-abbrevs.csv")

print(pop.head())
print(areas.head())
print(abbrevs.head())

# объединим pop и abbrevs по аббревиатуре названия штата
merged = pd.merge(pop,abbrevs, how='outer', left_on='state/region', right_on='abbreviation')
merged = merged.drop('abbreviation', axis=1)    # раз объединил по столбцам, оба столбца не нужны, один удалить
print(merged.head())

# есть ли нулевые значения по столбцам?
print(merged.isnull().any())

# вывести те нулевые значения (по строкам, к какому штату нули относятся то?)
print(merged[merged['population'].isnull()].head())

# среди тех записей, где отсутствует state покажи state/region, чтобы понять, что за state там должен быть
print(merged.loc[merged['state'].isnull(), 'state/region'].unique())

# сделаем все state, где state/region=PR - Puerto Rico и где USA - United States и посмотрим, сколько еще Nan осталось?
merged.loc[merged['state/region'] == 'PR', 'state'] = 'Puerto Rico'
merged.loc[merged['state/region'] == 'USA', 'state'] = 'United States'
print(merged.isnull().any())

# объединим третий CSV - площадь, по state и если ли кроме population (puerto rico) еще Nan
final = pd.merge(merged, areas, how='left')
print(final.head())
print(final.isnull().any())

# где они - удалим, если не нужны. Проверим еще Nan
print(final.loc[final['area (sq. mi)'].isnull(), 'state/region'].unique())
final.dropna(inplace=True)
print(final.isnull().any())     # NAN больше нет - очистили!!!

"""Отсортируем штаты и территорию США по плотности населения на 2010 год"""
data2010 = final.query("year==2010 & ages == 'total'")
print(data2010.head())

data2010.set_index('state', inplace=True)
density = data2010['population']/data2010['area (sq. mi)']
density.sort_values(ascending=False, inplace=True)
print(density.head())