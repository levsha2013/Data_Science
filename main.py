import pandas as pd
from statsmodels import robust
from collections import defaultdict

table = pd.read_csv('googleplaystore.csv')

category_count = defaultdict(int)
for i in table['Category']:
    category_count[i] += 1
print(category_count)

count_type = defaultdict(int)
for i in table['Type']:
    count_type[i] += 1

count_year = defaultdict(int)
for i in table['Last Updated']:
    count_year[i.split(",")[-1]] += 1

count_installs = defaultdict(int)
for i in table['Installs']:
    count_installs[i] += 1

count_rating = defaultdict(int)
for i in table['Content Rating']:
    count_rating[i] += 1

count_genres = defaultdict(int)
for i in table['Genres']:
    count_genres[i] += 1

count_size = defaultdict(int)
for i in table['Size']:
    count_size[i.replace('M', "")] += 1

print('End')
"""for i in table.keys():
    print(f'\t{i}')
    if type(table[i][1]) != str:
        print(table[i].mean())
        print(f"медиана - {table[i].median()}")
        print(f"стандартное отклонение - {table[i].std()}")
        print(f"робастная оценка медианного абсолютного значение - {robust.scale.mad(table[i])}")
        print(f"межквартильный размех (0.75-0.25) - {table[i].quantile() - table[i].quantile()}")"""
